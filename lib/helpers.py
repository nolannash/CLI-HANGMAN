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

    prGreen('\n1) Login')
    prCyan('2) New Player')
    prYellow('3) Help')
    prRed('4) Quit')

def login_menu():

    new_player = None

    while not new_player:
        username_input = input('Please Enter Your Username: ')
        password_input = input('Please enter your password: ') 
        new_player = Player.auth_user(username_input, password_input)
        prRed("Incorrect username or password. Try again")
    clear_terminal()
    logged_in_menu(new_player)

def logged_in_menu(player_inst):
    print(f'welcome {player_inst.username}!')
    print('\n Please choose one of the following:')
    prYellow('\n1) See your scores:')
    prGreen('\n2) Start a new game:')
    prRed('\n3) Quit')
    choice = input()
    if choice == '1':
        show_me_scores(player_inst.id)
    elif choice == '2':
        new_game_menu(player_inst.id)
    elif choice == '3':
        quit_game()
    else:
        prRed('Please enter valid option')

#if you havent played before
def new_player_menu():
    clear_terminal()

    prGreen('Excellent Please Follow The Direcetions To Create Your Account:')

    name = input('''To Begin Please Enter Your Name: ''')
    prGreen(f'Thank you! {name}')

    userName = input('''Next Enter a UserName: ''')
    prGreen(f'Excellent {userName} last step!')

    password = input('''Please Enter A 4 Digit PIN: ''')

    new_player = Player.create(name,userName,int(password))
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
# def new_game_menu(new_player):
#     clear_terminal()
#     prRed('\nWelcome it is time to begin playing!')
#     difficulty = input('First please select a difficulty: \n>>Easy \n>>Medium \n>>Hard\n')
#     new_game = Game.create(difficulty.title())
#     Result.create(0, new_player.id, new_game.id)
#     clear_terminal()
#     prLightPurple('Let The Game Begin!')
#     new_game.play()
def new_game_menu(player_instance):

    clear_terminal()
    prRed('\nWelcome it is time to begin playing!')
    difficulty = input('First please select a difficulty: \n>>Easy \n>>Medium \n>>Hard\n')
    new_game = Game.create(difficulty.title())
    Result.create(0, player_instance.id, new_game.id)
    clear_terminal()
    prLightPurple('Let The Game Begin!')
    new_game.play()

def show_me_scores(player_inst_id):
    CURSOR.execute(
    """"SELECT 
        games.word, results.score 
        FROM results
        INNER JOIN games
        ON results.player_id = ? AND results.game_id = games.id
    """, (player_inst_id,)
    )
    
    
def make_tables():
    Player.drop_table()
    Game.drop_table()
    Result.drop_table()

    Player.create_table()
    Game.create_table()
    Result.create_table()

from classes.game import Game
from classes.player import Player
from classes.result import Result
from classes.__init__ import CONN, CURSOR