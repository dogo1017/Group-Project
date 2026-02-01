def view_menu(characters, selected_character):
    import selecter
    compare_character = selecter.selecter(characters, compare=True)
    print(f"{compare_character['name']} vs {selected_character['name']}")
    # DO THIS
    input("Press Enter to continue...")
    return characters, selected_character