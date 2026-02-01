# Main run file. Holds the user interface
import add_character
import attribute_manager
import inventory_manager
import selecter
import skill_manager
import view
from menu import menu    
import text
import os

def main():
    text.bubble("Welcome to our program! This is our RPG Character Manager. Use up/down arrow keys to change options, left and right to change values, and options with ':' are writable (If you need more help click on the help option to tell you what everything does)", speed= 0.025)
    selected_character = "example character 1 (default)"
    options = ["Add Character", "Manage Skills", "Manage Inventory", "Manage Attributes", "View / Compare Characters", "Select / Search Characters", "Help"]
    classes = [{"name": "rogue", "dmg": 1.2, "dex": 1.5, "int": 1.1, "con": 0.9, "cha": 1.2}, {"name": "warrior", "dmg": 1.5, "dex": 0.9, "int": 0.8, "con": 1.4, "cha": 1.0}, {"name": "mage", "dmg": 1.3, "dex": 0.8, "int": 1.6, "con": 0.7, "cha": 1.1}, {"name": "paladin", "dmg": 1.2, "dex": 0.9, "int": 1.0, "con": 1.3, "cha": 1.4 }, {"name": "ranger", "dmg": 1.3, "dex": 1.4, "int": 1.0, "con": 1.0, "cha": 1.0 }, {"name": "bard", "dmg": 0.9, "dex": 1.1, "int": 1.2, "con": 0.9, "cha": 1.6}, {"name": "tank", "dmg": 0.9, "dex": 0.7, "int": 0.8, "con": 1.7, "cha": 0.9}]
    races = [{"name": "Human", "dmg": 1.0, "dex": 1.0, "int": 1.0, "con": 1.0, "cha": 1.0}, {"name": "Elf", "dmg": 0.9, "dex": 1.2, "int": 1.1, "con": 0.9, "cha": 1.1}, {"name": "Ork", "dmg": 1.3, "dex": 0.8, "int": 0.7, "con": 1.2, "cha": 0.8}, {"name": "Dwarf", "dmg": 1.1, "dex": 0.8, "int": 0.9, "con": 1.3, "cha": 0.9}, {"name": "Halfling", "dmg": 0.8, "dex": 1.3, "int": 1.0, "con": 0.9, "cha": 1.2}]
    items = [{"name": "Iron Sword", "dmg": 1.2}, {"name": "Dagger", "dex": 1.3}, {"name": "Wizard Staff", "int": 1.4}, {"name": "Heavy Armor", "con": 1.5}, {"name": "Silver Amulet", "cha": 1.3}]
    characters = ({
        "name": "example character 1 (default)", 
        "class": "rogue", 
        "level": 1, 
        "race": "Human", 
        "attributes": [], 
        "base_attributes": [5, 5, 5, 5, 5],
        "skills": {}, 
        "inventory": []},
     {
        "name": "example character 2", 
        "class": "warrior", 
        "level": 10, 
        "race": "Ork", 
        "attributes": [], 
        "base_attributes": [8, 4, 3, 7, 4],
        "skills": {"Fireball"}, 
        "inventory": ["Iron Sword", "Heavy Armor"]},
    {
        "name": "example character 3", 
        "class": "mage", 
        "level": 20, 
        "race": "Human", 
        "attributes": [], 
        "base_attributes": [3, 5, 9, 4, 6],
        "skills": {"Heal", "Shield"}, 
        "inventory": ["Wizard Staff", "Silver Amulet"]}
    )
    saved_skills = {
        "Fireball": {"description": "Shoots a fireball", "effect": "Attack", "amount": 50, "target": "Enemy"},
        "Heal": {"description": "Restores health", "effect": "Health", "amount": 30, "target": "Self"},
        "Shield": {"description": "Increases defense", "effect": "Defense", "amount": 20, "target": "Self"}
    }
    while True:
        choice = menu(options)
        characters = list(characters)
        if choice.get('index') == 0:
            characters = add_character.add_menu(characters, classes, races, items)
        elif choice.get('index') == 1:
            if selected_character != "":
                characters, selected_character = skill_manager.skill_menu(saved_skills, characters, selected_character)
            else:
                print("Please select a character before entering this function.")
                input("Press Enter to continue...")
                continue  
        elif choice.get('index') == 2:
            if selected_character != "":
                characters, selected_character = inventory_manager.inventory_menu(items, characters, selected_character)
            else:
                print("Please select a character before entering this function.")
                input("Press Enter to continue...")
                continue
        elif choice.get('index') == 3:
            if selected_character != "":
                characters, selected_character = attribute_manager.attribute_menu(characters, selected_character)
            else:
                print("Please select a character before entering this function.")
                input("Press Enter to continue...")
                continue
        elif choice.get('index') == 4:
            if selected_character != "":
                characters, selected_character = view.view_menu(characters, selected_character, classes, races, items)
            else:
                print("Please select a character before entering this function.")
                input("Press Enter to continue...")
                continue
        elif choice.get('index') == 5:
            characters, selected_character = selecter.selecter_menu(characters, selected_character)
        elif choice.get('index') == 6:
            os.system('cls')
            # General Navigation
            text.bubble("Welcome to the Help Menu! Use the up and down arrow keys to navigate through menu options. Press Enter to select an option. For writable fields (marked with ':'), you can type directly. For number fields (shown with <>), use left and right arrows to adjust values. For toggle fields, use left and right arrows to cycle through options.", speed=0.01)
            os.system('cls')
            # Add Character
            text.bubble("Add Character: This function lets you create a new character for your RPG. You'll set your character's name, choose their class and race, and set their starting level. You can also assign initial attribute points like damage, dexterity, intelligence, constitution, and charisma. Additionally, you can select starting skills and inventory items. Don't worry - all of these choices can be changed later through other menu options!", speed=0.01)
            os.system('cls')
            # Manage Skills
            text.bubble("Manage Skills: This is where you control your character's abilities and powers. You can add new skills from a saved library, create completely custom skills with unique effects, or edit existing skills your character already knows. Each skill has a name, description, effect type (Attack, Defense, or Health), strength amount, and target (Enemy, Self, or Ally). You can also view all your character's current skills and remove any you no longer want.", speed=0.01)
            os.system('cls')
            # Manage Inventory
            text.bubble("Manage Inventory: Use this menu to equip your character with powerful items! You can add items from the available item list to your character's inventory, remove items you no longer need, or view all the items your character is currently carrying. Each item provides stat bonuses like increased damage, dexterity, intelligence, constitution, or charisma. Build the perfect loadout for your character's playstyle!", speed=0.01)
            os.system('cls')
            # Manage Attributes
            text.bubble("Manage Attributes: This function allows you to modify your character's core stat values. You can change your character's strength as they progress and grow stronger, change your character's constitution for a more beefy build, and other values. You can also view a complete summary of all your character's attributes one convenient display.", speed=0.01)
            os.system('cls')
            # Compare Characters
            text.bubble("View / Compare Characters: This feature lets you compare two characters side by side or just one. You can select your currently active character and view it or use it and another character from your roster to compare. You'll be able to see their stats, skills, and equipment to help you decide which character is better suited for different situations.", speed=0.01)
            os.system('cls')
            # Search Characters
            text.bubble("Select / Search Characters: This function lets you search for a character to select and change for all the rest of the functions.", speed=0.01)
            os.system('cls')

        def make_lookup(data_list):
            """Closure that caches a name->entry dict for fast lookups."""
            index = {entry["name"]: entry for entry in data_list}

            def find(name):
                return index.get(name)

            return find
        
        def make_attribute_applier():
            """Closure that binds the attribute key order and applies multipliers from any source."""
            keys = ["dmg", "dex", "int", "con", "cha"]

            def apply(attributes, source):
                if source:
                    for i, key in enumerate(keys):
                        if key in source:
                            attributes[i] *= source[key]

            return apply
        
        find_race = make_lookup(races)
        find_class = make_lookup(classes)
        find_item = make_lookup(items)
        apply_multipliers = make_attribute_applier()

        for character in characters:
            character["attributes"] = character["base_attributes"].copy()

            race_data = find_race(character["race"])
            class_data = find_class(character["class"])

            for item_name in character["inventory"]:
                apply_multipliers(character["attributes"], find_item(item_name))

            apply_multipliers(character["attributes"], race_data)
            apply_multipliers(character["attributes"], class_data)
        characters = tuple(characters)
main()