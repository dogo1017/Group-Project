def compare(selected_character, characters):
    compare_character = search(characters, boolean=True)
    if not compare_character:
        return characters, selected_character
    print(f"{compare_character['name']} vs {selected_character['name']}")
    while True:
        exit_choice = input("Would you like to return? (y/n): ").strip().lower()
        if exit_choice in ("yes", "y"):
            return characters, selected_character


def search(characters, boolean):
    keyword = input("What would you like to search for: ").strip().lower()
    pulled = []
    for character in characters:
        # search through all values in the dictionary
        if any(keyword in str(value).lower() for value in character.values()):
            pulled.append(character)
            print(f"{len(pulled)}. {character['name']}")
    if not pulled:
        print("No character was found.")
        again = input("Would you like to repeat the search? (y/n): ").strip().lower()
        if again in ("yes", "y"):
            return search(characters, boolean)
        return None
    while True:
        try:
            choice = int(input("Input the number of the character you would like to choose: "))
            selected = pulled[choice - 1]
            break
        except :
            print("Invalid choice. Try again.")
    print("You have selected a character. ")
    if boolean:
        return selected
    else:
        return selected, characters

def search_menu(characters, selected_character, comp):
    import os
    os.system('cls')
    if comp:
        characters, selected_character = compare(selected_character, characters)
    else:
        result = search(characters, boolean=False)
        if result:
            selected_character, characters = result
    return characters, selected_character
