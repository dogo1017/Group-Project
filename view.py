def view_menu(characters, selected_character, classes, races, items):
    import selecter
    import os

    def apply_multipliers(attributes, source):
        for i, key in enumerate(["dmg", "dex", "int", "con", "cha"]):
            if key in source:
                attributes[i] *= source[key]

    chosen_names = [selected_character]
    while len(chosen_names) < len(characters):
        os.system('cls')
        print(f"Characters selected so far: {', '.join(chosen_names)}")
        print(f"\nAdd another character to compare? (you have {len(characters) - len(chosen_names)} remaining)")
        print("1. Yes")
        print("2. No, show me the comparison")
        choice = input("Choose an option: ").strip()
        if choice != "1":
            break
        result = selecter.selecter(characters)
        if result is None:
            continue
        new_char, characters = result
        new_name = new_char["name"]
        if new_name in chosen_names:
            print(f"'{new_name}' is already selected!")
            input("Press Enter to continue...")
            continue
        chosen_names.append(new_name)

    chosen = []
    for name in chosen_names:
        match = next((c for c in characters if isinstance(c, dict) and c["name"] == name), None)
        if match:
            chosen.append(match)

    for c in chosen:
        c["attributes"] = c["base_attributes"].copy()
        for item_name in c["inventory"]:
            item = next((i for i in items if i["name"] == item_name), None)
            if item:
                apply_multipliers(c["attributes"], item)
        race_data = next((r for r in races if r["name"] == c["race"]), None)
        if race_data:
            apply_multipliers(c["attributes"], race_data)
        class_data = next((cl for cl in classes if cl["name"] == c["class"]), None)
        if class_data:
            apply_multipliers(c["attributes"], class_data)

    os.system('cls')
    title = "  VS  ".join(c["name"] for c in chosen)
    print("=" * len(title))
    print(title)
    print("=" * len(title))
    print()
    col_width = max(len(c["name"]) for c in chosen) + 4

    print("ATTRIBUTES")
    print("-" * (15 + col_width * len(chosen)))
    header = f"{'Stats':<15}" + "".join(f"{c['name']:<{col_width}}" for c in chosen)
    print(header)
    print("-" * (15 + col_width * len(chosen)))
    for i, label in enumerate(["Damage", "Dexterity", "Intelligence", "Constitution", "Charisma"]):
        row = f"{label:<15}" + "".join(f"{round(c['attributes'][i], 2):<{col_width}}" for c in chosen)
        print(row)

    print("\nSKILLS")
    print("-" * (15 + col_width * len(chosen)))
    for c in chosen:
        skills_str = ", ".join(c["skills"]) if c["skills"] else "None"
        print(f"{c['name']}: {skills_str}")

    print("\nINVENTORY")
    print("-" * (15 + col_width * len(chosen)))
    for c in chosen:
        if c["inventory"]:
            inv_items = []
            total_weight = 0
            total_value = 0
            for item in c["inventory"]:
                item_name = item.get("name", "Unknown") if isinstance(item, dict) else item
                inv_items.append(item_name)
                if isinstance(item, dict):
                    if "weight" in item:
                        total_weight += item["weight"]
                    if "value" in item:
                        total_value += item["value"]
            inv_str = ", ".join(inv_items)
            print(f"{c['name']}: {inv_str}")
            print(f"  Total Weight: {total_weight} lbs | Total Value: {total_value} gold")
        else:
            print(f"{c['name']}: None")

    print("\n" + "=" * (15 + col_width * len(chosen)))
    input("Press Enter to continue...")
    return characters, selected_character