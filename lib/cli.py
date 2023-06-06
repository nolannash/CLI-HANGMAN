from .helpers import *

def main():
    welcome_message()
    while True:
        start_menu()
        choice = input('Please Select an Option')
        if choice ==1:
            login_menu()
        elif choice ==2:
            new_player_menu()
        elif choice ==3:
            help_menu()
        elif choice ==4:
            quit_game()
            break
        else:
            print('Please enter a valid option.')
            

if __name__ == "__main__":
    main()