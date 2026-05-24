# Week 6 Assignment: Inventory Management Game

## PROJECT OVERVIEW
This project is a text-based adventure game inspired by Assassin's Creed. The player is an assassin in Florence in the year 1486. The main objective of the game is to find the correct items in the area, manage the inventory space, and successfully eliminate the target, Marco Barbarigo, like in the original game.

## HOW THE CODE WORKS
The game is built using modular functions and clear data collections to handle player actions smoothly. At the start of the script, the game sets up the inventory as an empty list and defines the room items using a list of dictionaries. Each dictionary contains specific information about an item, including its name, type, number of uses, and a brief description.

Player actions are split into six specific functions that manage how items move and change state. The show functions print what is currently inside the inventory or lying on the ground. The pickup and drop functions safely transfer the item dictionaries between the room list and the inventory list while checking that the inventory does not exceed the maximum limit of five items. The examine function searches both lists to print the item details, and the use function reduces the available uses of an item before removing it if it is empty.

The main game loop runs continuously to handle player commands. It captures the text input from the player and splits it into two parts so that commands like pickup disguise can be read correctly. All text inputs are automatically converted to lowercase to prevent typos from breaking the logic. Finally, when the player types the assassinate command, a validation function checks if the player holds the required tools in their inventory list, which determines if the game triggers a victory or a failure ending.

## WHY I DESIGNED THE CODE THIS WAY

I chose this specific structure to keep the code highly organized, easy to test, and safe from unexpected crashes. Using a list of dictionaries for the items allows the game to store multiple pieces of information about a single object in a neat package. Separating the game into individual functions means that each action has only one job, which makes it simple to find and fix bugs if something goes wrong. Using global constants for settings like the inventory limit ensures that game rules are set in one place and can be adjusted instantly without changing lines of code inside the loops.
