# Game screen: shows questions/options, checks answers, updates winnings, ends game


# Import Tkinter to build the GUI (buttons, labels, frames).
import tkinter as tk
from tkinter import messagebox
from typing import TYPE_CHECKING, List, Dict




from data.constants import PRIZES       # Importing the prize structure for the game
from data.db import fetch_game_questions            # Function to fetch game questions from the database



if TYPE_CHECKING:
    from app import App
    from screens.result_screen import ResultScreen



# This screen is the main game screen: shows the current question, shows 4 answer buttons, checks if the answer is correct, updates money and question number, can finish the game and go to ResultScreen
class GameScreen(tk.Frame):



    def __init__(self, parent: tk.Widget, app: "App") -> None:                             # This run only one time, when the app starts, it creates all GUI elements: labels, buttons, frames.
        super().__init__(parent)
        self.app = app

        self.game_questions: List[Dict] = []




        content = tk.Frame(self)                # Create an empty container to hold all other GUI elements
        content.pack(expand=True)





        self.header = tk.Label(content, text="", font=("Arial", 12, "bold"))                # Header label showing player name, question number, next prize, current winnings (also font settings)
        self.header.pack(pady=(0, 12))

        self.question_label = tk.Label(         # Create label to show the question text
            content,
            text="",
            font=("Arial", 16, "bold"),         # font Arial, size 16 and bold style
            wraplength=660,                      # Wrap text to fit within 660 pixels
            justify="center",                   # Position: center text inside label
        )
        self.question_label.pack(pady=(0, 14))

        self.answer_frame = tk.Frame(content)
        self.answer_frame.pack(pady=(0, 14))        # Positioning the frame





        self.answer_buttons: list[tk.Button] = []
        for i in range(4):          # Create cycle for 4 buttons for the answer options
            btn = tk.Button(
                self.answer_frame,
                text=f"Option {i + 1}",
                width=38,
                height=2,
                command=lambda idx=i: self.choose(idx),
            )
            btn.grid(row=i // 2, column=i % 2, padx=10, pady=8)
            self.answer_buttons.append(btn)

        bottom = tk.Frame(content)
        bottom.pack()


# Create Take money button:
        self.take_btn = tk.Button(bottom, text="Take money", width=16, command=self.take_money)
        self.take_btn.grid(row=0, column=0, padx=8)



# Create menu button:
        tk.Button(bottom, text="Menu", width=16, command=lambda: self.app.show("MainMenu")).grid(
            row=0, column=1, padx=8
        )

    def on_show(self) -> None:
        if self.app.current_index == 0:         # If it's the first question, take new questions from the database
            try:
                self.game_questions = fetch_game_questions()
            except ValueError as ex:        # Check if database is valid
                messagebox.showerror("DB error", str(ex))       # If not, then show error message
                self.app.show("MainMenu")       # Return to main menu 
                return

        self.render_question()

    def render_question(self) -> None:           # if, else statement to update header text and next prize
        i = self.app.current_index
        next_prize = PRIZES[i] if i < len(PRIZES) else PRIZES[-1]



# Update header text with player name, question number, next prize, current winnings
        self.header.config( 
            text=(
                f"Player: {self.app.player_name}  |  "
                f"Question: {i + 1}/10  |  "
                f"Next: €{next_prize}  |  "
                f"Current: €{self.app.current_win}"
            )
        )


# Enable or disable the Take money button based on current winnings
        self.take_btn.config(state=("normal" if self.app.current_win >= 100 else "disabled"))


# Get the current question and update the question label and answer buttons
        q = self.game_questions[i]
        self.question_label.config(text=q["text"])

        for idx, option in enumerate(q["options"]):
            self.answer_buttons[idx].config(text=option, state="normal")



# When an answer is chosen, check if it's correct, update winnings and question number or finish the game
    def choose(self, idx: int) -> None:
        i = self.app.current_index
        q = self.game_questions[i]
        correct = q["correct"]

        if idx == correct:
            self.app.current_win = PRIZES[i]
            self.app.current_index += 1


            
# if,else: After 10 questions finish text
            if self.app.current_index >= 10:
                self.finish("You won!", f"You won €{self.app.current_win}. Congratulations!")
            else:
                self.render_question()

# if,else: If player lose, show this message:
        else:
            self.finish("Game over", "Wrong answer. Your winnings are lost.")



#Player choose take money option, show this message:
    def take_money(self) -> None:
        self.finish("You took the money", f"You took €{self.app.current_win}. Game finished.")



# Show last screen with result message:
    def finish(self, title: str, message: str) -> None:
        result_frame: "ResultScreen" = self.app.frames["ResultScreen"]  # type: ignore[assignment]
        result_frame.set_result(title, message)
        self.app.show("ResultScreen")
