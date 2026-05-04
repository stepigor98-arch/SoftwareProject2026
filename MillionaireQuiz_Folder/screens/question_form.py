# Admin form: add or edit a question (text, 4 options, correct option, level, category)



# Load GUI libraries
import tkinter as tk
from tkinter import messagebox, ttk
from typing import TYPE_CHECKING


# Load database functions
from data.db import add_question, get_question_by_id, update_question

if TYPE_CHECKING:
    from app import App

LEVELS = ["easy", "medium", "hard", "expert"]

# Question Form Screen
class QuestionForm(tk.Frame):
    def __init__(self, parent: tk.Widget, app: "App") -> None:
        super().__init__(parent)
        self.app = app

        content = tk.Frame(self)
        content.pack(fill="both", expand=True, padx=14, pady=12)


# Title
        self.title_lbl = tk.Label(content, text="", font=("Arial", 18, "bold"))
        self.title_lbl.pack(anchor="w", pady=(0, 10))


# Create form
        form = tk.Frame(content)
        form.pack(fill="x")


# Question Text
        self.text_var = tk.StringVar()
        tk.Label(form, text="Question text:").grid(row=0, column=0, sticky="w")
        tk.Entry(form, textvariable=self.text_var, width=80).grid(row=1, column=0, columnspan=2, sticky="w", pady=(2, 10))


# Options
        self.opt_vars = [tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()]
        labels = ["Option A:", "Option B:", "Option C:", "Option D:"]


# Cycle which show options to answer and check correct one 
        r = 2
        for i in range(4):
            tk.Label(form, text=labels[i]).grid(row=r, column=0, sticky="w")
            tk.Entry(form, textvariable=self.opt_vars[i], width=45).grid(row=r, column=1, sticky="w", pady=2)
            r += 1

        self.correct_var = tk.IntVar(value=0)
        tk.Label(form, text="Correct option:").grid(row=r, column=0, sticky="w", pady=(8, 2))
        cf = tk.Frame(form)
        cf.grid(row=r, column=1, sticky="w", pady=(8, 2))
        for i, t in enumerate(["A", "B", "C", "D"]):
            tk.Radiobutton(cf, text=t, variable=self.correct_var, value=i).pack(side="left", padx=(0, 10))
        r += 1

        self.level_var = tk.StringVar(value="easy")
        tk.Label(form, text="Level:").grid(row=r, column=0, sticky="w", pady=(6, 2))
        ttk.Combobox(form, textvariable=self.level_var, values=LEVELS, width=12, state="readonly").grid(
            row=r, column=1, sticky="w", pady=(6, 2)
        )
        r += 1



# Category
        self.category_var = tk.StringVar(value="General")
        tk.Label(form, text="Category:").grid(row=r, column=0, sticky="w", pady=(6, 2))
        tk.Entry(form, textvariable=self.category_var, width=30).grid(row=r, column=1, sticky="w", pady=(6, 2))



# Buttons
        btns = tk.Frame(content)
        btns.pack(fill="x", pady=(12, 0))
        tk.Button(btns, text="Save", width=12, command=self.save).pack(side="left", padx=(0, 8))
        tk.Button(btns, text="Cancel", width=12, command=lambda: self.app.show("QuestionBank")).pack(side="left")

    def on_show(self) -> None:
        mode = self.app.form_mode
        qid = self.app.selected_question_id

        if mode == "edit" and qid is not None:
            self.title_lbl.config(text=f"Edit Question (ID {qid})")
            q = get_question_by_id(int(qid))
            if not q:
                messagebox.showerror("Error", "Question not found.")
                self.app.show("QuestionBank")
                return

            self.text_var.set(q["text"])
            for i in range(4):
                self.opt_vars[i].set(q["options"][i])
            self.correct_var.set(q["correct"])
            self.level_var.set(q["level"])
            self.category_var.set(q["category"])
        else:
            self.title_lbl.config(text="Add New Question")
            self.text_var.set("")
            for v in self.opt_vars:
                v.set("")
            self.correct_var.set(0)
            self.level_var.set("easy")
            self.category_var.set("General")

    def save(self) -> None:
        text = self.text_var.get().strip()
        options = [v.get().strip() for v in self.opt_vars]
        category = self.category_var.get().strip()


#Error messages for validation
        if text == "":
            messagebox.showwarning("Validation", "Question text is required.")
            return
        if "" in options:
            messagebox.showwarning("Validation", "All 4 options are required.")
            return
        if len(set(options)) != 4:
            messagebox.showwarning("Validation", "Options must be different.")
            return
        if category == "":
            messagebox.showwarning("Validation", "Category is required.")
            return

        correct = int(self.correct_var.get())
        level = self.level_var.get()

        if self.app.form_mode == "edit" and self.app.selected_question_id is not None:
            update_question(int(self.app.selected_question_id), text, options, correct, level, category)
        else:
            add_question(text, options, correct, level, category)

        self.app.show("QuestionBank")
