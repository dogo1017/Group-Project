#DU p1 

from menu import menu

def attribute_menu(characters, selected_character):
    while True:
        attribute_options = list(selected_character.keys()) + ["Return to Main"]
        attribute_choice = menu(f"Select attribute to modify for {selected_character}:", attribute_options)
        if attribute_choice == "Return to Main":
            return
        confirm_modify = menu(f"Are you sure you want to modify {attribute_choice}?", ["Yes", "No"])
        if confirm_modify == "No":
            manage_again = menu("Would you like to manage different attributes?", ["Yes", "No"])
            if manage_again == "Yes":
                continue  
            return selected_character, characters
        current_value = characters[selected_character][attribute_choice]
        change_options = [f"Enter new value (Current: {current_value})", "Return to attribute selection"]
        change_choice = menu(f"Modify {attribute_choice}:", change_options)
        if change_choice == "Return to attribute selection":
            continue  
        while True:
            try:
                new_value_input = input(f"Enter new value for {attribute_choice}: ")
                if isinstance(current_value, int):
                    new_value = int(new_value_input)
                elif isinstance(current_value, float):
                    new_value = float(new_value_input)
                else:
                    new_value = new_value_input
                break
            except:
                print(f"Invalid input. Please enter {'an integer' if isinstance(current_value, int) else 'a number' if isinstance(current_value, float) else 'a value'}.")
        confirm_change = menu(f"Change {attribute_choice} from {current_value} to {new_value}?", ["Yes", "No"])
        if confirm_change == "No":
            continue  
        characters[selected_character][attribute_choice] = new_value
        print(f"{attribute_choice} updated to {new_value}")
        change_more = menu("Would you like to change more attributes?", ["Yes", "No (Return to Main)"])
        if change_more == "Yes":
            continue  
        else:
            return selected_character, characters