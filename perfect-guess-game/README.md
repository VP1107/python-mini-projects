# Perfect Guess Game

A fun and interactive number guessing game suitable for one or two players. Test your intuition and logic by guessing a randomly generated number between 0 and 100!

## Description

The "Perfect Guess Game" challenges players to guess a secret number chosen by the computer. It provides feedback ("Higher" or "Lower") for each guess until the correct number is found. The game tracks the number of attempts it takes to guess correctly.

## Features

*   **One Player Mode:** Play against the computer to find the secret number in the fewest guesses possible.
*   **Two Player Mode:** Challenge a friend! Player A competes against Player B to see who can guess their respective secret numbers in fewer attempts.
*   **Feedback System:** The game hints whether you need to guess higher or lower after each attempt.
*   **Win/Draw Logic:** In two-player mode, the game compares the number of guesses to declare a winner or a draw.

## Prerequisites

*   Python 3.x installed on your system.
*   Basic understanding of running Python scripts in a terminal.

## How to Play

1.  **Start the Game:** Run the script.
2.  **Select Mode:**
    *   Type `One` for single-player mode.
    *   Type `Two` for two-player mode.
    *   Type `Q` to quit.
3.  **Gameplay:**
    *   Enter a number between 0 and 100.
    *   Follow the "Higher" or "Lower" hints.
    *   Keep guessing until you find the "Perfect" number!
4.  **Two Player:**
    *   First, Player A plays and their score (attempts) is recorded.
    *   Then, Player B plays a separate round.
    *   Finally, the scores are compared to announce the winner.

## How to Run

1.  Navigate to the project directory:
    ```bash
    cd perfect-guess-game
    ```

2.  Run the game:
    ```bash
    python main.py
    ```
