#DU p1 

from menu import menu

def attribute_manager(characters, selected_character):
    # Use a while loop instead of recursive calls
    while True:
        # Step 1: Select attribute to modify or return to main
        attribute_options = list(characters[selected_character].keys()) + ["Return to Main"]
        attribute_choice = menu(f"Select attribute to modify for {selected_character}:", attribute_options)
        
        # If return to main selected
        if attribute_choice == "Return to Main":
            return
        
        # Step 2: Ask if sure about modifying
        confirm_modify = menu(f"Are you sure you want to modify {attribute_choice}?", ["Yes", "No"])
        
        if confirm_modify == "No":
            # Ask if they want to manage attributes again
            manage_again = menu("Would you like to manage different attributes?", ["Yes", "No"])
            
            if manage_again == "Yes":
                continue  # Restart attribute management (go back to start of loop)
            else:
                return  # Return to main function
        
        # Step 3: Display current value and option to change it
        current_value = characters[selected_character][attribute_choice]
        change_options = [f"Enter new value (Current: {current_value})", "Return to attribute selection"]
        change_choice = menu(f"Modify {attribute_choice}:", change_options)
        
        if change_choice == "Return to attribute selection":
            continue  # Return to start of loop
        
        # Step 4: Get new value
        while True:
            try:
                new_value_input = input(f"Enter new value for {attribute_choice}: ")
                # Try to convert to same type as current value
                if isinstance(current_value, int):
                    new_value = int(new_value_input)
                elif isinstance(current_value, float):
                    new_value = float(new_value_input)
                else:
                    new_value = new_value_input
                break
            except ValueError:
                print(f"Invalid input. Please enter {'an integer' if isinstance(current_value, int) else 'a number' if isinstance(current_value, float) else 'a value'}.")
        
        # Step 5: Ask if sure about the change
        confirm_change = menu(f"Change {attribute_choice} from {current_value} to {new_value}?", ["Yes", "No"])
        
        if confirm_change == "No":
            continue  # Return to start of loop
        
        # Step 6: Apply changes
        characters[selected_character][attribute_choice] = new_value
        print(f"{attribute_choice} updated to {new_value}")
        
        # Step 7: Ask if want to change more attributes or return
        change_more = menu("Would you like to change more attributes?", ["Yes", "No (Return to Main)"])
        
        if change_more == "Yes":
            continue  # Return to start of loop
        else:
            return  # Exit attribute management function

