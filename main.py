# Main run file. Holds the user interface
import os
import msvcrt
import add_character
import attribute_manager
import inventory_manager
import search_compare
import skill_manager

def menu(options):
    index = 0
    while True:
        os.system('cls')
        for i, option in enumerate(options):
            prefix = "> " if i == index else "  "
            print(prefix + option)
        key = msvcrt.getch()
        if key in (b'\x00', b'\xe0'):
            key = msvcrt.getch()
        if key == b"H":
            index = (index - 1) % len(options)
        elif key == b"P":
            index = (index + 1) % len(options)
        elif key == b"\r":
            return index        

def main():
    selected_character = ""
    options = ["Add Character", "Manage Skills", "Manage Inventory", "Manage Attributes", "Compare Characters", "Search Characters"]
    classes = [{"name": "rogue", "dmg": 1.2, "dex": 1.5, "int": 1.1, "con": 0.9, "cha": 1.2}, {"name": "warrior", "dmg": 1.5, "dex": 0.9, "int": 0.8, "con": 1.4, "cha": 1.0}, {"name": "mage", "dmg": 1.3, "dex": 0.8, "int": 1.6, "con": 0.7, "cha": 1.1}, {"name": "paladin", "dmg": 1.2, "dex": 0.9, "int": 1.0, "con": 1.3, "cha": 1.4 }, {"name": "ranger", "dmg": 1.3, "dex": 1.4, "int": 1.0, "con": 1.0, "cha": 1.0 }, {"name": "bard", "dmg": 0.9, "dex": 1.1, "int": 1.2, "con": 0.9, "cha": 1.6}, {"name": "tank", "dmg": 0.9, "dex": 0.7, "int": 0.8, "con": 1.7, "cha": 0.9}]
    races = []
    items = []
    characters = [{"test character yipee", "rogue", 15, "autism creature", [], {}, [], {}}, {"", "", "", "", [], {}, []}]
    # INDEXES 0: name, 1: class, 2: level, 3: race, 4: attributes, 5: skills, 6: inventory, 7: stats

    #add_character.add_menu
    while True:
        choice = menu(options)
        if choice == 0:
            characters = add_character.add_menu(characters)
        elif choice == 1:
            if selected_character == "":
                characters, selected_character = skill_manager.skill_menu(characters, selected_character)
            else:
                print("Please select a character before entering this function.")
                input("Press Enter to continue...")
                continue  
        elif choice == 2:
            if selected_character != "":
                characters, selected_character = inventory_manager.inventory_menu(characters, selected_character)
            else:
                print("Please select a character before entering this function.")
                input("Press Enter to continue...")
                continue
        elif choice == 3:
            if selected_character != "":
                characters, selected_character = attribute_manager.attribute_menu(characters, selected_character)
            else:
                print("Please select a character before entering this function.")
                input("Press Enter to continue...")
                continue
        elif choice == 4:
            if selected_character != "":
                characters, selected_character = search_compare.search_menu(characters, selected_character, comp=True)
            else:
                print("Please select a character before entering this function.")
                input("Press Enter to continue...")
                continue
        else:
            characters, selected_character = search_compare.search_menu(characters, selected_character, comp=False)

main()