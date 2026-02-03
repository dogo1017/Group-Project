from menu import menu

def skill_menu(saved_skills, characters, selected_character):
    # Main skill management menu
    from menu import menu
    
    if selected_character == "":
        char_names = [char["name"] for char in characters]
        char_names.append("Return")
        result = menu(char_names)
        selected_index = result['index']
        
        if selected_index >= len(characters):
            return characters, selected_character
        
        selected_character = characters[selected_index]["name"]
    
    current_character = get_character(characters, selected_character)
    
    if current_character is None:
        print("Character not found!")
        input("Press Enter to continue...")
        return characters, ""
    
    skill_manage = True
    while skill_manage:
        result = menu(["Add Skill", "Remove Skill", "View Character Skills", "Level Up Skill", "View Skill Tree", "Return"])
        selected_index = result['index']
        
        if selected_index == 0:
            handle_add_skill(saved_skills, current_character)
        elif selected_index == 1:
            handle_remove_skill(current_character, saved_skills)
        elif selected_index == 2:
            handle_view_skills(saved_skills, current_character)
        elif selected_index == 3:
            handle_level_up_skill(saved_skills, current_character)
        elif selected_index == 4:
            handle_view_skill_tree(saved_skills, current_character)
        else:
            skill_manage = False
    
    return characters, selected_character


def get_character(characters, selected_character):
    # Helper function to find character by name
    for char in characters:
        if char["name"] == selected_character:
            return char
    return None


def initialize_skill_levels(character):
    # Initialize skill_levels dictionary if it doesn't exist
    if "skill_levels" not in character:
        character["skill_levels"] = {}


def initialize_default_skills():
    # Create a comprehensive skill library with 25+ skills organized by type
    
    def create_skill(description, effect, amount, target, level_req=1, max_level=10, prerequisites=None):
        # Inner function to create skill dictionary
        return {
            "description": description,
            "effect": effect,
            "amount": amount,
            "target": target,
            "level_requirement": level_req,
            "max_level": max_level,
            "prerequisites": prerequisites if prerequisites else [],
            "min_prerequisite_level": 1
        }
    
    skills = {}
    
    # BASIC COMBAT SKILLS (No prerequisites)
    skills["Basic Strike"] = create_skill("A simple physical attack", "Attack", 10, "Enemy", 1, 5)
    skills["Defend"] = create_skill("Raise your guard to block attacks", "Defense", 5, "Self", 1, 5)
    skills["Minor Heal"] = create_skill("Restore a small amount of health", "Health", 15, "Self", 1, 5)
    
    # FIRE MAGIC TREE
    skills["Spark"] = create_skill("Shoot a small spark of fire", "Attack", 15, "Enemy", 2, 8)
    skills["Fireball"] = create_skill("Launch a ball of flames", "Attack", 50, "Enemy", 5, 10, ["Spark"])
    skills["Flame Wave"] = create_skill("A wave of fire hits all enemies", "Attack", 40, "Enemy", 8, 10, ["Fireball"])
    skills["Inferno"] = create_skill("Devastating flames engulf the battlefield", "Attack", 100, "Enemy", 15, 10, ["Flame Wave"])
    skills["Phoenix Fire"] = create_skill("Legendary flames that revive the caster", "Health", 80, "Self", 20, 10, ["Inferno"])
    
    # ICE MAGIC TREE
    skills["Frost Touch"] = create_skill("Freeze an enemy with a touch", "Attack", 12, "Enemy", 2, 8)
    skills["Ice Shard"] = create_skill("Launch sharp ice projectiles", "Attack", 45, "Enemy", 5, 10, ["Frost Touch"])
    skills["Blizzard"] = create_skill("Summon a freezing storm", "Attack", 70, "Enemy", 10, 10, ["Ice Shard"])
    skills["Absolute Zero"] = create_skill("Ultimate ice magic freezes everything", "Attack", 120, "Enemy", 18, 10, ["Blizzard"])
    
    # HEALING TREE
    skills["Heal"] = create_skill("Restore moderate health", "Health", 30, "Self", 3, 10, ["Minor Heal"])
    skills["Greater Heal"] = create_skill("Restore significant health", "Health", 60, "Self", 7, 10, ["Heal"])
    skills["Mass Heal"] = create_skill("Heal all allies", "Health", 40, "Ally", 12, 10, ["Greater Heal"])
    skills["Resurrection"] = create_skill("Bring an ally back from defeat", "Health", 100, "Ally", 20, 10, ["Mass Heal"])
    
    # DEFENSIVE TREE
    skills["Shield"] = create_skill("Create a protective barrier", "Defense", 20, "Self", 3, 10, ["Defend"])
    skills["Iron Skin"] = create_skill("Harden your body against attacks", "Defense", 35, "Self", 6, 10, ["Shield"])
    skills["Fortress"] = create_skill("Become nearly invulnerable", "Defense", 60, "Self", 12, 10, ["Iron Skin"])
    skills["Guardian's Aura"] = create_skill("Protect all allies with a shield", "Defense", 45, "Ally", 16, 10, ["Fortress"])
    
    # ADVANCED COMBAT TREE
    skills["Power Strike"] = create_skill("A stronger physical attack", "Attack", 35, "Enemy", 4, 10, ["Basic Strike"])
    skills["Cleave"] = create_skill("Attack multiple enemies at once", "Attack", 55, "Enemy", 8, 10, ["Power Strike"])
    skills["Berserker Rage"] = create_skill("Massive damage at the cost of defense", "Attack", 90, "Enemy", 14, 10, ["Cleave"])
    
    # SUPPORT SKILLS
    skills["Focus"] = create_skill("Increase your concentration", "Defense", 10, "Self", 2, 8)
    skills["Battle Cry"] = create_skill("Boost all allies' morale", "Defense", 25, "Ally", 6, 10, ["Focus"])
    skills["Divine Blessing"] = create_skill("Grant protection to all allies", "Defense", 50, "Ally", 11, 10, ["Battle Cry"])
    
    # ULTIMATE SKILLS (Require multiple high-level prerequisites)
    skills["Armageddon"] = create_skill(
        "Ultimate destruction magic", "Attack", 150, "Enemy", 25, 10, 
        ["Inferno", "Absolute Zero", "Berserker Rage"]
    )
    skills["Transcendence"] = create_skill(
        "Achieve a higher state of being", "Defense", 100, "Self", 25, 10,
        ["Guardian's Aura", "Divine Blessing", "Resurrection"]
    )
    
    return skills


def handle_add_skill(saved_skills, character):
    # Handle the skill addition menu
    result = menu(["Add Existing Skill", "Edit Existing Skill", "Add New Skill", "Return"])
    result_index = result['index']
    
    if result_index == 0:
        add_existing_skill(saved_skills, character)
    elif result_index == 1:
        edit_existing_skill(saved_skills, character)
    elif result_index == 2:
        add_new_skill(saved_skills, character)


def add_existing_skill(saved_skills, character):
    # Add a skill from the saved skills library
    if not saved_skills:
        print("No saved skills available!")
        input("Press Enter to continue...")
        return
    
    initialize_skill_levels(character)
    
    # Categorize skills for better organization
    categorized_skills = categorize_skills(saved_skills)
    
    # Show categories
    categories = list(categorized_skills.keys())
    categories.append("View All Skills")
    categories.append("Return")
    
    cat_result = menu(categories)
    cat_selected = cat_result['index']
    
    # Handle Return
    if cat_selected == len(categories) - 1:
        return
    
    # Handle View All Skills
    if cat_selected == len(categories) - 2:
        skill_names = list(saved_skills.keys())
    else:
        # Handle specific category
        category = categories[cat_selected]
        skill_names = categorized_skills[category]
    
    skill_names.append("Return")
    skill_result = menu(skill_names)
    selected = skill_result['index']
    
    if selected < len(skill_names) - 1:
        selected_skill = skill_names[selected]
        attempt_add_skill(character, selected_skill, saved_skills)


def categorize_skills(saved_skills):
    # Categorize skills by their effect type and prerequisites
    
    def get_category(skill_name, skill_info):
        # Inner function to determine skill category
        if not skill_info.get("prerequisites"):
            return "Basic Skills"
        elif skill_info["effect"] == "Attack":
            if "fire" in skill_name.lower() or "flame" in skill_name.lower() or "inferno" in skill_name.lower():
                return "Fire Magic"
            elif "ice" in skill_name.lower() or "frost" in skill_name.lower() or "blizzard" in skill_name.lower():
                return "Ice Magic"
            else:
                return "Combat Skills"
        elif skill_info["effect"] == "Health":
            return "Healing Skills"
        elif skill_info["effect"] == "Defense":
            return "Defensive Skills"
        return "Special Skills"
    
    categories = {}
    for skill_name, skill_info in saved_skills.items():
        category = get_category(skill_name, skill_info)
        if category not in categories:
            categories[category] = []
        categories[category].append(skill_name)
    
    return categories


def attempt_add_skill(character, selected_skill, saved_skills):
    # Attempt to add a skill to character with validation
    skill_info = saved_skills[selected_skill]
    
    # Check if already has skill
    if selected_skill in character["skills"]:
        print(f"{selected_skill} is already in {character['name']}'s skills!")
        input("Press Enter to continue...")
        return
    
    # Validate prerequisites
    prereq_check = validate_prerequisites(character, skill_info, saved_skills)
    if not prereq_check["valid"]:
        print(f"\nCannot add {selected_skill}!")
        print(f"Missing prerequisites: {', '.join(prereq_check['missing'])}")
        if prereq_check["low_level_prereqs"]:
            print(f"Insufficient prerequisite levels: {', '.join(prereq_check['low_level_prereqs'])}")
        input("Press Enter to continue...")
        return
    
    # Check level requirement
    if character.get("level", 1) < skill_info.get("level_requirement", 1):
        print(f"\nCannot add {selected_skill}!")
        print(f"Character level {character.get('level', 1)} is too low. Required level: {skill_info['level_requirement']}")
        input("Press Enter to continue...")
        return
    
    # Add the skill
    character["skills"].add(selected_skill)
    character["skill_levels"][selected_skill] = 1
    print(f"Added {selected_skill} to {character['name']} at level 1!")
    input("Press Enter to continue...")


def validate_prerequisites(character, skill_info, saved_skills):
    # Validate all prerequisites for a skill
    
    def check_single_prereq(prereq):
        # Inner function to check a single prerequisite
        if prereq not in character["skills"]:
            return {"valid": False, "reason": "not_learned"}
        
        prereq_info = saved_skills.get(prereq, {})
        min_level = prereq_info.get("min_prerequisite_level", 1)
        current_level = character.get("skill_levels", {}).get(prereq, 0)
        
        if current_level < min_level:
            return {"valid": False, "reason": "low_level", "required": min_level, "current": current_level}
        
        return {"valid": True}
    
    result = {
        "valid": True,
        "missing": [],
        "low_level_prereqs": []
    }
    
    prerequisites = skill_info.get("prerequisites", [])
    if not prerequisites:
        return result
    
    for prereq in prerequisites:
        check = check_single_prereq(prereq)
        if not check["valid"]:
            result["valid"] = False
            if check["reason"] == "not_learned":
                result["missing"].append(prereq)
            elif check["reason"] == "low_level":
                result["low_level_prereqs"].append(f"{prereq} (Lv {check['current']}/{check['required']})")
    
    return result


def handle_level_up_skill(saved_skills, character):
    # Level up a skill to improve its effectiveness
    if not character["skills"]:
        print("No skills to level up!")
        input("Press Enter to continue...")
        return
    
    initialize_skill_levels(character)
    
    skill_list = list(character["skills"])
    
    # Show skills with their current levels and upgrade costs
    skill_display = []
    for skill in skill_list:
        level = character['skill_levels'].get(skill, 1)
        max_level = saved_skills.get(skill, {}).get("max_level", 10)
        skill_display.append(f"{skill} (Lv {level}/{max_level})")
    skill_display.append("Return")
    
    result = menu(skill_display)
    selected = result['index']
    
    if selected < len(skill_list):
        skill_name = skill_list[selected]
        perform_skill_levelup(character, skill_name, saved_skills)


def perform_skill_levelup(character, skill_name, saved_skills):
    # Perform the actual skill level up with calculations
    
    def calculate_stat_increase(base_amount, current_level):
        # Inner function to calculate stat increase per level
        return base_amount * 0.1 * current_level
    
    current_level = character["skill_levels"].get(skill_name, 1)
    skill_info = saved_skills.get(skill_name, {})
    max_level = skill_info.get("max_level", 10)
    
    if current_level >= max_level:
        print(f"{skill_name} is already at max level ({max_level})!")
        input("Press Enter to continue...")
        return
    
    # Level up the skill
    new_level = current_level + 1
    character["skill_levels"][skill_name] = new_level
    
    # Calculate and display improvements
    base_amount = skill_info.get("amount", 0)
    old_amount = base_amount + calculate_stat_increase(base_amount, current_level - 1)
    new_amount = base_amount + calculate_stat_increase(base_amount, new_level - 1)
    
    print(f"\n{'='*50}")
    print(f"SKILL LEVEL UP!")
    print(f"{'='*50}")
    print(f"{skill_name}: Level {current_level} → Level {new_level}")
    print(f"Effect strength: {old_amount:.1f} → {new_amount:.1f}")
    print(f"Improvement: +{new_amount - old_amount:.1f}")
    print(f"{'='*50}")
    input("\nPress Enter to continue...")


def handle_view_skill_tree(saved_skills, character):
    # Display available skills and their prerequisites in a tree structure
    
    def build_dependency_map():
        # Inner function to build skill dependency relationships
        root_skills = []
        dependent_skills = {}
        
        for skill_name, skill_info in saved_skills.items():
            prereqs = skill_info.get("prerequisites", [])
            if not prereqs:
                root_skills.append(skill_name)
            else:
                for prereq in prereqs:
                    if prereq not in dependent_skills:
                        dependent_skills[prereq] = []
                    if skill_name not in dependent_skills[prereq]:
                        dependent_skills[prereq].append(skill_name)
        
        return root_skills, dependent_skills
    
    import os
    os.system('cls')
    
    print("\n" + "="*80)
    print(" "*25 + "SKILL TREE OVERVIEW")
    print("="*80)
    
    # Show legend first
    print("\nLEGEND:")
    print("  ✓ = You have this skill")
    print("  ○ = Available to learn now")
    print("  ● = Locked (need prerequisites)")
    print("  ⚠ = Locked (character level too low)")
    print("\n" + "-"*80)
    
    root_skills, dependent_skills = build_dependency_map()
    
    # Organize skills by category for cleaner display
    categories = {
        "Basic": [],
        "Fire Magic": [],
        "Ice Magic": [],
        "Healing": [],
        "Defense": [],
        "Combat": [],
        "Support": [],
        "Ultimate": []
    }
    
    for skill_name, skill_info in saved_skills.items():
        desc = skill_info.get("description", "").lower()
        name = skill_name.lower()
        prereqs = skill_info.get("prerequisites", [])
        
        if not prereqs:
            categories["Basic"].append(skill_name)
        elif "fire" in name or "flame" in name or "inferno" in name or "spark" in name or "phoenix" in name:
            categories["Fire Magic"].append(skill_name)
        elif "ice" in name or "frost" in name or "blizzard" in name or "zero" in name:
            categories["Ice Magic"].append(skill_name)
        elif "heal" in name or "resurrection" in name:
            categories["Healing"].append(skill_name)
        elif "shield" in name or "fortress" in name or "guardian" in name or "iron skin" in name:
            categories["Defense"].append(skill_name)
        elif "strike" in name or "cleave" in name or "berserker" in name:
            categories["Combat"].append(skill_name)
        elif "focus" in name or "battle cry" in name or "blessing" in name:
            categories["Support"].append(skill_name)
        elif len(prereqs) >= 3:  # Ultimate skills have multiple prereqs
            categories["Ultimate"].append(skill_name)
    
    # Display each category
    for category, skills in categories.items():
        if not skills:
            continue
            
        print(f"\n┌─ {category.upper()}")
        for i, skill_name in enumerate(sorted(skills)):
            is_last = (i == len(skills) - 1)
            display_skill_in_tree(skill_name, saved_skills, character, dependent_skills, is_last)
    
    print("\n" + "="*80)
    input("\nPress Enter to return to skill menu...")


def display_skill_in_tree(skill_name, saved_skills, character, dependent_skills, is_last_in_category):
    # Display a single skill in the tree with better formatting
    
    def get_skill_status_symbol(skill_name, skill_info, character):
        # Get the status symbol for a skill
        if skill_name in character.get("skills", set()):
            level = character.get("skill_levels", {}).get(skill_name, 1)
            max_level = skill_info.get("max_level", 10)
            return "✓", f"Lv{level}/{max_level}"
        
        prereq_check = validate_prerequisites(character, skill_info, saved_skills)
        char_level = character.get("level", 1)
        req_level = skill_info.get("level_requirement", 1)
        
        if char_level < req_level:
            return "⚠", f"Need Lv{req_level}"
        elif not prereq_check["valid"]:
            return "●", "Locked"
        else:
            return "○", "Available"
    
    skill_info = saved_skills.get(skill_name, {})
    symbol, status = get_skill_status_symbol(skill_name, skill_info, character)
    
    # Get skill stats
    effect = skill_info.get("effect", "?")
    amount = skill_info.get("amount", 0)
    target = skill_info.get("target", "?")
    
    # Main skill line
    branch = "└─" if is_last_in_category else "├─"
    print(f"│ {branch} {symbol} {skill_name:<20} [{effect}: {amount} → {target}] ({status})")
    
    # Show prerequisites if any
    prereqs = skill_info.get("prerequisites", [])
    if prereqs:
        continuation = "  " if is_last_in_category else "│ "
        prereq_str = " + ".join(prereqs)
        print(f"│ {continuation}   └─ Requires: {prereq_str}")
    
    # Show what this unlocks (only for unlocked skills)
    if skill_name in character.get("skills", set()) and skill_name in dependent_skills:
        continuation = "  " if is_last_in_category else "│ "
        unlocks = ", ".join(dependent_skills[skill_name][:3])
        if len(dependent_skills[skill_name]) > 3:
            unlocks += f" +{len(dependent_skills[skill_name]) - 3} more"
        print(f"│ {continuation}   └─ Unlocks: {unlocks}")


def handle_view_skills(saved_skills, character):
    # View all of character's current skills with detailed information
    import os
    os.system('cls')
    
    print("\n" + "="*80)
    print(f" "*25 + f"{character['name'].upper()}'S SKILLS")
    print("="*80)
    
    if character["skills"]:
        initialize_skill_levels(character)
        
        # Organize skills by category for better viewing
        categorized = {}
        for skill_name in character["skills"]:
            skill_info = saved_skills.get(skill_name, {})
            effect = skill_info.get("effect", "Other")
            if effect not in categorized:
                categorized[effect] = []
            categorized[effect].append(skill_name)
        
        # Display skills by category
        for category in sorted(categorized.keys()):
            print(f"\n┌─ {category.upper()} SKILLS")
            skills_in_cat = sorted(categorized[category])
            for i, skill_name in enumerate(skills_in_cat):
                is_last = (i == len(skills_in_cat) - 1)
                display_owned_skill_info(saved_skills, skill_name, character, is_last)
            print("│")
    else:
        print("\n  No skills learned yet!")
        print("  Visit 'Add Skill' to learn your first skill.")
    
    print("="*80)
    input("\nPress Enter to continue...")


def display_owned_skill_info(saved_skills, skill_name, character, is_last):
    # Display detailed information about a skill the character owns
    skill_info = saved_skills.get(skill_name, {})
    skill_level = character.get("skill_levels", {}).get(skill_name, 1)
    max_level = skill_info.get("max_level", 10)
    
    # Calculate level-adjusted amount
    base_amount = skill_info.get("amount", 0)
    adjusted_amount = base_amount + (skill_level - 1) * (base_amount * 0.1)
    
    branch = "└─" if is_last else "├─"
    continuation = "  " if is_last else "│ "
    
    # Skill name and level
    print(f"│ {branch} {skill_name} [Level {skill_level}/{max_level}]")
    
    # Description
    desc = skill_info.get('description', 'N/A')
    print(f"│ {continuation}   • {desc}")
    
    # Stats
    effect = skill_info.get('effect', 'N/A')
    target = skill_info.get('target', 'N/A')
    print(f"│ {continuation}   • Power: {adjusted_amount:.1f} (Base: {base_amount}) | {effect} → {target}")
    
    # Level progress bar
    if skill_level < max_level:
        progress = int((skill_level / max_level) * 20)
        bar = "█" * progress + "░" * (20 - progress)
        print(f"│ {continuation}   • Progress: [{bar}] {skill_level}/{max_level}")
    else:
        print(f"│ {continuation}   • ⭐ MAX LEVEL ⭐")


def handle_level_up_skill(saved_skills, character):
    # Level up a skill to improve its effectiveness
    if not character["skills"]:
        print("No skills to level up!")
        input("Press Enter to continue...")
        return
    
    initialize_skill_levels(character)
    
    skill_list = sorted(list(character["skills"]))
    
    # Show skills with their current levels and upgrade info
    skill_display = []
    for skill in skill_list:
        level = character['skill_levels'].get(skill, 1)
        max_level = saved_skills.get(skill, {}).get("max_level", 10)
        
        if level >= max_level:
            skill_display.append(f"{skill} (Lv {level}/{max_level}) [MAX]")
        else:
            skill_display.append(f"{skill} (Lv {level}/{max_level})")
    
    skill_display.append("Return")
    
    result = menu(skill_display)
    selected = result['index']
    
    if selected < len(skill_list):
        skill_name = skill_list[selected]
        perform_skill_levelup(character, skill_name, saved_skills)


def perform_skill_levelup(character, skill_name, saved_skills):
    # Perform the actual skill level up with calculations
    import os
    
    def calculate_stat_increase(base_amount, current_level):
        # Inner function to calculate stat increase per level
        return base_amount * 0.1 * current_level
    
    current_level = character["skill_levels"].get(skill_name, 1)
    skill_info = saved_skills.get(skill_name, {})
    max_level = skill_info.get("max_level", 10)
    
    if current_level >= max_level:
        print(f"\n{skill_name} is already at max level ({max_level})!")
        input("Press Enter to continue...")
        return
    
    # Level up the skill
    new_level = current_level + 1
    character["skill_levels"][skill_name] = new_level
    
    # Calculate and display improvements
    base_amount = skill_info.get("amount", 0)
    old_amount = base_amount + calculate_stat_increase(base_amount, current_level - 1)
    new_amount = base_amount + calculate_stat_increase(base_amount, new_level - 1)
    
    os.system('cls')
    print("\n" + "="*60)
    print(" "*20 + "⚔ SKILL LEVEL UP! ⚔")
    print("="*60)
    print(f"\n  {skill_name}")
    print(f"\n  Level: {current_level} ──→ {new_level}")
    print(f"  Power: {old_amount:.1f} ──→ {new_amount:.1f} (+{new_amount - old_amount:.1f})")
    
    if new_level == max_level:
        print(f"\n  ⭐ MAXIMUM LEVEL ACHIEVED! ⭐")
    
    print("\n" + "="*60)
    input("\nPress Enter to continue...")


def display_skill_node(skill_name, saved_skills, character, dependent_skills, indent=0):
    # Recursively display a skill and its dependents
    
    def get_skill_status(skill_name, skill_info, character):
        # Inner function to determine skill status symbol
        if skill_name in character.get("skills", set()):
            return "✓", f" [Lv {character.get('skill_levels', {}).get(skill_name, 1)}]"
        
        prereq_check = validate_prerequisites(character, skill_info, saved_skills)
        
        if character.get("level", 1) < skill_info.get("level_requirement", 1):
            return "⚠", f" [Req: Char Lv {skill_info.get('level_requirement', 1)}]"
        elif not prereq_check["valid"] and prereq_check["low_level_prereqs"]:
            return "⊗", f" [Low Prereq Levels]"
        elif not prereq_check["valid"]:
            return "✗", f" [Missing: {', '.join(prereq_check['missing'][:2])}]"
        else:
            return "✓", " [Available]"
    
    skill_info = saved_skills.get(skill_name, {})
    status, level_info = get_skill_status(skill_name, skill_info, character)
    
    # Print the skill
    prefix = "  " * indent + "├─ "
    effect = skill_info.get("effect", "?")
    amount = skill_info.get("amount", 0)
    print(f"{prefix}{status} {skill_name}{level_info} ({effect}: {amount})")
    
    # Show prerequisites if any
    if "prerequisites" in skill_info and skill_info["prerequisites"]:
        prereq_str = ", ".join(skill_info["prerequisites"])
        print(f"{'  ' * (indent + 1)}  └─ Requires: {prereq_str}")
    
    # Recursively display dependent skills
    if skill_name in dependent_skills:
        for dependent in sorted(dependent_skills[skill_name]):
            display_skill_node(dependent, saved_skills, character, dependent_skills, indent + 1)


def edit_existing_skill(saved_skills, character):
    # Edit an existing skill in the character's skill list
    if not character["skills"]:
        print("No skills to edit!")
        input("Press Enter to continue...")
        return
        
    skill_list = list(character["skills"])
    edit_result = menu([*skill_list, "Return"])
    selected = edit_result['index']
    
    if selected < len(skill_list):
        skill_to_edit = skill_list[selected]
        skill_info = saved_skills.get(skill_to_edit, {})
        
        skill_data = get_skill_data_from_menu(skill_info)
        
        if skill_data['index'] == 7:  # Save Changes index
            update_skill(saved_skills, character, skill_to_edit, skill_info, skill_data)


def get_skill_data_from_menu(skill_info=None):
    # Get skill data with prerequisites and level requirements
    if skill_info is None:
        skill_info = {}
    
    return menu(
        ["Skill Name", "Skill Description", "Skill Effect", "Effect Strength", 
         "Skill Target", "Level Requirement", "Max Skill Level", "Save Changes", "Return"],
        writable=[0, 1],
        toggle=[2, 4],
        tog_opts=[["Attack", "Defense", "Health"], [["Enemy", "Self", "Ally"], [4]]],
        number=[3, 5, 6],
        num_min=1,
        num_max=100
    )


def update_skill(saved_skills, character, skill_to_edit, skill_info, skill_data):
    # Update a skill's properties
    new_name = ''.join(skill_data['writable'][0]) or skill_to_edit
    new_desc = ''.join(skill_data['writable'][1]) or skill_info.get("description", "")
    
    updated_skill = {
        "description": new_desc,
        "effect": skill_data['toggles'][2],
        "amount": skill_data['numbers'][3],
        "target": skill_data['toggles'][4],
        "level_requirement": skill_data['numbers'][5],
        "max_level": skill_data['numbers'][6],
        "prerequisites": skill_info.get("prerequisites", [])
    }
    
    saved_skills[new_name] = updated_skill
    
    if new_name != skill_to_edit:
        character["skills"].remove(skill_to_edit)
        if skill_to_edit in saved_skills:
            del saved_skills[skill_to_edit]
        if "skill_levels" in character and skill_to_edit in character["skill_levels"]:
            character["skill_levels"][new_name] = character["skill_levels"][skill_to_edit]
            del character["skill_levels"][skill_to_edit]
    
    character["skills"].add(new_name)
    print("Skill updated!")
    input("Press Enter to continue...")


def add_new_skill(saved_skills, character):
    # Create and add a completely new skill
    skill_data = menu(
        ["Skill Name", "Skill Description", "Skill Effect", "Effect Strength", 
         "Skill Target", "Level Requirement", "Max Skill Level", "Save Skill", "Return"],
        writable=[0, 1],
        toggle=[2, 4],
        tog_opts=[["Attack", "Defense", "Health"], [["Enemy", "Self", "Ally"], [4]]],
        number=[3, 5, 6],
        num_min=1,
        num_max=100
    )
    
    if skill_data['index'] == 7:  # Save Skill
        skill_name = ''.join(skill_data['writable'][0])
        skill_desc = ''.join(skill_data['writable'][1])
        
        if skill_name:
            new_skill = create_skill_dict(skill_data, skill_desc)
            
            # Ask for prerequisites
            prereqs = get_prerequisites(saved_skills, skill_name)
            new_skill["prerequisites"] = prereqs
            
            saved_skills[skill_name] = new_skill
            
            # Check if character can add this skill
            prereq_check = validate_prerequisites(character, new_skill, saved_skills)
            if prereq_check["valid"] and character.get("level", 1) >= new_skill["level_requirement"]:
                character["skills"].add(skill_name)
                initialize_skill_levels(character)
                character["skill_levels"][skill_name] = 1
                print(f"Created and added {skill_name} to {character['name']}!")
            else:
                print(f"Created {skill_name} but prerequisites/level requirements not met to add to character.")
        else:
            print("Skill name cannot be empty!")
        input("Press Enter to continue...")


def get_prerequisites(saved_skills, current_skill_name):
    # Let user select prerequisite skills
    if not saved_skills:
        return []
    
    print("\nSelect prerequisite skills (skills that must be learned first)")
    print("This skill cannot be its own prerequisite!")
    
    available_skills = [s for s in saved_skills.keys() if s != current_skill_name]
    if not available_skills:
        print("No available skills for prerequisites.")
        input("Press Enter to continue...")
        return []
    
    selected_prereqs = []
    
    while True:
        display_list = available_skills.copy()
        display_list.append("Done - No more prerequisites")
        
        result = menu(display_list)
        selected = result['index']
        
        if selected >= len(available_skills):
            break
        
        prereq_skill = available_skills[selected]
        selected_prereqs.append(prereq_skill)
        available_skills.remove(prereq_skill)
        print(f"Added {prereq_skill} as a prerequisite.")
        
        if not available_skills:
            break
    
    return selected_prereqs


def create_skill_dict(skill_data, skill_desc):
    # Create a skill dictionary from menu data
    return {
        "description": skill_desc,
        "effect": skill_data['toggles'][2],
        "amount": skill_data['numbers'][3],
        "target": skill_data['toggles'][4],
        "level_requirement": skill_data['numbers'][5],
        "max_level": skill_data['numbers'][6],
        "prerequisites": []
    }


def handle_remove_skill(character, saved_skills):
    # Remove a skill from character with dependency checking
    
    def check_dependents(skill_to_remove, character, saved_skills):
        # Inner function to check if other skills depend on this one
        dependents = []
        for skill in character["skills"]:
            if skill == skill_to_remove:
                continue
            skill_info = saved_skills.get(skill, {})
            if skill_to_remove in skill_info.get("prerequisites", []):
                dependents.append(skill)
        return dependents
    
    if not character["skills"]:
        print("No skills to remove!")
        input("Press Enter to continue...")
        return
    
    skill_list = list(character["skills"])
    result = menu([*skill_list, "Return"])
    selected = result['index']
    
    if selected < len(skill_list):
        removed_skill = skill_list[selected]
        
        # Check if other skills depend on this one
        dependents = check_dependents(removed_skill, character, saved_skills)
        if dependents:
            print(f"\nWarning! The following skills require {removed_skill}:")
            for dep in dependents:
                print(f"  - {dep}")
            print("\nRemoving this skill will also remove all dependent skills.")
            confirm = input("Continue? (y/n): ").strip().lower()
            if confirm != 'y':
                return
            
            # Remove all dependent skills
            for dep in dependents:
                character["skills"].remove(dep)
                if "skill_levels" in character and dep in character["skill_levels"]:
                    del character["skill_levels"][dep]
        
        # Remove the skill
        character["skills"].remove(removed_skill)
        if "skill_levels" in character and removed_skill in character["skill_levels"]:
            del character["skill_levels"][removed_skill]
        
        print(f"Removed {removed_skill} from {character['name']}!")
        if dependents:
            print(f"Also removed: {', '.join(dependents)}")
        input("Press Enter to continue...")


def handle_view_skills(saved_skills, character):
    # View all of character's current skills with detailed information
    print(f"\n{'='*70}")
    print(f"{character['name']}'s Skills")
    print(f"{'='*70}")
    
    if character["skills"]:
        initialize_skill_levels(character)
        
        # Organize skills by category for better viewing
        categorized = {}
        for skill_name in character["skills"]:
            skill_info = saved_skills.get(skill_name, {})
            effect = skill_info.get("effect", "Other")
            if effect not in categorized:
                categorized[effect] = []
            categorized[effect].append(skill_name)
        
        # Display skills by category
        for category in sorted(categorized.keys()):
            print(f"\n[{category} Skills]")
            for skill_name in sorted(categorized[category]):
                display_skill_info(saved_skills, skill_name, character)
    else:
        print("  No skills yet!")
    
    print(f"\n{'='*70}")
    input("\nPress Enter to continue...")


def display_skill_info(saved_skills, skill_name, character):
    # Display detailed information about a specific skill
    skill_info = saved_skills.get(skill_name, {})
    skill_level = character.get("skill_levels", {}).get(skill_name, 1)
    max_level = skill_info.get("max_level", 10)
    
    # Calculate level-adjusted amount
    base_amount = skill_info.get("amount", 0)
    adjusted_amount = base_amount + (skill_level - 1) * (base_amount * 0.1)
    
    print(f"\n  ◆ {skill_name} [Level {skill_level}/{max_level}]")
    print(f"    Description: {skill_info.get('description', 'N/A')}")
    print(f"    Effect Type: {skill_info.get('effect', 'N/A')}")
    print(f"    Power: {adjusted_amount:.1f} (Base: {base_amount})")
    print(f"    Target: {skill_info.get('target', 'N/A')}")
    
    if "prerequisites" in skill_info and skill_info["prerequisites"]:
        print(f"    Required Skills: {', '.join(skill_info['prerequisites'])}")
    
    if "level_requirement" in skill_info:
        print(f"    Minimum Level: {skill_info['level_requirement']}")