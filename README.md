# Tic-Tac-Toe-game
This is a command-line implementation of the classic Tic-Tac-Toe game built in Python. The game allows two players to compete on a 3x3 board and supports score tracking between games. This project demonstrates core concepts in Python, including OOP (Object-Oriented Programming), user input handling, and basic game logic.


Key Features:
Interactive Gameplay: Two players can take turns selecting cells to mark with 'X' or 'O'.
Dynamic Board Display: The game board updates in real time after each move, showing the current game state.
Win & Draw Detection: Automatically detects when a player wins by completing a row, column, or diagonal, or when the game ends in a draw.
Score Tracking: Tracks scores for each player across multiple games.
Clear Console Display: Refreshes the screen to show only the latest game state for a clean interface.
Input Validation: Ensures players enter valid move choices and prevents overwriting of previously marked cells.


How to Use:
Register Players: Enter names for both players at the start.
Choose Moves: Players choose a cell by entering a number from 1 to 9, corresponding to cells on the board.
Win, Lose, or Draw: The game displays the updated board after each move, checking for wins or draws.
View Score: Players can view current scores between games.
Exit: Option to exit the game at any time.
Requirements:
Python 3.x
pyfiglet and termcolor libraries for ASCII art and colored text (install with pip install pyfiglet termcolor)
