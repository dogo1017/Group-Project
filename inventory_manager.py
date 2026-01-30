# GNB fr

#Should end up here after a character has been selected and they wanna make/edit a certain inventory

saved_inventorys = {}

from menu import menu

# SIMPLE MENU FUNCTION (so the file runs without external imports)
#def menu(options):
 #   for i, option in enumerate(options):
   #     print(f"{i}. {option}")
    #while True:
     #   choice = input("Choose an option: ")
      #  if choice.isdigit() and 0 <= int(choice) < len(options):
       #     return int(choice)
        #print("Invalid choice.")

def add_items(characters, selected_character):
    # characters[selected_character][inventory]
        # access dictionary with saved inventory named 'saved_inventorys'

        # print all saved inventory from saved_inventory dictionary
    print(f"\nThis is what your inventory looks like right now:\n")

    if "inventory" not in characters[selected_character]:
        characters[selected_character]["inventory"] = []

    if len(saved_inventorys) == 0:
        print("No saved inventory items.")
    else:
        for name, item in saved_inventorys.items():
            print(f"{name}: {item}")

    #print(characters[selected_character][inventory])
        # use menu function from main to ask which item to add to inventory or return
    item_choice = input('Which item would you like to add to your inventory? (type "return" if you want to go back to menu):  ')

        # if return chosen then return to start of inventory managing function
    if item_choice.lower() == "return":
        return

        # if inventory selected then add inventory to character inventorys in the characters main attribute list
    if item_choice in saved_inventorys:
        characters[selected_character]["inventory"].append(saved_inventorys[item_choice])
        print(f"{item_choice} added to inventory.")

        # return to start of inventory managing function
        return
    else:
        print("Item not found.")


    # if remove from inventory option is chosen:
def remove_items(characters, selected_character):
        # let user input name(Save inventory name temporarily) with option to return(go back to start of inventory managment function)
    name = input('Inventory name ("return" to cancel): ')
    if name.lower() == "return":
        return

        # let user input description(Save inventory description temporarily) with option to return(go back to start of inventory managment function)
    description = input('Inventory description ("return" to cancel): ')
    if description.lower() == "return":
        return

        # let user input effect(Save inventory effect temporarily) with option to return(go back to start of inventory managment function)
    effect = input('Inventory effect ("return" to cancel): ')
    if effect.lower() == "return":
        return

        # let user input target(Save inventory target temporarily) with option to return(go back to start of inventory managment function)
    target = input('Inventory target ("return" to cancel): ')
    if target.lower() == "return":
        return

        # save inventory to dictionary saved_inventorys and apply to character
    saved_inventorys[name] = {
        "description": description,
        "effect": effect,
        "target": target
    }

    if "inventory" not in characters[selected_character]:
        characters[selected_character]["inventory"] = []

    characters[selected_character]["inventory"].append(saved_inventorys[name])

        # return to start of inventory management function
    print(f"{name} saved and added to character.")
    return

# define function to remove inventory from a character:
def remove_inventory_from_character(characters, selected_character):
    # Use menu function from main to choose between all characters inventorys and return(which returns to inventory managment function)
    if "inventory" not in characters[selected_character] or len(characters[selected_character]["inventory"]) == 0:
        print("No inventory to remove.")
        return

    options = [str(item) for item in characters[selected_character]["inventory"]]
    options.append("Return")

    choice = menu(options)

    if choice == len(options) - 1:
        return

    # remove selected inventory from character stats
    removed = characters[selected_character]["inventory"].pop(choice)
    print(f"Removed {removed}")

# define inventory_managment function:
def inventory_managment(characters, selected_character):
    # use menu function from main to choose between adding inventory (run add_inventory function), removing inventory(run remove_inventory), or return(retrn to main character management)
    options = ["Add inventory", "Remove inventory", "Return"]
    while True:
        choice = menu(options)
        if choice == 0:
            add_items(characters, selected_character)
        elif choice == 1:
            remove_inventory_from_character(characters, selected_character)
        elif choice == 2:
            return

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


characters = {
    "Hero": {}
}

selected_character = "Hero"

inventory_menu(characters, selected_character)
