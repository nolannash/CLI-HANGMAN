# from classes.game import Game
# from classes.player import Player
# from classes.result import Result
# from __init__ import CONN, CURSOR
from .helpers import *
import sys
import os



def main():
    welcome_message()
    while True:
        start_menu()
        choice = input('Please Select an Option')
        if choice ==1:
            login_menu()
        if choice ==2:
            new_player_menu()
        if choice ==3:
            help_menu()
        if choice ==4:
            quit_game()
            

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
            userName = input('''Next Enter a UserName: ''')
            password = input('''Please Enter A 4 Digit PIN: ''')
            Player.create(name,userName,password)

#if player selects help menu
        elif player_choice == 3:
            clear_terminal()
            print('''AVAILABLE HELP
                ''')

#if player selects quit
        elif player_choice ==4:
            clear_terminal()
            sys.exit()

#after going through start menu 
        def new_game_menu():
            print('hi')


if __name__ == "__main__":
    main()