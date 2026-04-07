def selecter(characters):
    keyword = input("What keyword would you like to search for: ").strip().lower()
    pulled = []
    for character in characters:
        if any(keyword in str(value).lower() for value in character.values()):
            pulled.append(character)
            print(f"{len(pulled)}. {character['name']}")
    if not pulled:
        print("No character was found.")
        again = input("Would you like to repeat the search? (y/n): ").strip().lower()
        if again in ("yes", "y"):
            return selecter(characters)
        return None
    while True:
        try:
            choice = int(input("Input the number of the character you would like to choose: "))
            selected = pulled[choice - 1]
            break
        except :
            print("Invalid choice. Try again.")
    print("You have selected a character. ")
    input("Press Enter to continue...")
    return selected, characters

def selecter_menu(characters, selected_character):
    import os
    os.system('cls')
    selected, characters = selecter(characters)
    if selected is None:
        return characters, selected_character
    selected_character = selected["name"]
    return characters, selected_character
