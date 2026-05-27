# Week 7 Assignment: Leaderboard and Record-Saving System

## Project Overview
This week, I added a persistent record-saving system and a leaderboard to the text-based Assassin's Creed game. The game now tracks how much time a player needs to complete the assassination mission. This data is saved externally so that players can compete for the fastest time across different game sessions.

## New Core Features

### 1. The Timer and Scoring System
Instead of a traditional point score, this game uses "time spent in seconds" as the score. When the game loop begins, Python notes the exact start time using the `time` module. Once the player successfully executes the `assassinate` command with the correct equipment, the game captures the end time, calculates the total duration, and pairs it with the player's custom assassin name.

### 2. CSV File Management
To store player records permanently, the game automatically reads and writes to an external file named `assassin_records.csv`. I chose the CSV format because it allows structured data to be saved row-by-row like a spreadsheet. When a game ends, the program loads the existing rows, appends the new player data, and sorts the entire list so that the fastest times always appear at the top of the leaderboard.

### 3. Exception Handling (Try/Except)
To make the application robust and prevent crashes, I implemented defensive programming with `try/except` blocks. If the CSV file does not exist yet during a player's very first run, the program catches the `FileNotFoundError` and smoothly handles it by creating a brand-new file. Additional blocks safeguard the game against data conversion errors (`ValueError`) and file permission issues (`PermissionError`).

### 4. Debug Mode Configuration
As requested in the assignment instructions, a global variable called `DEBUG` is placed at the top of the script and set to `True`. When active, this flag alters the game flow by completely skipping the core text adventure loop. The tester only needs to input a name, and the program automatically generates a random placeholder time to immediately test the file-writing logic, sorting mechanism, and leaderboard visualization.

## Why I Designed the Code This Way
Following the concepts taught in class, I used the `with open(...)` context manager to ensure that files are safely and automatically closed after operations, which prevents data loss. I used formatted f-strings like `{:15s}` to align the text columns, ensuring the terminal leaderboard looks clean and readable. Finally, separating the record-saving logic into its own independent function keeps the code modular and clean.
