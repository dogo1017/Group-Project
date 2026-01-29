from menu import menu
saved_skills = {
    "Fireball": {"description": "Shoots a fireball", "effect": "Attack", "amount": 50, "target": "Enemy"},
    "Heal": {"description": "Restores health", "effect": "Health", "amount": 30, "target": "Self"},
    "Shield": {"description": "Increases defense", "effect": "Defense", "amount": 20, "target": "Self"}
}

example_character = {
    "name": "Hero",
    "skills": set()
}

def add_skill(existing_skills):
    result = menu(["Add Existing Skill", "Edit Existing Skill", "Add New Skill", "Return"])
    result = result['index']
    
    if result == 0:
        skill_names = list(saved_skills.keys())
        skill_result = menu([*skill_names, "Return"])
        selected = skill_result['index']
        if selected < len(skill_names):
            selected_skill = skill_names[selected]
            if selected_skill in example_character["skills"]:
                print(f"{selected_skill} is already in character's skills!")
                input("Press Enter to continue...")
            else:
                example_character["skills"].add(selected_skill)
                print(f"Added {selected_skill} to character!")
                input("Press Enter to continue...")
        return
    
    elif result == 1:
        if not example_character["skills"]:
            print("No skills to edit!")
            input("Press Enter to continue...")
            return
        skill_list = list(example_character["skills"])
        edit_result = menu([*skill_list, "Return"])
        selected = edit_result['index']
        if selected < len(skill_list):
            skill_to_edit = skill_list[selected]
            if skill_to_edit in saved_skills:
                skill_data = menu(
                    ["Skill Name", "Skill Description", "Skill Effect", "Effect Strength", "Skill Target", "Save Changes", "Return"],
                    writable=[0, 1],
                    toggle=[2, 4],
                    tog_opts=[["Attack", "Defense", "Health"], [["Enemy", "Self", "Ally"], [4]]],
                    number=[3]
                )
                if skill_data['index'] == 5:
                    new_name = ''.join(skill_data['writable'][0]) or skill_to_edit
                    new_desc = ''.join(skill_data['writable'][1]) or saved_skills[skill_to_edit]["description"]
                    saved_skills[new_name] = {
                        "description": new_desc,
                        "effect": skill_data['toggles'][2],
                        "amount": skill_data['numbers'][3],
                        "target": skill_data['toggles'][4]
                    }
                    if new_name != skill_to_edit:
                        del saved_skills[skill_to_edit]
                        example_character["skills"].discard(skill_to_edit)
                        example_character["skills"].add(new_name)
                    print("Skill updated!")
                    input("Press Enter to continue...")
        return
    
    elif result == 2:
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
                if skill_name in example_character["skills"]:
                    print(f"{skill_name} is already in character's skills!")
                else:
                    saved_skills[skill_name] = {
                        "description": skill_desc,
                        "effect": skill_data['toggles'][2],
                        "amount": skill_data['numbers'][3],
                        "target": skill_data['toggles'][4]
                    }
                    example_character["skills"].add(skill_name)
                    print(f"Created and added {skill_name} to character!")
            else:
                print("Skill name cannot be empty!")
            input("Press Enter to continue...")
        return
def remove_skill():
    if not example_character["skills"]:
        print("No skills to remove!")
        input("Press Enter to continue...")
        return
    
    skill_list = list(example_character["skills"])
    result = menu([*skill_list, "Return"])
    selected = result['index']
    
    if selected < len(skill_list):
        removed_skill = skill_list[selected]
        example_character["skills"].discard(removed_skill)
        print(f"Removed {removed_skill} from character!")
        input("Press Enter to continue...")

def skill_menu():
    skill_manage = 1
    while skill_manage == 1:
        result = menu(["Add Skill", "Remove Skill", "View Character Skills", "Return"])
        selected_index = result['index']
        if selected_index == 0:
            add_skill(example_character["skills"])
        elif selected_index == 1:
            remove_skill()
        elif selected_index == 2:
            print(f"\n{example_character['name']}'s Skills:")
            if example_character["skills"]:
                for skill in example_character["skills"]:
                    if skill in saved_skills:
                        skill_info = saved_skills[skill]
                        print(f"\n  {skill}")
                        print(f"    Description: {skill_info['description']}")
                        print(f"    Effect: {skill_info['effect']}")
                        print(f"    Strength: {skill_info['amount']}")
                        print(f"    Target: {skill_info['target']}")
            else:
                print("  No skills yet!")
            input("\nPress Enter to continue...")
        else:
            skill_manage = 0