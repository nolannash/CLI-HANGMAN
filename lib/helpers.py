import sys
import os

#text colors and helper functions
        #red
def prRed(skk):   # sourcery skip: use-fstring-for-formatting
    print("\033[91m{}\033[00m".format(skk))


    #green
def prGreen(skk): # sourcery skip: use-fstring-for-formatting
    print("\033[92m{}\033[00m".format(skk))


        #yellow
def prYellow(skk):   # sourcery skip: use-fstring-for-formatting
    print("\033[93m{}\033[00m".format(skk))


        #pink
def prPink(skk):   # sourcery skip: use-fstring-for-formatting
    print('\033[95m{}\033[00m'.format(skk))

def prCyan(skk): # sourcery skip: use-fstring-for-formatting
    print("\033[96m{}\033[00m".format(skk))

def prLightPurple(skk): 
    print("\033[94m{}\033[00m".format(skk))


def clear_terminal():
    os.system('clear')

def welcome_message():
    prPink('Hello and Welcome to: Python Hangman!')

def start_menu():
    clear_terminal()
    welcome_message()

    prGreen('\n1) Login')
    prCyan('2) New Player')
    prYellow('3) Help')
    prRed('4) Quit')

def login_menu():
    # clear_terminal()

    username_input = input('Please Enter Your Username:')
    if isinstance(username_input, Player) and username_input.username == Player.username:
        returning_player = Player.find_by_id(Player.id)
        new_game_menu(returning_player)
    else:
        choice = 0


def new_player_menu():
    clear_terminal()
    
    prGreen('Excellent Please Follow The Direcetions To Create Your Account:')
    
    name = input('''To Begin Please Enter Your Name: ''')
    prGreen(f'Thank you! {name}')
    
    userName = input('''Next Enter a UserName: ''')
    prGreen(f'Excellent {userName} last step!')
    
    password = input('''Please Enter A 4 Digit PIN: ''')
    
    new_player = Player.create(name,userName,password)
    
    new_player.save()
    new_game_menu(new_player)


def help_menu():
    clear_terminal()
    print('''AVAILABLE HELP:''')
    #methods go here
        #forgot username --> find by username
        #player method to show highest scores
        #point calculator explained

def quit_game():
    clear_terminal()
    sys.exit()

#saves player from either login -> get_by_id
#or the Player.create from new_player_menu
def new_game_menu(player_instance):
    clear_terminal()
    prRed('\nWelcome it is time to begin playing!')
    difficulty = input('First please select a difficulty: \n>>Easy \n>>Medium \n>>Hard\n')
    new_game = Game(player_instance, difficulty.title())
    clear_terminal()
    prLightPurple('Let The Game Begin!')
    new_game.play()
    
    
from classes.game import Game
from classes.player import Player
from classes.result import Result
