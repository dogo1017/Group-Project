from menu import menu

def skill_menu(saved_skills, characters, selected_character):
    """
    Main skill management menu
    Returns: (characters, selected_character) tuple
    """

    from menu import menu
    
    if selected_character == "":
        char_names = [char["name"] for char in characters]
        char_names.append("Return")
        result = menu(char_names)
        selected_index = result['index']
        
        if selected_index >= len(characters):
            return characters, selected_character
        
        selected_character = characters[selected_index]["name"]
    
    current_character = None
    for char in characters:
        if char["name"] == selected_character:
            current_character = char
            break
    
    if current_character is None:
        print("Character not found!")
        input("Press Enter to continue...")
        return characters, ""
    
    skill_manage = True
    while skill_manage:
        result = menu(["Add Skill", "Remove Skill", "View Character Skills", "Return"])
        selected_index = result['index']
        
        if selected_index == 0:
            add_skill(saved_skills, current_character)
        elif selected_index == 1:
            remove_skill(current_character)
        elif selected_index == 2:
            view_skills(saved_skills, current_character)
        else:
            skill_manage = False
    
    return characters, selected_character


def add_skill(saved_skills, character):
    """Add a skill to the character"""
    result = menu(["Add Existing Skill", "Edit Existing Skill", "Add New Skill", "Return"])
    result_index = result['index']
    
    if result_index == 0:
        if not saved_skills:
            print("No saved skills available!")
            input("Press Enter to continue...")
            return
            
        skill_names = list(saved_skills.keys())
        skill_result = menu([*skill_names, "Return"])
        selected = skill_result['index']
        
        if selected < len(skill_names):
            selected_skill = skill_names[selected]
            if selected_skill in character["skills"]:
                print(f"{selected_skill} is already in {character['name']}'s skills!")
                input("Press Enter to continue...")
            else:
                character["skills"].add(selected_skill)  # Changed to add()
                print(f"Added {selected_skill} to {character['name']}!")
                input("Press Enter to continue...")
    
    elif result_index == 1:
        if not character["skills"]:
            print("No skills to edit!")
            input("Press Enter to continue...")
            return
            
        skill_list = list(character["skills"])
        edit_result = menu([*skill_list, "Return"])
        selected = edit_result['index']
        
        if selected < len(skill_list):
            skill_to_edit = skill_list[selected]
            skill_info = saved_skills[skill_to_edit]
            
            skill_data = menu(
                ["Skill Name", "Skill Description", "Skill Effect", "Effect Strength", "Skill Target", "Save Changes", "Return"],
                writable=[0, 1],
                toggle=[2, 4],
                tog_opts=[["Attack", "Defense", "Health"], [["Enemy", "Self", "Ally"], [4]]],
                number=[3]
            )
            
            if skill_data['index'] == 5:
                new_name = ''.join(skill_data['writable'][0]) or skill_to_edit
                new_desc = ''.join(skill_data['writable'][1]) or skill_info["description"]
                
                updated_skill = {
                    "description": new_desc,
                    "effect": skill_data['toggles'][2],
                    "amount": skill_data['numbers'][3],
                    "target": skill_data['toggles'][4]
                }
                
                saved_skills[new_name] = updated_skill
                
                if new_name != skill_to_edit:
                    character["skills"].remove(skill_to_edit)  # Changed to remove()
                    if skill_to_edit in saved_skills:
                        del saved_skills[skill_to_edit]
                
                character["skills"].add(new_name)  # Changed to add()
                print("Skill updated!")
                input("Press Enter to continue...")
    
    elif result_index == 2:
        skill_data = menu(
            ["Skill Name", "Skill Description", "Skill Effect", "Effect Strength", "Skill Target", "Save Skill", "Return"],
            writable=[0, 1],
            toggle=[2, 4],
            tog_opts=[["Attack", "Defense", "Health"], [["Enemy", "Self", "Ally"], [4]]],
            number=[3]
        )
        
        if skill_data['index'] == 5:
            skill_name = ''.join(skill_data['writable'][0])
            skill_desc = ''.join(skill_data['writable'][1])
            
            if skill_name:
                new_skill = {
                    "description": skill_desc,
                    "effect": skill_data['toggles'][2],
                    "amount": skill_data['numbers'][3],
                    "target": skill_data['toggles'][4]
                }
                
                saved_skills[skill_name] = new_skill
                character["skills"].add(skill_name)  # Changed to add()
                print(f"Created and added {skill_name} to {character['name']}!")
            else:
                print("Skill name cannot be empty!")
            input("Press Enter to continue...")


def remove_skill(character):
    """Remove a skill from the character"""
    if not character["skills"]:
        print("No skills to remove!")
        input("Press Enter to continue...")
        return
    
    skill_list = list(character["skills"])
    result = menu([*skill_list, "Return"])
    selected = result['index']
    
    if selected < len(skill_list):
        removed_skill = skill_list[selected]
        character["skills"].remove(removed_skill)  # Changed to remove()
        print(f"Removed {removed_skill} from {character['name']}!")
        input("Press Enter to continue...")


def view_skills(saved_skills, character):
    """View all skills for the character"""
    print(f"\n{character['name']}'s Skills:")
    if character["skills"]:
        for skill_name in character["skills"]:
            skill_info = saved_skills.get(skill_name, {})
            print(f"\n  {skill_name}")
            print(f"    Description: {skill_info.get('description', 'N/A')}")
            print(f"    Effect: {skill_info.get('effect', 'N/A')}")
            print(f"    Strength: {skill_info.get('amount', 'N/A')}")
            print(f"    Target: {skill_info.get('target', 'N/A')}")
    else:
        print("  No skills yet!")
    input("\nPress Enter to continue...")