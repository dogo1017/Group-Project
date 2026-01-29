from menu import menu

def add_skill(existing_skills):
    result = menu(["Add Existing Skill", "Edit Existing Skill", "Add New Skill", "Return"])
    result = result['index']
    if result == 0:
        menu([*existing_skills, "return"])
    if result == 1:
        menu([*existing_skills, "return"])
    if result == 2:
        skill_index = menu(["Skill Name", "Skill Description", "Skill effect", "Effect amount", "Skill Target", "return"], writable = [0,1], toggle = [2,4], tog_opts = [["Attack", "Defense", "Health"]], number = [3])
        skill_index = skill_index['index']

def remove_skill():
    pass

def skill_menu():
    skill_manage = 1
    while skill_manage == 1:
        result = menu(["Add Skill", "Remove Skill", "Return"])
        selected_index = result['index']
        if selected_index == 0:
            add_skill([1, 2, 3, 4, 5, "hi"])
        elif selected_index == 1:
            remove_skill()
        else:
            skill_manage = 0

skill_menu()