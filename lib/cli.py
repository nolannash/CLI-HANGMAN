from classes.game import Game
from classes.player import Player
from classes.result import Result
import sys
# # import colorama
# from colorama import Fore


def main():
#text colors
    def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
#welcome message
    prRed(
        '''Hello and Welcome To HangMan
        \n''')
    
#start menu allows user to choose how to procede
    player_choice = 0
    while player_choice !=4:
        print('''Please Select an Option:\n
            ''')
        print('1) I have never played before!')
        print('2) I have played before!')
        print('3) Help')
        print('4) Quit.')
        player_choice = int(input())

#if the player has played before
        if player_choice == 1:
            input('Please Enter Your Username:')
            
#if the player has not played before
        elif player_choice == 2:
            name = input('''To Begin Please Enter Your Name''')
            userName = input('''Next Enter a UserName''')
            password = input('''Please Choose a PIN (PIN must be 4 numbers)''')
            new_player = Player.create(name,userName,password)
            
            
#if they select help (show commands etc)
        elif player_choice == 3:
            print('''AVAILABLE HELP
                ''')
#if they type quit
        elif player_choice ==4:
            sys.exit()

if __name__ == "__main__":
    main()