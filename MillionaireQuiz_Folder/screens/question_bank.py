# Admin screen: shows question list with search/filters and buttons to add/edit/delete questions



#Loads GUI library
import tkinter as tk
from tkinter import messagebox, ttk
from typing import TYPE_CHECKING



# Import database functions
from data.db import delete_question, get_categories, list_questions

if TYPE_CHECKING:
    from app import App



# Levels for filtering questions
LEVELS = ["All", "easy", "medium", "hard", "expert"]




# This screen is the Question Bank (Admin) screen: shows list of questions, allows filtering, adding, editing, deleting questions
class QuestionBank(tk.Frame):
    def __init__(self, parent: tk.Widget, app: "App") -> None:
        super().__init__(parent)
        self.app = app


# Create a container for all GUI elements
        content = tk.Frame(self)
        content.pack(fill="both", expand=True, padx=14, pady=12)


# Title label with font, font size and position
        tk.Label(content, text="Question Bank (Admin)", font=("Arial", 18, "bold")).pack(anchor="w", pady=(0, 10))


        # Filters
        f = tk.Frame(content)
        f.pack(fill="x", pady=(0, 10))
        f.grid_columnconfigure(1, weight=1)


# Search box, Level dropdown, Category dropdown, Apply and Reset buttons
        tk.Label(f, text="Search:").grid(row=0, column=0, sticky="w")
        self.search_var = tk.StringVar()
        tk.Entry(f, textvariable=self.search_var).grid(row=0, column=1, padx=(6, 12), sticky="ew")

        tk.Label(f, text="Level:").grid(row=0, column=2, sticky="w")
        self.level_var = tk.StringVar(value="All")
        ttk.Combobox(f, textvariable=self.level_var, values=LEVELS, width=10, state="readonly").grid(
            row=0, column=3, padx=(6, 12), sticky="w"
        )

        tk.Label(f, text="Category:").grid(row=0, column=4, sticky="w")
        self.category_var = tk.StringVar(value="All")
        self.category_cb = ttk.Combobox(f, textvariable=self.category_var, values=["All"], width=16, state="readonly")
        self.category_cb.grid(row=0, column=5, padx=(6, 12), sticky="w")

        rbtn = tk.Frame(f)
        rbtn.grid(row=0, column=6, sticky="e")
        tk.Button(rbtn, text="Apply", width=10, command=self.refresh).pack(side="left", padx=(0, 8))
        tk.Button(rbtn, text="Reset", width=10, command=self.reset_filters).pack(side="left")




        # Table
        t = tk.Frame(content)
        t.pack(fill="both", expand=True)

        cols = ("id", "level", "category", "text")
        self.tree = ttk.Treeview(t, columns=cols, show="headings")
        


        for c, title, w, a in (             # Positioning and size of columns
            ("id", "ID", 60, "center"),
            ("level", "Level", 90, "center"),
            ("category", "Category", 120, "center"),
            ("text", "Question", 380, "w"),
        ):
            self.tree.heading(c, text=title)
            self.tree.column(c, width=w, anchor=a)


#Create scrollbar for table
        sb = ttk.Scrollbar(t, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)
        self.tree.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")




        # Bottom buttons
        b = tk.Frame(content)
        b.pack(fill="x", pady=(10, 0))


# Create Add, Edit, Delete, Back buttons
        for txt, cmd in (("Add", self.add), ("Edit", self.edit), ("Delete", self.delete)):
            tk.Button(b, text=txt, width=12, command=cmd).pack(side="left", padx=(0, 8))

        tk.Button(b, text="Back", width=12, command=lambda: self.app.show("MainMenu")).pack(side="right")


# Load categories and refresh the question list
    def on_show(self) -> None:
        self.load_categories()
        self.refresh()


# Load categories into the Category dropdown
    def load_categories(self) -> None:
        values = ["All"] + get_categories()
        self.category_cb["values"] = values
        if self.category_var.get() not in values:
            self.category_var.set("All")


# Reset filters to default values
    def reset_filters(self) -> None:
        self.search_var.set("")
        self.level_var.set("All")
        self.category_var.set("All")
        self.refresh()


# Refresh the question list based on current filters
    def refresh(self) -> None:
        self.tree.delete(*self.tree.get_children())
        rows = list_questions(self.search_var.get(), self.level_var.get(), self.category_var.get())
        for r in rows:
            self.tree.insert("", "end", values=(r["id"], r["level"], r["category"], r["text"]))



# Get the selected question ID from the table
    def _selected_id(self) -> int | None:
        sel = self.tree.selection()
        return int(self.tree.item(sel[0], "values")[0]) if sel else None


# Add new question
    def add(self) -> None:
        self.app.form_mode = "add"
        self.app.selected_question_id = None
        self.app.show("QuestionForm")


# Edit selected question
    def edit(self) -> None:
        qid = self._selected_id()
        if qid is None:
            messagebox.showwarning("Select", "Please select a question to edit.")
            return
        self.app.form_mode = "edit"
        self.app.selected_question_id = qid
        self.app.show("QuestionForm")


        
# Delete selected question
    def delete(self) -> None:
        qid = self._selected_id()
        if qid is None:
            messagebox.showwarning("Select", "Please select a question to delete.")
            return
        if messagebox.askyesno("Confirm", f"Delete question ID {qid}?"):
            delete_question(qid)
            self.load_categories()
            self.refresh()
