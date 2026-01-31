def compare_menu(characters, selected_character):
    import select
    compare_character = select.search(characters, compare=True)
    print(f"{compare_character['name']} vs {selected_character['name']}")
    # DO THIS
    input("Press Enter to continue...")
    return characters, selected_character