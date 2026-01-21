def add_skill():
    pass
def remove_skill():
    pass
def skill_menu():
    from main import menu
    choice = menu(["Add Skill", "Remove Skill", "Return"])
    if choice == 1:
        add_skill()
    elif choice == 2:
        remove_skill()

    