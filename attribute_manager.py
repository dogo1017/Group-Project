#DU p1 

from menu import menu

selected_character = "example character 1"
options = ["Add Character", "Manage Skills", "Manage Inventory", "Manage Attributes", "Compare Characters", "Search Characters"]
classes = [{"name": "rogue", "dmg": 1.2, "dex": 1.5, "int": 1.1, "con": 0.9, "cha": 1.2}, {"name": "warrior", "dmg": 1.5, "dex": 0.9, "int": 0.8, "con": 1.4, "cha": 1.0}, {"name": "mage", "dmg": 1.3, "dex": 0.8, "int": 1.6, "con": 0.7, "cha": 1.1}, {"name": "paladin", "dmg": 1.2, "dex": 0.9, "int": 1.0, "con": 1.3, "cha": 1.4 }, {"name": "ranger", "dmg": 1.3, "dex": 1.4, "int": 1.0, "con": 1.0, "cha": 1.0 }, {"name": "bard", "dmg": 0.9, "dex": 1.1, "int": 1.2, "con": 0.9, "cha": 1.6}, {"name": "tank", "dmg": 0.9, "dex": 0.7, "int": 0.8, "con": 1.7, "cha": 0.9}]
races = [{"name": "Human", "dmg": 1.0, "dex": 1.0, "int": 1.0, "con": 1.0, "cha": 1.0}, {"name": "Elf", "dmg": 0.9, "dex": 1.2, "int": 1.1, "con": 0.9, "cha": 1.1}, {"name": "Ork", "dmg": 1.3, "dex": 0.8, "int": 0.7, "con": 1.2, "cha": 0.8}, {"name": "Dwarf", "dmg": 1.1, "dex": 0.8, "int": 0.9, "con": 1.3, "cha": 0.9}, {"name": "Halfling", "dmg": 0.8, "dex": 1.3, "int": 1.0, "con": 0.9, "cha": 1.2}]
items = [{"name": "Iron Sword", "dmg": 1.2}, {"name": "Dagger", "dex": 1.3}, {"name": "Wizard Staff", "int": 1.4}, {"name": "Heavy Armor", "con": 1.5}, {"name": "Silver Amulet", "cha": 1.3}]
characters = [{"name": "example character 1", "class": "rogue", "level": 15, "race": "Elf", "attributes": [], "skills": {}, "inventory": [], "stats": {}}]
attributes = []


def attribute_menu(characters, selected_character):
    while True:
        temp_count = 0
        for char in characters:
            if char.get("name") == selected_character:
                char_index = temp_count
            temp_count += 1
        current_character = characters[char_index]
        character_skills = current_character.get('skills')
        
        attribute_choice = menu(f"Select attribute to modify for {selected_character}:", attribute_options)
        if attribute_choice == "Return to Main":
            return
        confirm_modify = menu(f"Are you sure you want to modify {attribute_choice}?", ["Yes", "No"])
        if confirm_modify == "No":
            manage_again = menu("Would you like to manage different attributes?", ["Yes", "No"])
            if manage_again == "Yes":
                continue  
            return selected_character, characters
        current_value = characters[selected_character][attribute_choice]
        change_options = [f"Enter new value (Current: {current_value})", "Return to attribute selection"]
        change_choice = menu(f"Modify {attribute_choice}:", change_options)
        if change_choice == "Return to attribute selection":
            continue  
        while True:
            try:
                new_value_input = input(f"Enter new value for {attribute_choice}: ")
                if isinstance(current_value, int):
                    new_value = int(new_value_input)
                elif isinstance(current_value, float):
                    new_value = float(new_value_input)
                else:
                    new_value = new_value_input
                break
            except:
                print(f"Invalid input. Please enter {'an integer' if isinstance(current_value, int) else 'a number' if isinstance(current_value, float) else 'a value'}.")
        confirm_change = menu(f"Change {attribute_choice} from {current_value} to {new_value}?", ["Yes", "No"])
        if confirm_change == "No":
            continue  
        characters[selected_character][attribute_choice] = new_value
        print(f"{attribute_choice} updated to {new_value}")
        change_more = menu("Would you like to change more attributes?", ["Yes", "No (Return to Main)"])
        if change_more == "Yes":
            continue  
        else:
            return selected_character, characters
        
attribute_menu(characters, selected_character)