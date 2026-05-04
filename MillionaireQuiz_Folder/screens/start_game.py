# Start screen: collects player name and starts a new game



#Load GUI library
import tkinter as tk
from tkinter import messagebox
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App



# Create Label and entry for player name with font settings and positioning
class StartGame(tk.Frame):
    def __init__(self, parent: tk.Widget, app: "App") -> None:
        super().__init__(parent)
        self.app = app

        content = tk.Frame(self)
        content.pack(expand=True)

        tk.Label(content, text="Enter player name", font=("Arial", 16, "bold")).pack(pady=(0, 18))

        self.name_var = tk.StringVar()
        tk.Entry(content, textvariable=self.name_var, width=30, font=("Arial", 12)).pack(pady=(0, 18))

        btns = tk.Frame(content)
        btns.pack()



# Create buttons: Back and Start with font style,size and positioning
        tk.Button(btns, text="Back", width=12,
                  command=lambda: self.app.show("MainMenu")).grid(row=0, column=0, padx=8)
        tk.Button(btns, text="Start", width=12, command=self.start).grid(row=0, column=1, padx=8)


#display eroor message if name not entered
    def start(self) -> None:
        name = self.name_var.get().strip()
        if not name:
            messagebox.showwarning("Name", "Please enter your name.")
            return

        self.app.player_name = name
        self.app.reset_game()
        self.app.show("GameScreen")
