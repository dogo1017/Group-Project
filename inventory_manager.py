# GNB fr

#Should end up here after a character has been selected and they wanna make/edit a certain inventory

#from main import menu

def add_items():
   # characters[selected_character][inventory]
        # access dictionary with saved inventory named 'saved_inventorys'

        # print all saved inventory from saved_inventory dictionary
    #print(characters[selected_character][inventory])
        # use menu function from main to ask which item to add to inventory or return
    item_choice = input("Which item would you like to add to your inventory? (type return if you want to go back to menu):  ")
        # if return chosen then return to start of inventory managing function
        # if inventory selected then add inventory to character inventorys in the characters main attribute list
        # return to start of inventory managing function
    # if remove from inventory option is chosen:
def remove_items():
    help
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

from menu import menu
def inventory_menu(characters, selected_character):
    options = ["Add items", "Remove items", "Return to Menu"]
    while True:
        choice = menu(options)
        if choice == 0:
            add_items(characters, selected_character)
        elif choice == 1:
            remove_items(characters, selected_character)
        elif choice == 2:
            return characters, selected_character