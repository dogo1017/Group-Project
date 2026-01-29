from menu import menu

def compare(selected_character, characters):
    compare_character = search(characters=characters, comp=True)
    print(f"{compare_character["name"]} vs {selected_character["name"]}") #FINISH THIS
    while True:
        exit = input("Would you like to return? ").strip().lower()
        if exit == "yes" or exit == "y":
            return characters, selected_character

def search(comp, characters):
    keyword = input("What would you like to search for: ")
    count = 0
    pulled = []
    for character in characters:
        if keyword in character:
            print() # FINISH THIS
            pulled.append(character)
            count += 1   
    if count == 0:
        print("No character was found.")
        again = input("Would you like to repeat the search? ")
        if again == "yes":    
            search(comp, characters)
        else:
            return
    else:
        choice = input("Input the number of the character you would like to choose: ")
        if comp == True:
            compare_character = pulled[choice-1]
            return compare_character
        else:
            selected_character = pulled[choice-1]
            return selected_character, characters

def search_menu(characters, selected_character, comp):
    if comp == True:
        characters, selected_character = compare(selected_character, characters)
    else:
        characters, selected_character = search(characters=characters, comp=False)
    return characters, selected_character

#define search_menu function with parameters characters, selected_character, compare
#- if compare = True
#    - call compare function
#- else:
#    - call search function with compare equal to False
#
#define compare function with parameters selected_character and characters
#- call search function with compare equal to True
#- print compare_character and selected_character
#- always loop
#    - ask if user would like to return
#    - if yes
#        - return to main

#define search function with parameters characters, compare
#- ask user for input
#- set count equal to 0 
#- for every character in characters
#    - if input is anywhere in their dictionary
#        - print each character with an index + 1
#        - increase count by 1
#- if count is still 0
#    - tell user there was no character found
#    - ask if they would like to search again
#    - if yes
#        - call search
#    - if no
#        - return to main
#- else
#    - ask user to choose one of the pulled up characters
#    - if compare is equal to True
#        - set compare_character to chosen character
#        - return compare_character
#    - else:
#        - set selected_character to chosen character
#       - return selected_character