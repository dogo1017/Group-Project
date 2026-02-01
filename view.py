def view_menu(characters, selected_character):
    import selecter
    import os

    labels = ["Damage", "Dexterity", "Intelligence", "Constitution", "Charisma"]

    # Start with the currently selected character
    chosen_names = [selected_character]

    # Keep asking for more characters until they stop or all are picked
    while len(chosen_names) < len(characters):
        os.system('cls')
        print(f"Characters selected so far: {', '.join(chosen_names)}")
        print(f"\nAdd another character to compare? (you have {len(characters) - len(chosen_names)} remaining)")
        print("1. Yes")
        print("2. No, show me the comparison")
        choice = input("Choose an option: ").strip()

        if choice != "1":
            break

        characters, new_name = selecter.search_menu(characters, selected_character)

        if new_name in chosen_names:
            print(f"'{new_name}' is already selected!")
            input("Press Enter to continue...")
            continue

        chosen_names.append(new_name)

    # Resolve all chosen names into character dicts
    chosen = [next(c for c in characters if c["name"] == name) for name in chosen_names]

    # --- DISPLAY ---
    os.system('cls')

    # Build the title
    title = "  VS  ".join(c["name"] for c in chosen)
    print("=" * len(title))
    print(title)
    print("=" * len(title))
    print()

    # Figure out column widths based on the longest name in each column
    col_width = max(len(c["name"]) for c in chosen) + 4

    # Attributes table
    print("ATTRIBUTES")
    print("-" * (15 + col_width * len(chosen)))
    header = f"{'Stat':<15}" + "".join(f"{c['name']:<{col_width}}" for c in chosen)
    print(header)
    print("-" * (15 + col_width * len(chosen)))

    for i, label in enumerate(labels):
        row = f"{label:<15}" + "".join(f"{round(c['attributes'][i], 2):<{col_width}}" for c in chosen)
        print(row)

    # Skills
    print("\nSKILLS")
    print("-" * (15 + col_width * len(chosen)))
    for c in chosen:
        skills_str = ", ".join(c["skills"]) if c["skills"] else "None"
        print(f"{c['name']}: {skills_str}")

    # Inventory
    print("\nINVENTORY")
    print("-" * (15 + col_width * len(chosen)))
    for c in chosen:
        inv_str = ", ".join(c["inventory"]) if c["inventory"] else "None"
        print(f"{c['name']}: {inv_str}")

    print("\n" + "=" * (15 + col_width * len(chosen)))
    input("Press Enter to continue...")
    return characters, selected_character