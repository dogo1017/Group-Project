#Should end up here after a character has been selected and they wanna make/edit a certain inventory

saved_inventorys = {}

from menu import menu


def add_items(items, characters, selected_character):
    # Find the character object
    current_character = None
    for char in characters:
        if char["name"] == selected_character:
            current_character = char
            break
    
    if current_character is None:
        print("Character not found!")
        input("Press Enter to continue...")
        return

    if "inventory" not in current_character:
        current_character["inventory"] = []

    # Print available items from the items list passed from main
    print(f"\nAvailable items:\n")
    if len(items) == 0:
        print("No items available.")
        input("Press Enter to continue...")
        return
    
    # Create menu options from items
    item_names = [item["name"] for item in items]
    item_names.append("Return")
    
    result = menu(item_names)
    selected = result['index']
    
    if selected >= len(items):
        return
    
    selected_item = items[selected]
    current_character["inventory"].append(selected_item)
    print(f"{selected_item['name']} added to inventory.")
    input("Press Enter to continue...")


def remove_items(characters, selected_character):
    # Find the character object
    current_character = None
    for char in characters:
        if char["name"] == selected_character:
            current_character = char
            break
    
    if current_character is None:
        print("Character not found!")
        input("Press Enter to continue...")
        return

    if "inventory" not in current_character or len(current_character["inventory"]) == 0:
        print("No inventory to remove.")
        input("Press Enter to continue...")
        return

    item_names = [item["name"] for item in current_character["inventory"]]
    item_names.append("Return")
    
    result = menu(item_names)
    selected = result['index']
    
    if selected < len(current_character["inventory"]):
        removed = current_character["inventory"].pop(selected)
        print(f"Removed {removed['name']}")
        input("Press Enter to continue...")


def view_inventory(characters, selected_character):
    # View all inventory items for the character
    # Find the character object
    current_character = None
    for char in characters:
        if char["name"] == selected_character:
            current_character = char
            break
    
    if current_character is None:
        print("Character not found!")
        input("Press Enter to continue...")
        return
    
    print(f"\n{current_character['name']}'s Inventory:")
    if "inventory" in current_character and current_character["inventory"]:
        total_weight = 0
        total_value = 0
        for item in current_character["inventory"]:
            print(f"\n  {item['name']}")
            for key, value in item.items():
                if key != "name":
                    print(f"    {key}: {value}")
            # Track totals
            if "weight" in item:
                total_weight += item["weight"]
            if "value" in item:
                total_value += item["value"]
        print(f"\n  Total Weight: {total_weight} lbs")
        print(f"  Total Value: {total_value} gold")
    else:
        print("  No items yet!")
    input("\nPress Enter to continue...")


def inventory_menu(items, characters, selected_character):
    options = ["Add items", "Remove items", "View Inventory", "Return to Menu"]
    while True:
        choice = menu(options)
        if choice.get('index') == 0:
            add_items(items, characters, selected_character)
        elif choice.get('index') == 1:
            remove_items(characters, selected_character)
        elif choice.get('index') == 2:
            view_inventory(characters, selected_character)
        elif choice.get('index') == 3:
            return characters, selected_character