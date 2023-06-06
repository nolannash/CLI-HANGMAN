from classes.game import Game
from classes.player import Player
from classes.result import Result
from classes.__init__ import CONN, CURSOR

import sys
import os



def main():
#text colors and helper functions
        #red
    def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
        #yellow
    def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
        #green
    def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
        #pink
    def prPink(skk): print('\033[95m {}\033[00m]' .format(skk))
        #clear terminal
    def clear_terminal():
        os.system('clear')

    #welcome message
    prRed(
        '''Hello and Welcome To HangMan
        \n''')

#start menu allows user to choose how to procede
    player_choice = 0
    while player_choice !=4:
        print('''Please Select an Option:\n
            ''')
        print('1) Login')
        print('2) New Player')
        print('3) Help')
        print('4) Quit.')
        player_choice = int(input())

#if the player has played before
        if player_choice == 1:
            clear_terminal()
            prRed('To Go Back To Start Menu Please Type "back".')
            username_input = input('Please Enter Your Username:')
            if isinstance(username_input,Player) and Player.username == username_input:
                new_game_menu()
            elif username_input == "back" or "Back" :
                player_choice = 0
            else:
                prRed('Please Enter A Valid Username!')

#if player has not played before
        elif player_choice == 2:
            clear_terminal()
            name = input('''To Begin Please Enter Your Name: ''')
            username = input('''Next Enter a UserName: ''')
            password = input('''Please Enter A 4 Digit PIN: ''')
            Player.create(name,username,password)


        elif player_choice == 3:
            clear_terminal()
            print('''AVAILABLE HELP
                ''')
        elif player_choice ==4:
            clear_terminal()
            sys.exit()
            
        def new_game_menu():
            print('hi')


if __name__ == "__main__":
    main()