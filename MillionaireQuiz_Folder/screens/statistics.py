# Statistics screen: shows total questions and counts by category and by level



#Load GUI library
import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING


#Load database functions
from data.db import stats_questions_by_category, stats_questions_by_level, total_questions

if TYPE_CHECKING:
    from app import App


class Statistics(tk.Frame):
    def __init__(self, parent: tk.Widget, app: "App") -> None:
        super().__init__(parent)
        self.app = app

        # Root layout: content area + fixed bottom bar
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)

        content = tk.Frame(self)
        content.grid(row=0, column=0, sticky="nsew", padx=14, pady=12)


# Create title label
        tk.Label(content, text="Statistics", font=("Arial", 18, "bold")).pack(anchor="w", pady=(0, 8))


# Show total questions label
        self.total_lbl = tk.Label(content, text="", font=("Arial", 12))
        self.total_lbl.pack(anchor="w", pady=(0, 12))

        tables = tk.Frame(content)
        tables.pack(fill="both", expand=True)

# ----- Category table -----
        left = tk.Frame(tables)
        left.pack(side="left", fill="both", expand=True, padx=(0, 10))

        # Title for the category table
        tk.Label(left, text="Questions by Category", font=("Arial", 12, "bold")).pack(anchor="w", pady=(0, 6))


        # Create the table (Treeview) with 2 columns: category and count
        self.cat_tree = ttk.Treeview(left, columns=("category", "count"), show="headings", height=12)

        # Set column headers
        self.cat_tree.heading("category", text="Category")
        self.cat_tree.heading("count", text="Count")

        # Set column headers
        self.cat_tree.column("category", width=220, anchor="w")
        self.cat_tree.column("count", width=80, anchor="center")


        # Add vertical scrollbar for the table
        cat_scroll = ttk.Scrollbar(left, orient="vertical", command=self.cat_tree.yview)
        self.cat_tree.configure(yscrollcommand=cat_scroll.set)

        # Place table and scrollbar in the window
        self.cat_tree.pack(side="left", fill="both", expand=True)
        cat_scroll.pack(side="right", fill="y")

# --- Level table ---
        right = tk.Frame(tables)
        right.pack(side="left", fill="both", expand=True)


        # Title for the level table
        tk.Label(right, text="Questions by Level", font=("Arial", 12, "bold")).pack(anchor="w", pady=(0, 6))


        # Create the table (Treeview) with 2 columns: level and count
        self.level_tree = ttk.Treeview(right, columns=("level", "count"), show="headings", height=12)


        # Set column headers
        self.level_tree.heading("level", text="Level")
        self.level_tree.heading("count", text="Count")


        # Set column sizes and text alignment
        self.level_tree.column("level", width=220, anchor="w")
        self.level_tree.column("count", width=80, anchor="center")



#Create scrollbar for level table
        level_scroll = ttk.Scrollbar(right, orient="vertical", command=self.level_tree.yview)
        self.level_tree.configure(yscrollcommand=level_scroll.set)

        self.level_tree.pack(side="left", fill="both", expand=True)
        level_scroll.pack(side="right", fill="y")

        # Fixed bottom bar (always visible)
        bottom = tk.Frame(self)
        bottom.grid(row=1, column=0, sticky="ew", padx=14, pady=(0, 12))



        # Create buttons in bottom bar
        tk.Button(bottom, text="Refresh", width=12, command=self.refresh).pack(side="left")
        tk.Button(bottom, text="Back", width=12, command=lambda: self.app.show("MainMenu")).pack(side="right")

    def on_show(self) -> None:
        self.refresh()



# Show total questions in database
    def refresh(self) -> None:
        total = total_questions()
        self.total_lbl.config(text=f"Total questions in DB: {total}")



# Populate statistics tables
        for item in self.cat_tree.get_children():
            self.cat_tree.delete(item)
        for item in self.level_tree.get_children():
            self.level_tree.delete(item)

        for category, cnt in stats_questions_by_category():
            self.cat_tree.insert("", "end", values=(category, cnt))

        for level, cnt in stats_questions_by_level():
            self.level_tree.insert("", "end", values=(level, cnt))
