# Main run file. Holds the user interface
import add_character as add_character
import attribute_manager as attribute_manager
import inventory_manager as inventory_manager
import selecter as selecter
import skill_manager as skill_manager
import view as view
from menu import menu    
import text as text
import os
import data_visualization as data_visualization
import statistical_analyzer as statistical_analyzer
import random_generator as random_generator


def visualization_menu(characters, visualizer):
    import os
    options = [
        "Individual Character Radar Chart",
        "Individual Character Bar Chart",
        "Multi-Character Stat Comparison",
        "Class Distribution Analysis",
        "Character Level Progression",
        "Return"
    ]
    while True:
        os.system('cls')
        result = menu(options)
        choice = result['index']

        if choice == 5:
            break

        if not characters:
            print("No characters available.")
            input("Press Enter to continue...")
            continue

        if choice == 0 or choice == 1:
            char_names = [c["name"] for c in characters]
            char_names.append("Return")
            os.system('cls')
            pick = menu(char_names)
            if pick['index'] >= len(characters):
                continue
            character = characters[pick['index']]
            if choice == 0:
                visualizer.radar_chart(character)
            else:
                visualizer.bar_chart(character)
            input("Press Enter to continue...")

        elif choice == 2:
            char_names = [c["name"] for c in characters]
            char_names.append("Done selecting")
            selected_chars = []
            os.system('cls')
            print("Select characters to compare (select Done when finished):")
            while True:
                pick = menu(char_names)
                if pick['index'] >= len(characters):
                    break
                selected_char = characters[pick['index']]
                if selected_char not in selected_chars:
                    selected_chars.append(selected_char)
                    print(f"Added {selected_char['name']}")
            if len(selected_chars) >= 2:
                visualizer.comparison_bar_chart(selected_chars)
                input("Press Enter to continue...")
            else:
                print("Need at least 2 characters to compare.")
                input("Press Enter to continue...")

        elif choice == 3:
            visualizer.class_distribution_chart(characters)
            input("Press Enter to continue...")

        elif choice == 4:
            visualizer.level_progression_chart(characters)
            input("Press Enter to continue...")


def analysis_menu(characters, analyzer):
    import os
    options = [
        "Roster Summary Statistics",
        "Filter Characters by Class",
        "Sort Characters by Stat",
        "Top Characters by Stat",
        "Return"
    ]
    while True:
        os.system('cls')
        result = menu(options)
        choice = result['index']

        if choice == 4:
            break

        if not characters:
            print("No characters available.")
            input("Press Enter to continue...")
            continue

        if choice == 0:
            os.system('cls')
            analyzer.print_summary_stats(characters)

        elif choice == 1:
            os.system('cls')
            class_name = input("Enter class name to filter by: ").strip()
            analyzer.print_filtered_by_class(characters, class_name)

        elif choice == 2:
            os.system('cls')
            print("Sort by: level, damage, dexterity, intelligence, constitution, charisma, skill_count, inventory_count")
            col = input("Enter stat name: ").strip().lower()
            analyzer.print_sorted_by(characters, col)

        elif choice == 3:
            os.system('cls')
            print("Top by: level, damage, dexterity, intelligence, constitution, charisma")
            stat = input("Enter stat name: ").strip().lower()
            try:
                top_n = int(input("How many top characters to show: "))
            except ValueError:
                top_n = 3
            analyzer.print_top_characters(characters, stat, top_n)


def data_management_menu(characters, analyzer):
    import os
    options = [
        "Export Characters to CSV",
        "Import Characters from CSV",
        "Return"
    ]
    while True:
        os.system('cls')
        result = menu(options)
        choice = result['index']

        if choice == 2:
            break

        if choice == 0:
            os.system('cls')
            analyzer.export_to_csv(characters)

        elif choice == 1:
            os.system('cls')
            characters = analyzer.import_from_csv(characters)

    return characters


def random_generator_menu(characters, generator):
    import os
    options = [
        "Generate Random Character",
        "Generate Character Backstory",
        "Generate Character Description",
        "Generate Random Quest",
        "Generate Random Name",
        "Return"
    ]
    while True:
        os.system('cls')
        result = menu(options)
        choice = result['index']

        if choice == 5:
            break

        if choice == 0:
            os.system('cls')
            new_char = generator.generate_random_character()
            print(f"\nGenerated Character:")
            print(f"  Name:  {new_char['name']}")
            print(f"  Class: {new_char['class']}")
            print(f"  Race:  {new_char['race']}")
            print(f"  Level: {new_char['level']}")
            print(f"  Base Attributes: {new_char['base_attributes']}")
            add = input("\nAdd this character to your roster? (y/n): ").strip().lower()
            if add == 'y':
                characters = list(characters)
                characters.append(new_char)
                characters = tuple(characters)
                print(f"Added {new_char['name']} to roster!")
            input("\nPress Enter to continue...")

        elif choice == 1:
            os.system('cls')
            if not characters:
                print("No characters available.")
                input("Press Enter to continue...")
                continue
            char_names = [c["name"] for c in characters]
            char_names.append("Return")
            pick = menu(char_names)
            if pick['index'] < len(characters):
                character = characters[pick['index']]
                backstory = generator.generate_backstory(character["name"], character.get("class", "adventurer"), character.get("race", "Human"))
                os.system('cls')
                print(f"\nBackstory for {character['name']}:")
                print(f"\n{backstory}")
                input("\nPress Enter to continue...")

        elif choice == 2:
            os.system('cls')
            if not characters:
                print("No characters available.")
                input("Press Enter to continue...")
                continue
            char_names = [c["name"] for c in characters]
            char_names.append("Return")
            pick = menu(char_names)
            if pick['index'] < len(characters):
                character = characters[pick['index']]
                description = generator.generate_character_description(character)
                os.system('cls')
                print(f"\nDescription:")
                print(f"\n{description}")
                input("\nPress Enter to continue...")

        elif choice == 3:
            os.system('cls')
            quest = generator.generate_quest()
            print(f"\n{quest}")
            input("\nPress Enter to continue...")

        elif choice == 4:
            os.system('cls')
            name = generator.generate_name()
            print(f"\nGenerated Name: {name}")
            input("\nPress Enter to continue...")

    return characters


def main():
    text.bubble("Welcome to our program! This is our RPG Character Manager. Use up/down arrow keys to change options, left and right to change values, and options with ':' are writable (If you need more help click on the help option to tell you what everything does)", speed= 0.01)
    selected_character = "example character 1"
    options = [
        "Add Character",
        "Manage Skills",
        "Manage Inventory",
        "Manage Attributes",
        "View / Compare Characters",
        "Select / Search Characters",
        "Help",
        "Character Visualization",
        "Statistical Analysis",
        "Random Generator",
        "Save/Import Characters",
        f' (Your current selected character is "{selected_character}")'
    ]
    classes = [{"name": "rogue", "dmg": 1.2, "dex": 1.5, "int": 1.1, "con": 0.9, "cha": 1.2}, {"name": "warrior", "dmg": 1.5, "dex": 0.9, "int": 0.8, "con": 1.4, "cha": 1.0}, {"name": "mage", "dmg": 1.3, "dex": 0.8, "int": 1.6, "con": 0.7, "cha": 1.1}, {"name": "paladin", "dmg": 1.2, "dex": 0.9, "int": 1.0, "con": 1.3, "cha": 1.4 }, {"name": "ranger", "dmg": 1.3, "dex": 1.4, "int": 1.0, "con": 1.0, "cha": 1.0 }, {"name": "bard", "dmg": 0.9, "dex": 1.1, "int": 1.2, "con": 0.9, "cha": 1.6}, {"name": "tank", "dmg": 0.9, "dex": 0.7, "int": 0.8, "con": 1.7, "cha": 0.9}]
    races = [{"name": "Human", "dmg": 1.0, "dex": 1.0, "int": 1.0, "con": 1.0, "cha": 1.0}, {"name": "Elf", "dmg": 0.9, "dex": 1.2, "int": 1.1, "con": 0.9, "cha": 1.1}, {"name": "Ork", "dmg": 1.3, "dex": 0.8, "int": 0.7, "con": 1.2, "cha": 0.8}, {"name": "Dwarf", "dmg": 1.1, "dex": 0.8, "int": 0.9, "con": 1.3, "cha": 0.9}, {"name": "Halfling", "dmg": 0.8, "dex": 1.3, "int": 1.0, "con": 0.9, "cha": 1.2}]
    items = [
        {"name": "Iron Sword", "dmg": 1.2, "weight": 5.0, "value": 150, "effects": "Sharp edge, reliable weapon"},
        {"name": "Dagger", "dex": 1.3, "weight": 1.5, "value": 75, "effects": "Lightweight, easy to conceal"},
        {"name": "Wizard Staff", "int": 1.4, "weight": 3.0, "value": 300, "effects": "Channeling magic, arcane focus"},
        {"name": "Heavy Armor", "con": 1.5, "weight": 25.0, "value": 500, "effects": "High protection, reduced mobility"},
        {"name": "Silver Amulet", "cha": 1.3, "weight": 0.2, "value": 200, "effects": "Enchanted charm, noble appearance"}
    ]
    characters = ({
        "name": "example character 1",
        "class": "rogue", 
        "level": 15, 
        "race": "Elf", 
        "attributes": [], 
        "base_attributes": [5, 5, 5, 5, 5], 
        "skills": set(),                    
        "skill_levels": {},
        "inventory": []
    },)

    saved_skills = skill_manager.initialize_default_skills()
    visualizer = data_visualization.DataVisualization()
    analyzer = statistical_analyzer.StatisticalAnalyzer()
    generator = random_generator.RandomGenerator()

    while True:
        choice = menu(options)
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
            text.bubble("Welcome to the Help Menu! Use the up and down arrow keys to navigate through menu options. Press Enter to select an option. For writable fields (marked with ':'), you can type directly. For number fields (shown with <>), use left and right arrows to adjust values. For toggle fields, use left and right arrows to cycle through options.", speed=0.01)
            result = menu(["Add Character", "Manage Skills", "Manage Inventory", "Manage Attributes", "View / Compare Characters", "Select / Search Characters"])
            selected_index = result['index']
            os.system('cls')
            if selected_index == 1:
                text.bubble("Add Character: This function lets you create a new character for your RPG. You'll set your character's name, choose their class and race, and set their starting level. You can also assign initial attribute points like damage, dexterity, intelligence, constitution, and charisma. Additionally, you can select starting skills and inventory items. Don't worry - all of these choices can be changed later through other menu options!", speed=0.01)
                os.system('cls')
            elif selected_index == 2:
                text.bubble("Manage Skills: This is where you control your character's abilities and powers. You can add new skills from a saved library, create completely custom skills with unique effects, or edit existing skills your character already knows. Each skill has a name, description, effect type (Attack, Defense, or Health), strength amount, and target (Enemy, Self, or Ally). You can also view all your character's current skills and remove any you no longer want.", speed=0.01)
                os.system('cls')
            elif selected_index == 3:
                text.bubble("Manage Inventory: Use this menu to equip your character with powerful items! You can add items from the available item list to your character's inventory, remove items you no longer need, or view all the items your character is currently carrying. Each item provides stat bonuses like increased damage, dexterity, intelligence, constitution, or charisma. Build the perfect loadout for your character's playstyle!", speed=0.01)
                os.system('cls')
            elif selected_index == 4:
                text.bubble("Manage Attributes: This function allows you to modify your character's core stat values. You can change your character's strength as they progress and grow stronger, change your character's constitution for a more beefy build, and other values. You can also view a complete summary of all your character's attributes one convenient display.", speed=0.01)
                os.system('cls')
            elif selected_index == 5:
                text.bubble("View / Compare Characters: This feature lets you compare two characters side by side or just one. You can select your currently active character and view it or use it and another character from your roster to compare. You'll be able to see their stats, skills, and equipment to help you decide which character is better suited for different situations.", speed=0.01)
                os.system('cls')
            elif selected_index == 6:
                text.bubble("Select / Search Characters: This function lets you search for a character to select and change for all the rest of the functions.", speed=0.01)
                os.system('cls')
        elif choice.get('index') == 7:
            visualization_menu(characters, visualizer)
        elif choice.get('index') == 8:
            analysis_menu(characters, analyzer)
        elif choice.get('index') == 9:
            characters = random_generator_menu(characters, generator)
        elif choice.get('index') == 10:
            characters = data_management_menu(characters, analyzer)

        def lookup(data_list):
            index = {entry["name"]: entry for entry in data_list}
            def find(name):
                return index.get(name)
            return find
        
        def attribute_applier():
            keys = ["dmg", "dex", "int", "con", "cha"]
            def apply(attributes, source):
                if source:
                    for i, key in enumerate(keys):
                        if key in source:
                            attributes[i] *= source[key]
            return apply
        
        find_race = lookup(races)
        find_class = lookup(classes)
        apply_multipliers = attribute_applier()

        for character in characters:
            character["attributes"] = [float(val) for val in character["base_attributes"]]

            race_data = find_race(character["race"])
            class_data = find_class(character["class"])

            for item in character["inventory"]:
                apply_multipliers(character["attributes"], item)

            apply_multipliers(character["attributes"], race_data)
            apply_multipliers(character["attributes"], class_data)

main()