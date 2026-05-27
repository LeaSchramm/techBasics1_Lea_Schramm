import time
import csv
import os
import random
from datetime import datetime

# ==========================================
# REQ_7: DEBUG FLAG & SETTINGS (Aus der Aufgabe)
# ==========================================
DEBUG = False  # Auf False setzen, um das echte Spiel zu spielen!
RECORD_FILE = "assassin_records.csv"

# step 1: the data collection
inventory = []
INVENTORY_LIMIT = 5

items_in_room = [
    {"name": "coin_pouch", "type": "tool", "uses": 1, "description": "A pouch of coins. Useful for bribing guards."},
    {"name": "disguise", "type": "tool", "uses": 1,
     "description": "A noble's outfit. Lets you blend in at the palace."},
    {"name": "poison_vial", "type": "weapon", "uses": 1,
     "description": "A vial of poison. Can be slipped into a drink."},
    {"name": "hidden_blade", "type": "weapon", "uses": 1, "description": "The assassin's weapon. Silent and deadly."},
    {"name": "smoke_bomb", "type": "tool", "uses": 1, "description": "Creates a diversion to slip past guards."}
]


# step 2: the 6 functions
def show_inventory():
    print("\n--- YOUR INVENTORY ---")
    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        for item in inventory:
            print(f"- {item['name']} ({item['type']}) | uses left: {item['uses']}")
    print(f"Slots: {len(inventory)}/{INVENTORY_LIMIT}")
    print("----------------------")


def show_room_items():
    print("\n--- ITEMS IN THE AREA ---")
    if len(items_in_room) == 0:
        print("Nothing here.")
    else:
        for item in items_in_room:
            print(f"  - {item['name']} ({item['type']})")
    print("-------------------------")


def pick_up(item_name):
    if len(inventory) >= INVENTORY_LIMIT:
        print("Inventory full! Drop something first.")
        return
    for item in items_in_room:
        if item["name"] == item_name:
            inventory.append(item)
            items_in_room.remove(item)
            print(f"Picked up: {item_name}")
            return
    print(f"No '{item_name}' here.")


def drop(item_name):
    for item in inventory:
        if item["name"] == item_name:
            items_in_room.append(item)
            inventory.remove(item)
            print(f"Dropped: {item_name}")
            return
    print(f"You don't have '{item_name}'.")


def examine(item_name):
    for item in inventory + items_in_room:
        if item["name"] == item_name:
            print(f"\n--- {item['name'].upper()} ---")
            print(f"Type: {item['type']}")
            print(f"Uses left: {item['uses']}")
            print(f"Description: {item['description']}")
            return
    print(f"No '{item_name}' found.")


def use(item_name):
    for item in inventory:
        if item["name"] == item_name:
            if item["uses"] <= 0:
                print(f"The {item_name} has no uses left!")
                return
            item["uses"] -= 1
            print(f"You use the {item_name}...")
            if item_name == "coin_pouch":
                print("You bribe a guard. He looks the other way.")
            elif item_name == "disguise":
                print("You put on the noble outfit.")
            elif item_name == "poison_vial":
                print("You slip the poison into a drink.")
            elif item_name == "smoke_bomb":
                print("You throw the smoke bomb. Guards are confused!")
            elif item_name == "hidden_blade":
                print("The blade clicks into place.")
            if item["uses"] == 0:
                inventory.remove(item)
                print(f"The {item_name} has been used up.")
            return
    print(f"You don't have '{item_name}'.")


def check_assassination():
    inventory_names = [item["name"] for item in inventory]
    required = ["hidden_blade", "disguise"]
    missing = [i for i in required if i not in inventory_names]

    if not missing:
        print("""
====================================
        MISSION ACCOMPLISHED
====================================
You blend in with your disguise and
strike Barbarigo with the hidden
blade. Florence is free.

  "Nothing is true, everything is
         permitted."
====================================
        """)
        return True
    else:
        print(f"""
====================================
          MISSION FAILED
====================================
You are not prepared. The guards
spot you immediately.
Missing: {", ".join(missing)}
====================================
        """)
        return False


# ========================================================
# NEW FOR WEEK 7: SYSTEM BASED ON YOUR NOTEBOOK LESSONS
# ========================================================

def save_and_display_records(player_name, time_used):
    """Saves the current run into a CSV and prints a sorted leaderboard using try/except."""
    current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_record = [player_name, current_timestamp, f"{time_used:.1f}"]

    all_records = []

    # --- 1. DATEN LADEN (Basierend auf Notebook Kapitel: Exceptions Handling) ---
    try:
        with open(RECORD_FILE, mode="r", newline="", encoding="utf-8") as file:
            # Nutzen des csv-Moduls, wie in deiner Übung gezeigt
            csvreader = csv.reader(file)
            for row in csvreader:
                all_records.append(row)
    except FileNotFoundError:
        # Dieser spezifische Error wurde in deinem Notebook als Beispiel genannt!
        print(f"\n[System] '{RECORD_FILE}' not found. A new file will be created.")
    except Exception as e:
        print(f"\n[System] An unexpected error occurred while reading: {e}")

    # Aktuellen Lauf zur Liste hinzufügen
    all_records.append(new_record)

    # --- 2. DATEN SPEICHERN (Basierend auf Notebook Kapitel: csv.writer) ---
    try:
        with open(RECORD_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            # Nutzt writerows(), wie ganz unten im Notebook erklärt
            writer.writerows(all_records)
        print("[System] Record saved successfully to CSV!")
    except PermissionError:
        print("\n❌ Error: Lacking permissions to write to the file.")
        return
    except Exception as e:
        print(f"\n❌ Error: Could not save the data. Reason: {e}")
        return

    # --- 3. LEADERBOARD ZEIGEN (Basierend auf Notebook Kapitel: F-String Formatting) ---
    print("\n====================================")
    print("            LEADERBOARD             ")
    print("====================================")
    # Nutzen von linksbündiger Ausrichtung (<), ähnlich wie im Früchte-Beispiel des Notebooks
    print(f"{'Rank':<5} {'Name':<15} {'Timestamp':<18} {'Time Used':<10}")
    print("-" * 52)

    try:
        # Sortiert die Liste nach Zeit (Index 2). Schnellste Zeit (kleinste Zahl) nach oben.
        all_records.sort(key=lambda x: float(x[2]))

        for index, record in enumerate(all_records, start=1):
            print(f"{index:<5} {record[0]:<15} {record[1]:<18} {record[2]}s")
    except (ValueError, IndexError):
        print("❌ Error: The record data could not be parsed or sorted properly.")

    print("====================================\n")


# step 3 win oder lose the game
def show_help():
    print("""
--- COMMANDS ---
inventory           -> show inventory
look                -> show items in area
pickup [item]       -> pick up an item
drop [item]         -> drop an item
use [item]          -> use an item
examine [item]      -> examine an item
assassinate         -> attempt the assassination
help                -> show commands
quit                -> quit game
----------------
    """)


def game_loop():
    print("""
====================================
   ASSASSIN'S CREED: FLORENCE 1486
====================================
Target: Marco Barbarigo
A corrupt nobleman. Eliminate him.
""")

    # Namen abfragen für die Bestenliste
    player_name = input("Enter your Assassin Name: ").strip()
    if not player_name:
        player_name = "Unknown Assassin"

    # ==========================================
    # REQ_7: DEBUG-MODE LOGIK
    # ==========================================
    if DEBUG:
        print("\n[DEBUG MODE ACTIVE] Skipping main game loop...")
        placeholder_time = random.uniform(8.5, 38.0)  # Simuliert eine benötigte Zeit in Sekunden
        print(f"Saving a placeholder time of {placeholder_time:.1f} seconds for test purposes.")
        save_and_display_records(player_name, placeholder_time)
        return  # Beendet die Funktion und lässt das Spiel aus

    # --- REGULÄRES SPIEL (Wenn DEBUG = False) ---
    print("\nFind the right items and type 'assassinate' when you are ready.")
    print("Type 'help' to see all commands.")
    print("====================================")

    show_room_items()
    start_time = time.time()  # Hier starten wir die Zeitmessung (Woche 7)

    while True:
        user_input = input("\n> ").strip().lower()
        parts = user_input.split(" ", 1)
        command = parts[0]
        target = parts[1] if len(parts) > 1 else ""

        if command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command == "pickup":
            pick_up(target)
        elif command == "drop":
            drop(target)
        elif command == "use":
            use(target)
        elif command == "examine":
            examine(target)
        elif command == "assassinate":
            result = check_assassination()
            if result:
                # Zeit stoppen und ausrechnen
                end_time = time.time()
                time_used = end_time - start_time
                print(f"You finished the mission in {time_used:.1f} seconds.")
                # Rekordsystem aufrufen
                save_and_display_records(player_name, time_used)
                break
        elif command == "help":
            show_help()
        elif command == "quit":
            print("You abandon the mission. For now...")
            break
        else:
            print(f"Unknown command: '{command}'. Type 'help'.")


if __name__ == "__main__":
    game_loop()
