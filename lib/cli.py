from helpers import (
    login_menu,
    new_player_menu,
    help_menu,
    quit_game,
    start_menu,
    prRed,
    welcome_message,
    make_tables)
#nolans to-do thoughts:
    #! MISSING DELIVERABLES
        #confirm we are using: list,tuple,dictionary --> list good, 
        #go back through validations
        #add imported modules somehow 

def main():
    make_tables()
    welcome_message()
    while True:
        start_menu()
        choice = input('\nPlease Select an Option: ')
        if choice == '1' :
            login_menu()
        elif choice == '2' :
            new_player_menu()
        elif choice == '3' :
            help_menu()
        elif choice == '4' :
            quit_game()
            break
        else:
            prRed('Please Enter Valid Answer!')


if __name__ == "__main__":
    main()

