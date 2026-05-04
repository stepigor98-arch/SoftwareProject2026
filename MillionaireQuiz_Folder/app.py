# Main application: creates the window, stores global state, and switches between screens



import tkinter as tk


#Load database initialization
from data.db import init_db
from screens.main_menu import MainMenu
from screens.start_game import StartGame
from screens.game_screen import GameScreen
from screens.result_screen import ResultScreen
from screens.question_bank import QuestionBank
from screens.question_form import QuestionForm
from screens.statistics import Statistics


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        init_db()


# Set window properties
        self.title("Millionaire Quiz")
        self.geometry("720x420")
        self.resizable(True, True)

# Game state
        self.player_name: str = ""
        self.current_index: int = 0
        self.current_win: int = 0

# Admin state
        self.form_mode: str = "add"          # "add" | "edit"
        self.selected_question_id: int | None = None

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames: dict[str, tk.Frame] = {}
        for FrameClass in (
            MainMenu,
            StartGame,
            GameScreen,
            ResultScreen,
            QuestionBank,
            QuestionForm,
            Statistics,
        ):
            frame = FrameClass(parent=container, app=self)
            self.frames[FrameClass.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show("MainMenu")


# Show a screen by its name, choose screen on top, check screen status
    def show(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()
        on_show = getattr(frame, "on_show", None)
        if callable(on_show):
            on_show()


# Resets game progress to start a new game
    def reset_game(self) -> None:
        self.current_index = 0
        self.current_win = 0
