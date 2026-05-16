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

## Module Structure

```text
lifelines
├── __init__.py
├── strategies.py
└── README.md
