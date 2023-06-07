#nolans to-do thoughts:
    #! MISSING DELIVERABLES
        #confirm we are using: list,tuple,dictionary --> list good, 
        #go back through validations
        #add imported modules somehow 
    #! THINGS WE COULD/SHOULD add
    #helpers #
        # --> add "help" methods --click/argparse(?)
        # add method (in help?) to show scores --> all time highscore + personal

    #player #
        # --> has lists of results
    #results 
        #--> connected properly
    #game 
        # --> might be fun to add method to allow people who have certain amt of points to add words to the lists or something *win bonus*
        #--> show all available letters --> guessed letters in color, correct in green and incorrect in red

def main():
    make_tables()
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

from helpers import *