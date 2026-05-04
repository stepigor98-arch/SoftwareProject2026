## SoftwareProject2026
Software Engineering (for education)


## Main project - Millionaire quiz - improving and finalizing the game


# Description about project:

  Millionaire Quiz is a desktop quiz application developed in Python using Tkinter and SQLite. 
The application allows users to play a quiz game similar to “Who Wants to Be a Millionaire”, answer 10 questions, receive virtual prize money, and finish the game early after reaching a minimum prize level. 


# Core features:

  - Start a quiz game with player name
  - Answer 10 questions with 4 answer options
  - Prize progression for correct answers
  - “Take money” option after several correct answers
  - SQLite database for storing questions
  - Admin panel for adding, editing, deleting questions
  - Search and filtering by keyword, difficulty, and category
  - Statistics about questions by category and difficulty level


  # What can be improved during the course?

1. Game Settings
2. Lifelines
3. Game History in SQLite
4. Leaderboard
5. Improved Interface Design
6. CSV Import / Export

# Course ending - final version (plan)
1. Game Settings
- choose number of questions: 5, 10, 15, 20
- choose difficulty mode: easy, medium, hard, mix

2. Lifelines
- 50/50: removes two wrong answers
- Second Chance: allows one mistake during the game (work only before answering)

3. Game History in SQLite
- save last games
- save player name
- save question text
- save selected answer
- save correct answer
- save prize after correct answer
- mark correct answer in green

4. Leaderboard
- show best players by name
- sort by highest prize (name should be the same as in first game)
- show date/result of the game 

5. Improved Interface Design
- better colors
- cleaner buttons
- prize ladder
- highlighted correct/wrong answers
- more modern layout

6. CSV Import / Export
- import questions from CSV file
- export question bank to CSV
