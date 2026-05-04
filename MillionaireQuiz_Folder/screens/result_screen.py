# Result screen: shows win/lose/take-money message and navigation buttons



# Load GUI library
import tkinter as tk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App

# Result Screen container with font, size and positioning
class ResultScreen(tk.Frame):
    def __init__(self, parent: tk.Widget, app: "App") -> None:
        super().__init__(parent)
        self.app = app

        content = tk.Frame(self)
        content.pack(expand=True)

        self.title_lbl = tk.Label(content, text="", font=("Arial", 20, "bold"))
        self.title_lbl.pack(pady=(0, 14))

        self.msg_lbl = tk.Label(content, text="", font=("Arial", 13),
                                wraplength=660, justify="center")
        self.msg_lbl.pack(pady=(0, 18))

        btns = tk.Frame(content)
        btns.pack()


# Create buttons: Play again and Menu with font style,size and positioning
        tk.Button(btns, text="Play again", width=16, command=self.play_again).grid(row=0, column=0, padx=8)
        tk.Button(btns, text="Menu", width=16, command=lambda: self.app.show("MainMenu")).grid(row=0, column=1, padx=8)


# Set result title and message
    def set_result(self, title: str, message: str) -> None:
        self.title_lbl.config(text=title)
        self.msg_lbl.config(text=message)


# Play again button action
    def play_again(self) -> None:
        self.app.reset_game()
        self.app.show("StartGame")
