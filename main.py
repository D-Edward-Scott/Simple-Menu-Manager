

MESSAGE = "Choose an option:"

OPTIONS = [
    "Option 1",
    "Option 2",
    "Option 3",
    "Option 4",
    "Option 5",
    "Option 6",
    "Option 7",
    "Option 8",
    "Option 9",
    "Option 10"    
]

RETURN_MESSAGE = "exit"


def standard_menu(message, options, return_message):
    while True:
        option_number = 1
        print(message)
        for option in options:
            print("    " + str(option_number) + ". " + option) 
            option_number += 1

        print(f"    0. {return_message}")

        try:
            selection = int(input(f"""Please make a selection (0 - {option_number - 1})
    > """))
            if selection in range(len(options) + 1):
                return selection

        except ValueError:
            print(f"Invalid selection, please try again (0 - {option_number - 1})")



def curses_menu(message, options, return_message):
    #TODO implement curses menu with handling 
    pass

    current_selection = 1
    option_number = 1
    while True:
        for option in options:
            if option_number == current_selection:
                print(">    " + str(option_number) + ". " + option + "<") 
            else:
                print("    " + str(option_number) + ". " + option) 

            option_number += 1

        if 0 == current_selection:
            print(f">    0. {return_message}<") 
        else:
            print(f"    0. {return_message}")

        try:
            selection = int(input(f"""Please make a selection (0 - {option_number - 1})
    > """))

            if selection in range(len(options) + 1):
                return selection

        except ValueError:
            print(f"Invalid selection, please try again (0 - {option_number - 1})")


def menu_handler(message, options, return_message, menu_type = "default"):
    #TODO add length checks to create tiers of menus, add checks for curses and select menu type
    if menu_type.lower() == "default" or menu_type.lower() == "curses":
        try:
            import curses
            menu_type = "curses"
        except ImportError:
            menu_type = "standard"

    if menu_type == "standard":
        return standard_menu(message, options, return_message)
    elif menu_type == "curses":
        #return "not yet implemented" #TODO
        
        return curses_menu(message, options, return_message)
    else:
        return "Invalid menu type"



print(menu_handler(MESSAGE, OPTIONS, RETURN_MESSAGE))
