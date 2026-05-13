# Feature: 50/50 Lifeline

## User Story

As a player, I want to use a 50/50 lifeline during the quiz, so that two wrong answer options are removed and I have a better chance to choose the correct answer.

## Acceptance Criteria

### AC1: Remove two wrong answers

Given the current question has four answer options and one correct answer  
When the player uses the 50/50 lifeline  
Then two incorrect answer options are removed and the correct answer remains visible

### AC2: Lifeline can be used only once

Given the player has not used the 50/50 lifeline yet  
When the player activates the 50/50 lifeline  
Then the lifeline becomes unavailable for the rest of the game

### AC3: Correct answer is never removed

Given the current question has one correct answer and three wrong answer options  
When the 50/50 lifeline is applied  
Then the correct answer must stay in the returned answer options

## Notes

This feature is part of the Millionaire Quiz MVP improvements.  
The logic should be implemented separately from the graphical interface and database.  
For the AI experiment, this feature should be written as a pure function with predictable output.
