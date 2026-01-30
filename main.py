# Main run file. Holds the user interface
import add_character
import attribute_manager
import inventory_manager
import search_compare
import skill_manager
from menu import menu    

def main():
    selected_character = ""
    options = ["Add Character", "Manage Skills", "Manage Inventory", "Manage Attributes", "Compare Characters", "Search Characters"]
    classes = [{"name": "rogue", "dmg": 1.2, "dex": 1.5, "int": 1.1, "con": 0.9, "cha": 1.2}, {"name": "warrior", "dmg": 1.5, "dex": 0.9, "int": 0.8, "con": 1.4, "cha": 1.0}, {"name": "mage", "dmg": 1.3, "dex": 0.8, "int": 1.6, "con": 0.7, "cha": 1.1}, {"name": "paladin", "dmg": 1.2, "dex": 0.9, "int": 1.0, "con": 1.3, "cha": 1.4 }, {"name": "ranger", "dmg": 1.3, "dex": 1.4, "int": 1.0, "con": 1.0, "cha": 1.0 }, {"name": "bard", "dmg": 0.9, "dex": 1.1, "int": 1.2, "con": 0.9, "cha": 1.6}, {"name": "tank", "dmg": 0.9, "dex": 0.7, "int": 0.8, "con": 1.7, "cha": 0.9}]
    races = [{"name": "Human", "dmg": 1.0, "dex": 1.0, "int": 1.0, "con": 1.0, "cha": 1.0}, {"name": "Elf", "dmg": 0.9, "dex": 1.2, "int": 1.1, "con": 0.9, "cha": 1.1}, {"name": "Ork", "dmg": 1.3, "dex": 0.8, "int": 0.7, "con": 1.2, "cha": 0.8}, {"name": "Dwarf", "dmg": 1.1, "dex": 0.8, "int": 0.9, "con": 1.3, "cha": 0.9}, {"name": "Halfling", "dmg": 0.8, "dex": 1.3, "int": 1.0, "con": 0.9, "cha": 1.2}]
    items = [{"name": "Iron Sword", "dmg": 1.2}, {"name": "Dagger", "dex": 1.3}, {"name": "Wizard Staff", "int": 1.4}, {"name": "Heavy Armor", "con": 1.5}, {"name": "Silver Amulet", "cha": 1.3}]
    characters = [{"name": "example character 1", "class": "rogue", "level": 15, "race": "Elf", "attributes": [], "skills": {}, "inventory": [], "stats": {}}]
    while True:
        choice = menu(options)
        if choice.get('index') == 0:
            characters = add_character.add_menu(characters, classes, races, items)
        elif choice.get('index') == 1:
            if selected_character == "":
                characters, selected_character = skill_manager.skill_menu(characters, selected_character)
            else:
                print("Please select a character before entering this function.")
                input("Press Enter to continue...")
                continue  
        elif choice.get('index') == 2:
            if selected_character != "":
                characters, selected_character = inventory_manager.inventory_menu(characters, selected_character)
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
                characters, selected_character = search_compare.search_menu(characters, selected_character, comp=True)
            else:
                print("Please select a character before entering this function.")
                input("Press Enter to continue...")
                continue
        elif choice.get('index') == 5:
            characters, selected_character = search_compare.search_menu(characters, selected_character, comp=False)
        else:
            print("ERROR")
        #UPDATE ALL CHARACTER STATS AFTER EVERY CHANGE
main()