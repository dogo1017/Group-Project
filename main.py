# Main run file. Holds the user interface
import os
import msvcrt
import add_character
import attribute_manager
import inventory_manager
import search
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
    options = ["Add Character", "Manage Skills", "Manage Inventory", "Manage Attributes", "Search for Character"]
    characters = []
    #add_character.add_menu
    while True:
        choice = menu(options)
        if choice == 0:
            add_character.add_menu()
        elif choice == 1:
            if selected_character == "":
                skill_manager.skill_menu()
            else:
                print("Please select a character before entering this function.")
                input("Press Enter to continue...")
                continue
        elif choice == 2:
            if selected_character != "":
                inventory_manager.inventory_menu()
            else:
                print("Please select a character before entering this function.")
                input("Press Enter to continue...")
                continue
        elif choice == 3:
            if selected_character != "":
                attribute_manager.attribute_menu()
            else:
                print("Please select a character before entering this function.")
                input("Press Enter to continue...")
                continue
        else:
            selected_character = search.search_menu(characters, selected_character, comp=False)

main()