# DU p1 - Attribute Manager

from menu import menu

def attribute_menu(characters, selected_character):
    """
    Main attribute management menu
    Returns: (characters, selected_character) tuple
    """
    
    # If no character selected, let user select one
    if selected_character == "":
        char_names = [char["name"] for char in characters]
        char_names.append("Return")
        result = menu(char_names)
        selected_index = result['index']
        
        if selected_index >= len(characters):
            return characters, selected_character
        
        selected_character = characters[selected_index]["name"]
    
    # Find the selected character in the characters list
    current_character = None
    char_index = 0
    for i, char in enumerate(characters):
        if char["name"] == selected_character:
            current_character = char
            char_index = i
            break
    
    if current_character is None:
        print("Character not found!")
        input("Press Enter to continue...")
        return characters, ""
    
    # Main attribute management loop
    while True:
        # Build attribute options list
        attribute_options = [
            "Modify Level",
            "Modify Class", 
            "Modify Race",
            "View All Attributes",
            "Return"
        ]
        
        result = menu(attribute_options)
        choice = result['index']
        
        if choice == 0:
            # Modify Level
            modify_level(characters, char_index)
        elif choice == 1:
            # Modify Class
            modify_class(characters, char_index)
        elif choice == 2:
            # Modify Race
            modify_race(characters, char_index)
        elif choice == 3:
            # View All Attributes
            view_attributes(current_character)
        else:
            # Return
            break
    
    return characters, selected_character


def modify_level(characters, char_index):
    """Modify character level"""
    current_level = characters[char_index].get("level", 1)
    
    print(f"\nCurrent Level: {current_level}")
    print("Use Left/Right arrows to adjust level, Enter to save")
    
    result = menu(
        [f"New Level", "Save Changes", "Cancel"],
        number=[0],
        num_min=1,
        num_max=100
    )
    
    if result['index'] == 1:  # Save Changes
        new_level = result['numbers'][0]
        characters[char_index]["level"] = new_level
        print(f"\nLevel updated to {new_level}!")
        input("Press Enter to continue...")
    else:
        print("\nLevel change cancelled.")
        input("Press Enter to continue...")


def modify_class(characters, char_index):
    """Modify character class"""
    classes = ["rogue", "warrior", "mage", "paladin", "ranger", "bard", "tank"]
    current_class = characters[char_index].get("class", "rogue")
    
    print(f"\nCurrent Class: {current_class}")
    print("Select new class:")
    
    class_options = [*classes, "Cancel"]
    result = menu(class_options)
    
    if result['index'] < len(classes):
        new_class = classes[result['index']]
        characters[char_index]["class"] = new_class
        print(f"\nClass updated to {new_class}!")
        input("Press Enter to continue...")
    else:
        print("\nClass change cancelled.")
        input("Press Enter to continue...")


def modify_race(characters, char_index):
    """Modify character race"""
    races = ["Human", "Elf", "Ork", "Dwarf", "Halfling"]
    current_race = characters[char_index].get("race", "Human")
    
    print(f"\nCurrent Race: {current_race}")
    print("Select new race:")
    
    race_options = [*races, "Cancel"]
    result = menu(race_options)
    
    if result['index'] < len(races):
        new_race = races[result['index']]
        characters[char_index]["race"] = new_race
        print(f"\nRace updated to {new_race}!")
        input("Press Enter to continue...")
    else:
        print("\nRace change cancelled.")
        input("Press Enter to continue...")


def view_attributes(character):
    """Display all character attributes"""
    print(f"\n{'='*50}")
    print(f"Character Attributes for: {character.get('name', 'Unknown')}")
    print(f"{'='*50}")
    print(f"Class: {character.get('class', 'N/A')}")
    print(f"Race: {character.get('race', 'N/A')}")
    print(f"Level: {character.get('level', 1)}")
    
    # Display stats if they exist
    if "stats" in character and character["stats"]:
        print(f"\nStats:")
        for stat, value in character["stats"].items():
            print(f"  {stat.upper()}: {value}")
    
    # Display skills if they exist
    if "skills" in character and character["skills"]:
        print(f"\nSkills: {len(character['skills'])} total")
        for skill_name in character["skills"].keys():
            print(f"  - {skill_name}")
    
    # Display inventory if it exists
    if "inventory" in character and character["inventory"]:
        print(f"\nInventory: {len(character['inventory'])} items")
        for item in character["inventory"]:
            if isinstance(item, dict) and "name" in item:
                print(f"  - {item['name']}")
            elif isinstance(item, dict):
                print(f"  - {list(item.keys())[0] if item else 'Unknown item'}")
    
    print(f"{'='*50}\n")
    input("Press Enter to continue...")