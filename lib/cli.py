from classes.game import Game
from classes.player import Player
from classes.result import Result
import sys
import os
# # import colorama
# from colorama import Fore


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
            player_choice = 0
        elif player_choice == 2:
            name = input('''To Begin Please Enter Your Name''')
            userName = input('''Next Enter a UserName''')
            password = input('''Please Choose a PIN (PIN must be 4 numbers)''')
            Player.create(name,userName,password)


        elif player_choice == 3:
            print('''AVAILABLE HELP
                ''')
        elif player_choice ==4:
            sys.exit()
            
def new_game_menu():
    ...


if __name__ == "__main__":
    main()