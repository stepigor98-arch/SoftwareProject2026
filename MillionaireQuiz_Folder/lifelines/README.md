# Lifelines Module

## Purpose

This module contains the business logic for quiz lifelines in the Millionaire Quiz project.

The first implemented lifeline is the 50/50 lifeline. It removes two wrong answer options and keeps the correct answer visible for the player.

## Selected Design Pattern

The selected design pattern is the Strategy Pattern.

## Why Strategy Pattern Was Selected

The Strategy Pattern is a good fit for this feature because the quiz can have different types of lifelines.

For example:

- 50/50 Lifeline
- Second Chance Lifeline
- Ask the Audience Lifeline
- Phone a Friend Lifeline

Each lifeline has its own logic, but all of them have the same general purpose: to help the player during the game.

Using the Strategy Pattern makes it possible to add new lifelines later without rewriting the main quiz logic.

## How the Module Works

The module contains a base strategy class called `LifelineStrategy`.

The `FiftyFiftyStrategy` class implements the logic for the 50/50 lifeline.

The `LifelineContext` class receives a selected strategy and uses it when the player activates a lifeline.

## Interaction With Other Components

This module does not directly interact with the graphical interface or the database.

The main quiz system can call this module when the player presses the 50/50 button.

The module returns the result as data. Then the GUI can use this result to update the visible answer options.

## Why This Helps the Project

This structure makes the code more modular and easier to maintain.

The business logic is separated from the Tkinter interface and SQLite database.

This also helps AI assistants generate safer code, because the module has a clear structure and strict responsibility.

## Module Structure

```text
lifelines
├── __init__.py
├── strategies.py
└── README.md
