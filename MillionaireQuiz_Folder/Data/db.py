# This file handles SQLite database: create table, seed data, CRUD, filters, game question selection, statistics


import os                   # path to DB - quiz.db
import sqlite3          # SQLite database operations

from typing import Dict, List, Optional, Tuple          # Type hints - for better code clearity 

from data.questions_bank import QUESTION_SEED           # Generate new database or edit already existed database

DB_PATH = os.path.join(os.path.dirname(__file__), "quiz.db")            # Path to the SQLite database file



def _conn() -> sqlite3.Connection:          # Opens the database file (quiz.db), “connecting to the database”
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c





def _rows(sql: str, params: tuple = ()) -> List[sqlite3.Row]:           # Runs a SELECT query and returns ALL matching rows as a list
    with _conn() as c:
        return c.execute(sql, params).fetchall()





def _one(sql: str, params: tuple = ()) -> Optional[sqlite3.Row]:            # Gives many results, example: “give me all questions” or “give me all categories”, return list of rows from the database
    with _conn() as c:
        return c.execute(sql, params).fetchone()





def _exec(sql: str, params: tuple = ()) -> None:          # Gives only one result, example: “give me question with id=5”, return single row from the database
    with _conn() as c:
        c.execute(sql, params)
        c.commit()





def _many(sql: str, params_list: List[tuple]) -> None:          # Does an action that CHANGES the database, such an add / update / delete / create table, then save changes
    with _conn() as c:
        c.executemany(sql, params_list)
        c.commit()






def init_db() -> None:      # Creates the table in the database if it does not exist yetб “make sure the DB structure is ready”
    _exec(
        """
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_index INTEGER NOT NULL CHECK (correct_index BETWEEN 0 AND 3),
            level TEXT NOT NULL CHECK (level IN ('easy', 'medium', 'hard', 'expert')),
            category TEXT NOT NULL DEFAULT 'General'
        )
        """
    )
    seed_questions_if_empty()






def seed_questions_if_empty() -> None:          # Checks if the questions table already has data (If there is at least 1 question, THEN do nothing) OR (If the table is empty, THEN insert the starter questions from QUESTION_SEED)
    r = _one("SELECT COUNT(*) AS cnt FROM questions")
    if r and int(r["cnt"]) > 0:
        return

    _many(
        """
        INSERT INTO questions
        (text, option_a, option_b, option_c, option_d, correct_index, level, category)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (
                q["text"],
                q["options"][0],
                q["options"][1],
                q["options"][2],
                q["options"][3],
                q["correct"],
                q["level"],
                q.get("category", "General"),
            )
            for q in QUESTION_SEED
        ],
    )





def _as_question(r: sqlite3.Row) -> Dict:             # Takes one database row and converts it into a normal Python dictionary
    return {
        "text": r["text"],
        "options": [r["option_a"], r["option_b"], r["option_c"], r["option_d"]],
        "correct": int(r["correct_index"]),
        "level": r["level"],
        "category": r["category"],
    }





def _random_by_level(level: str, limit: int) -> List[Dict]:             # Get random questions from the database for one difficulty level (easy/medium/hard/expert).
    return [
        _as_question(r)
        for r in _rows(
            """
            SELECT text, option_a, option_b, option_c, option_d, correct_index, level, category
            FROM questions
            WHERE level = ?
            ORDER BY RANDOM()
            LIMIT ?
            """,
            (level, limit),
        )
    ]






def fetch_game_questions() -> List[Dict]:       # Builds the full set of game questions (total 10) (3 easy + 3 medium + 3 hard + 1 expert)
    easy = _random_by_level("easy", 3)
    medium = _random_by_level("medium", 3)
    hard = _random_by_level("hard", 3)
    expert = _random_by_level("expert", 1)

    if min(len(easy), len(medium), len(hard)) < 3 or len(expert) < 1:
        raise ValueError("Not enough questions in DB. Need: easy>=3, medium>=3, hard>=3, expert>=1.")

    return easy + medium + hard + expert








# --- ADMIN ----



def get_categories() -> List[str]:          # Get from database all categories of questions (without duplicates) (example: "Math", "IT", "IT", "General", "General"), RESULT: "Math", "IT", "General")
    return [r["category"] for r in _rows("SELECT DISTINCT category FROM questions ORDER BY category")]







# Return questions for the admin table with filters: (keyword - search in question text) (level - easy/medium/hard/expert or All) (category - specific category or All) Use Question Bank screen to show the filtered list
def list_questions(keyword: str = "", level: str = "All", category: str = "All") -> List[Dict]:         
    sql = "SELECT id, text, level, category, correct_index FROM questions WHERE 1=1"
    params: List[object] = []

    kw = keyword.strip().lower()
    if kw:
        sql += " AND LOWER(text) LIKE ?"
        params.append(f"%{kw}%")

    if level != "All":
        sql += " AND level = ?"
        params.append(level)

    if category != "All":
        sql += " AND category = ?"
        params.append(category)

    sql += " ORDER BY id DESC"

    result: List[Dict] = []
    for r in _rows(sql, tuple(params)):
        result.append(
            {
                "id": int(r["id"]),
                "text": r["text"],
                "level": r["level"],
                "category": r["category"],
                "correct": int(r["correct_index"]),
            }
        )
    return result





def get_question_by_id(question_id: int) -> Optional[Dict]:          # Load one question by ID (primary key) for editing in the admin interface
    r = _one(
        """
        SELECT id, text, option_a, option_b, option_c, option_d, correct_index, level, category
        FROM questions
        WHERE id = ?
        """,
        (question_id,),
    )
    if not r:
        return None
    q = _as_question(r)
    q["id"] = int(r["id"])
    return q





def add_question(text: str, options: List[str], correct_index: int, level: str, category: str) -> None:         # Add a new question into database
    _exec(
        """
        INSERT INTO questions (text, option_a, option_b, option_c, option_d, correct_index, level, category)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (text, options[0], options[1], options[2], options[3], correct_index, level, category),
    )





def update_question(question_id: int, text: str, options: List[str], correct_index: int, level: str, category: str) -> None:        # Updates an existing question in the database by ID
    _exec(
        """
        UPDATE questions
        SET text = ?, option_a = ?, option_b = ?, option_c = ?, option_d = ?,
            correct_index = ?, level = ?, category = ?
        WHERE id = ?
        """,
        (text, options[0], options[1], options[2], options[3], correct_index, level, category, question_id),
    )






def delete_question(question_id: int) -> None:                  # Deletes one question from the database by ID.
    _exec("DELETE FROM questions WHERE id = ?", (question_id,))






# --- STATISTICS ---

def stats_questions_by_category() -> List[Tuple[str, int]]:                   # Counts how many questions exist in each category
    return [(r["category"], int(r["cnt"])) for r in _rows(
        "SELECT category, COUNT(*) AS cnt FROM questions GROUP BY category ORDER BY cnt DESC, category ASC"
    )]




def stats_questions_by_level() -> List[Tuple[str, int]]:                     # Counts how many questions exist in each difficulty level
    return [(r["level"], int(r["cnt"])) for r in _rows(
        """
        SELECT level, COUNT(*) AS cnt
        FROM questions
        GROUP BY level
        ORDER BY CASE level
            WHEN 'easy' THEN 1
            WHEN 'medium' THEN 2
            WHEN 'hard' THEN 3
            WHEN 'expert' THEN 4
            ELSE 5
        END
        """
    )]





def total_questions() -> int:                       # Count total questions in the database and show on screen
    r = _one("SELECT COUNT(*) AS cnt FROM questions")
    return int(r["cnt"]) if r else 0
