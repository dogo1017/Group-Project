def add_menu(characters, classes, races, items): 
    from menu import menu
    import text
    import os
    os.system('cls')
    text.bubble("Welcome to the Add Character Function. Here you will add the initial stats and stuff to your character. These changes are not final and can be changed later through different functions. You might need to adjust your terminal to fit all the following options.", speed= .02)
    result = menu(["Name", "Class", "Level", "Race", "Attributes", " Damage", " Dexterity", " Intellegence", " Constitution", " Charisma", "Skills", " Fireball", " Heal", " Shield", "Inventory", " Iron Sword", " Dagger", " Wizard Staff", " Heavy Armor", " Silver Amulet", "Return", "Return Without Saving"],
    number=[2, 5, 6, 7, 8, 9],
    writable=[0],
    num_min= -1000,
    num_max= 1000,
    toggle=[1, 3, 11, 12, 13, 15, 16, 17, 18, 19],
    tog_opts=[["Get", "Don't Get"], [[i.get('name', None).title() for i in classes], [1]], [[i.get('name', None) for i in races], [3]]])   
    selected_index = result['index']
    
    if selected_index == 21:
        return characters
    # elif name is empty tell user it is and ask them if they want to restart their creation or continue back to main menu without saving
    elif ''.join(result['writable'][0]) == "":
        print("You didn't enter a valid name. Would you like to restart character creation, or go back to main without saving.")
        input("Press Enter to continue...")
        result = menu(["Restart Character Creation", "Continue to Main Menu Without saving"])
        selected_index = result['index']
        if selected_index == 0:
            characters = add_menu(characters, classes, races, items)
            return characters
        else:
            return characters
    else:
        # Build the initial skills set based on toggles
        initial_skills = set()
        if result['toggles'][11] == "Get":
            initial_skills.add("Fireball")
        if result['toggles'][12] == "Get":
            initial_skills.add("Heal")
        if result['toggles'][13] == "Get":
            initial_skills.add("Shield")
        
        # Build the initial inventory based on toggles
        initial_inventory = []
        if result['toggles'][15] == "Get":
            initial_inventory.append("Iron Sword")
        if result['toggles'][16] == "Get":
            initial_inventory.append("Dagger")
        if result['toggles'][17] == "Get":
            initial_inventory.append("Wizard Staff")
        if result['toggles'][18] == "Get":
            initial_inventory.append("Heavy Armor")
        if result['toggles'][19] == "Get":
            initial_inventory.append("Silver Amulet")
        
        # Create the new character with proper initialization
        new_character = {
            "name": ''.join(result['writable'][0]), 
            "class": result['toggles'][1], 
            "level": result['numbers'][2], 
            "race": result['toggles'][3], 
            "attributes": [], 
            "base_attributes": [result['numbers'][5], result['numbers'][6], result['numbers'][7], result['numbers'][8], result['numbers'][9]],
            "skills": initial_skills,  # Proper set of skill names
            "skill_levels": {skill: 1 for skill in initial_skills},  # Initialize skill levels
            "inventory": initial_inventory  # List of item names
        }
        
        characters.append(new_character)
        
        print(f"\nCharacter '{new_character['name']}' created successfully!")
        print(f"Level: {new_character['level']}")
        print(f"Class: {new_character['class']}")
        print(f"Race: {new_character['race']}")
        print(f"Skills: {len(initial_skills)}")
        print(f"Inventory: {len(initial_inventory)} items")
        input("\nPress Enter to continue...")
        
        return characters