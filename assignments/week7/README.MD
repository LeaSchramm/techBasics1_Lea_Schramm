# Week 7 Assignment: Leaderboard and Record-Saving System in the assassins creed game

## Project Overview
With this assginment, I added a leaderboard and a save system to the Assassin's Creed game. The game now tracks how many seconds a player takes to complete the mission and saves this data to an external file.

## New Features and How They Work

### 1. The Timer and Score
The game uses "time used in seconds" as the final score. The program records the exact time when the game starts. When the player successfully completes the mission, the program stops the timer, calculates the total seconds, and links it to the player's name.

### 2. CSV File Saving
All player records are saved in a file called `assassin_records.csv`. When a game ends, the program opens this file, adds the new player's name, timestamp, and time, and then sorts the list. The fastest times (lowest seconds) are automatically placed at the top of the leaderboard.

### 3. Error Handling (Try/Except)
I added `try/except` blocks to prevent the game from crashing. For example, if the game is played for the very first time, the CSV file does not exist yet. The code catches this `FileNotFoundError` and automatically creates a new file instead of closing with an error.

### 4. Debug Mode
There is a `DEBUG = True` flag at the top of the code. When it is set to `True`, the program skips the main game loop entirely. The tester only needs to type their name, and the game automatically creates a random placeholder time to instantly show how the saving system and leaderboard work.

## Code Design Choices
I used the `with open(...)` statement because it automatically closes the file after reading or writing, which keeps the data safe. I also used formatted f-strings (like `{:15s}`) to align the text columns so the leaderboard prints as a clean, easy-to-read table in the terminal.
