import time

# step 1: the data collection
inventory = []
INVENTORY_LIMIT = 5

items_in_room = [
    {"name": "coin_pouch",   "type": "tool",   "uses": 1, "description": "A pouch of coins. Useful for bribing guards."},
    {"name": "disguise",     "type": "tool",   "uses": 1, "description": "A noble's outfit. Lets you blend in at the palace."},
    {"name": "poison_vial",  "type": "weapon", "uses": 1, "description": "A vial of poison. Can be slipped into a drink."},
    {"name": "hidden_blade", "type": "weapon", "uses": 1, "description": "The assassin's weapon. Silent and deadly."},
    {"name": "smoke_bomb",   "type": "tool",   "uses": 1, "description": "Creates a diversion to slip past guards."}
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

Find the right items and type
'assassinate' when you are ready.

Type 'help' to see all commands.
====================================
    """)
    show_room_items()

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
