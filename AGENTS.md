# AGENTS.md

## Project Overview

This project is a Software Engineering course project. The goal is to create a software product with a clear structure, documentation, and future development plan.

The project should be developed as a hybrid workflow between a human developer and AI assistants. The AI should help with simple coding tasks, documentation, testing, and refactoring, but the final decisions must stay with the human developer.

## Main Rules for AI Agents

- Always read the `/docs` folder before making changes.
- Keep the project structure simple and understandable.
- Do not create unnecessary files or folders.
- Do not change the main architecture without human approval.
- Write clean and readable code.
- Use simple naming for files, variables, and functions.
- Prefer small and safe changes instead of large rewrites.
- If something is unclear, check the documentation first.

## Coding Rules

- Use the programming language and tools already used in the project.
- Follow the existing style of the codebase.
- Keep comments short and useful.
- Do not remove existing functionality unless it is clearly required.
- Test important changes before suggesting them.

## Documentation Rules

- README.md is for humans.
- AGENTS.md is for AI assistants.
- Detailed project context must be stored inside `/docs`.
- Project plans should be stored inside `/docs/plans`.

## AI Responsibilities

AI assistants may help with:

- boilerplate code;
- simple functions;
- unit tests;
- documentation drafts;
- small refactoring;
- checking code consistency.

AI assistants must not:

- redesign the whole project without approval;
- delete important files;
- invent requirements that are not documented;
- ignore the roadmap and project documentation.
