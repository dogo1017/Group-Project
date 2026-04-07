# DU p1 - Attribute Manager

from menu import menu

def attribute_menu(characters, selected_character):
    # Main attribute management menu
    # Returns: (characters, selected_character) tuple
    
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
            "Modify Damage", 
            "Modify Dexterity",
            "Modify Intelligence",
            "Modify Constitution",
            "Modify Charisma",
            "Return"
        ]
        
        result = menu(attribute_options)
        choice = result['index']
        
        if choice == 0:
            # Modify Level
            modify_level(characters, char_index)
        elif choice == 1:
            # Modify Damage
            modify_attribute(characters, char_index, 0, "Damage")
        elif choice == 2:
            # Modify Dexterity
            modify_attribute(characters, char_index, 1, "Dexterity")
        elif choice == 3:
            # Modify Intelligence
            modify_attribute(characters, char_index, 2, "Intelligence")
        elif choice == 4:
            # Modify Constitution
            modify_attribute(characters, char_index, 3, "Constitution")
        elif choice == 5:
            # Modify Charisma
            modify_attribute(characters, char_index, 4, "Charisma")
        else:
            # Return
            break
    
    return characters, selected_character


def modify_level(characters, char_index):
    # Modify character level
    current_level = characters[char_index].get("level", 1)
    
    import os
    os.system('cls')
    print(f"\n{'='*50}")
    print(f"MODIFY LEVEL")
    print(f"{'='*50}")
    print(f"\nCurrent Level: {current_level}")
    print("\nEnter new level (1-100):")
    
    try:
        new_level = int(input("> "))
        if 1 <= new_level <= 100:
            characters[char_index]["level"] = new_level
            print(f"\n✓ Level updated to {new_level}!")
        else:
            print("\n✗ Level must be between 1 and 100!")
    except ValueError:
        print("\n✗ Invalid input! Please enter a number.")
    
    input("\nPress Enter to continue...")


def modify_attribute(characters, char_index, attr_index, attr_name):
    # Modify a specific attribute in the base_attributes list
    # Ensure base_attributes list exists and has enough elements
    if "base_attributes" not in characters[char_index]:
        characters[char_index]["base_attributes"] = [5, 5, 5, 5, 5]
    
    current_value = characters[char_index]["base_attributes"][attr_index]
    
    import os
    os.system('cls')
    print(f"\n{'='*50}")
    print(f"MODIFY {attr_name.upper()}")
    print(f"{'='*50}")
    print(f"\nCurrent Base {attr_name}: {current_value}")
    
    # Show what the final value will be with bonuses
    if "attributes" in characters[char_index] and len(characters[char_index]["attributes"]) > attr_index:
        final_value = characters[char_index]["attributes"][attr_index]
        print(f"Current Final {attr_name} (with bonuses): {final_value:.2f}")
    
    print("\nEnter new base value (-100 to 100):")
    print("(Note: Final value includes bonuses from race, class, and equipment)")
    
    try:
        new_value = int(input("> "))
        if -100 <= new_value <= 100:
            characters = list(characters)
            characters[char_index]["base_attributes"][attr_index] = new_value
            characters = tuple(characters)
            print(f"\n✓ Base {attr_name} updated to {new_value}!")
        else:
            print("\n✗ Value must be between -100 and 100!")
    except ValueError:
        print("\n✗ Invalid input! Please enter a number.")
    
    input("\nPress Enter to continue...")


