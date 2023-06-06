import sys
import os

#text colors and helper functions
        #red
def prRed(skk):   # sourcery skip: use-fstring-for-formatting
    print("\033[91m {}\033[00m" .format(skk))


        #green
def prGreen(skk): # sourcery skip: use-fstring-for-formatting
    print("\033[92m {}\033[00m" .format(skk))


        #yellow
def prYellow(skk):   # sourcery skip: use-fstring-for-formatting
    print("\033[93m {}\033[00m" .format(skk))


        #pink
def prPink(skk):   # sourcery skip: use-fstring-for-formatting
    print('\033[95m {}\033[00m]' .format(skk))


def clear_terminal():
    os.system('clear')
    
def welcome_message():
    prRed('''Hello and Welcome To HangMan\n''')
    
def start_menu():
    print('Please Select an Option:\n')
    print('1) Login')
    print('2) New Player')
    print('3) Help')
    print('4) Quit.')

def login_menu():
    clear_terminal()
    prRed('To Go Back To Start Menu Please Type "back".')
    username_input = input('Please Enter Your Username:')
    if isinstance(username_input,Player) and Player.username == username_input:
        new_game_menu()
    else:
        player_choice = 0
    

def new_player_menu():
    clear_terminal()
    name = input('''To Begin Please Enter Your Name: ''')
    userName = input('''Next Enter a UserName: ''')
    password = input('''Please Enter A 4 Digit PIN: ''')
    Player.create(name,userName,password)


def help_menu():
    clear_terminal()
    print('''AVAILABLE HELP:''')
    #methods go here

def quit_game():
    clear_terminal()
    sys.exit()

def new_game_menu():
    ...
from classes.game import Game
from classes.player import Player
from classes.result import Result
