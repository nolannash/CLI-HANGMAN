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

def prLightPurple(skk):   # sourcery skip: use-fstring-for-formatting
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
    clear_terminal()
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
    
    new_player = Player.create(name,userName,int(password))
    
    # new_player.save()
    new_game_menu(new_player)


def help_menu():
    clear_terminal()
    print('''AVAILABLE HELP:''')
    print('1) I forgot my username')
    print('2) About the game')
    help = input(prRed('\n Please select an option'))
    if help == '1':
        forgot_username()
    elif help == '2':
        about_game()

#needs work
def forgot_username():
    player_name = input('Lets find your profile!')
    if Player.find_by_name(player_name) is True:
        player_profile = Player.find_by_id()
    
def about_game():
    prGreen('Select a topic to learn more!')
    print('1) How score is calculated: ')
    print('2) How difficulty is determined')
    print('3) Extras')
    choice = input()
    if choice == '1':
        print('The following is used to determine your score after each game:')
        
        print('\n*Each correct guess adds 10 points.')
        
        print('\n*Each incorrect guess deducts 5 points.')
        
        print('\n*The word length is multiplied by 5 and added to the score.')
        
        print('\n*The number of unique letters in the word is multiplied by 10 and added to the score.')
        
        print('\n*Additional points are added based on selected difficulty.')

    elif choice == '2':
        print('The following is used to determine the difficulty of each word:')

        print('\n*Word Length: The words in each difficulty category were chosen to have an average length appropriate for the difficulty level.')

        print('\n*Vocabulary: Commonly used words were prioritized in the easy category, while medium and hard words include more specialized vocabulary or less frequently used terms.')

        print('\n*Complexity: The complexity of the words increases as the difficulty level rises. Easy words are simple and commonly known, while hard words are more challenging and might require specific knowledge or context.')

        print('\n*Variety: The list aims to include a diverse range of words, covering different themes, topics, and word structures.')

    elif choice == '3':
        print('there are no extras right now :-( ')

    else:
        print('Please enter a valid answer')


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
