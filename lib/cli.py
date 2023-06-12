from helpers import *
##!! side note --> I am not sure where ".headers" came from and dont want to delete
##!! if it would cause some sort of issue. -Nolan
def main():
    # make_tables()
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