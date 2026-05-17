# DESIGN.md

## Project

Millionaire Quiz

## Purpose

This document defines the visual design contract for the Millionaire Quiz user interface.

The goal is to use Spec-Driven Development to guide AI-generated frontend code and avoid generic, inconsistent, or inaccessible UI.

## Framework Choice

The selected UI framework is Streamlit.

Streamlit was selected because the project is written in Python and the backend business logic is already implemented as a Python module.

The UI should connect directly to the existing lifelines module:

```text
MillionaireQuiz_Folder/lifelines/strategies.py
