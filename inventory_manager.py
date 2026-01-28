# GNB fr

#Should end up here after a character has been selected and they wanna make/edit a certain inventory

from main import menu

def main():
    options = ["Add items", "Remove items", "Return to Menu"]
    while True:
        choice = menu(options)
        if choice == 0:
            add_items()
        elif choice == 1:
            if selected_character == "":
                remove_items()
            else:
                print("Please select a character before entering this function👍.")
                input("Press Enter to continue...")
                continue
        elif choice == 2:
            if selected_character != "":
                menu()
            else:
                print("Please select a character before entering this function👍.")
                input("Press Enter to continue...")
                continue
        else:
            selected_character = search.search_menu()

selected_character = ""
main()

# define function to add inventory to selected character:
def choice():
    # use menu function from main to choose between adding an existing inventory, new one, or return

    option = input("Do you want to add or remove an item from your inventory? Or do you want to return to the menu?👍: ")
    # if return chosen:
        # return to start of inventory management function
    # if existing inventory option is chosen:
        # access dictionary with saved inventory named 'saved_inventorys'
        # print all saved inventory from saved_inventory dictionary
        # use menu function form main to ask which inventory to add or return
        # if return chosen then return to start of inventory managing function
        # if inventory selected then add inventory to character inventorys in the characters main attribute list
        # return to start of inventory managing function
    # if new inventory option is chosen:
        # let user input name(Save inventory name temporarily) with option to return(go back to start of inventory managment function)
        # let user input description(Save inventory description temporarily) with option to return(go back to start of inventory managment function)
        # let user input effect(Save inventory effect temporarily) with option to return(go back to start of inventory managment function)
        # let user input target(Save inventory target temporarily) with option to return(go back to start of inventory managment function)
        # save inventory to dictionary saved_inventorys and apply to character
        # return to start of inventory management function
# define function to remove inventory from a character:
    # Use menu function from main to choose between all characters inventorys and return(which returns to inventory managment function)
    # remove selected inventory from character stats
# define inventory_managment function:
    # use menu function from main to choose between adding inventory (run add_inventory function), removing inventory(run remove_inventory), or return(retrn to main character management)