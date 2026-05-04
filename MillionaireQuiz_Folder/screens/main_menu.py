# Main menu screen: start game, open admin question bank, open statistics, exit



# Loads GUI library 
import tkinter as tk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App




# This screen is the main menu screen, it shows the game title and 4 buttons
class MainMenu(tk.Frame): 
    def __init__(self, parent: tk.Widget, app: "App") -> None:
        super().__init__(parent)
        self.app = app

        content = tk.Frame(self)                # Create an empty container to hold all other GUI elements
        content.pack(expand=True)



# Create label with font, font size, position with name "Millionaire Quiz":
        tk.Label(content, text="Millionaire Quiz", font=("Arial", 24, "bold")).pack(pady=(0, 12))




# Create label with font, font size, position with name "10 questions • 4 options • 1 correct":
        tk.Label(content, text="10 questions • 4 options • 1 correct", font=("Arial", 12)).pack(pady=(0, 22))




# Create 4 buttons with options: Start Game, Question Bank (Admin), Statistics, Exit
        tk.Button(content, text="Start Game", width=24, height=2,
                  command=lambda: self.app.show("StartGame")).pack(pady=8)

        tk.Button(content, text="Question Bank (Admin)", width=24, height=2,
                  command=lambda: self.app.show("QuestionBank")).pack(pady=8)

        tk.Button(content, text="Statistics", width=24, height=2,
                  command=lambda: self.app.show("Statistics")).pack(pady=8)

        tk.Button(content, text="Exit", width=24, height=2, command=self.app.destroy).pack(pady=8)
