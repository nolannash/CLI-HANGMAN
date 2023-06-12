import sys
import os
import time
#text colors and helper functions
def prRed(skk):   # sourcery skip: use-fstring-for-formatting
    print("\033[91m{}\033[00m".format(skk))
def prGreen(skk): # sourcery skip: use-fstring-for-formatting
    print("\033[92m{}\033[00m".format(skk))
def prYellow(skk):   # sourcery skip: use-fstring-for-formatting
    print("\033[93m{}\033[00m".format(skk))


        #pink
def prPink(skk):   # sourcery skip: use-fstring-for-formatting
    print('\033[95m{}\033[00m'.format(skk))
def prCyan(skk): # sourcery skip: use-fstring-for-formatting
    print("\033[96m{}\033[00m".format(skk))
def prLightPurple(skk): 
    print("\033[94m{}\033[00m".format(skk))

#! Menu functions and other helpers
def clear_terminal():
    os.system('clear')

def welcome_message():
    prPink('Hello and Welcome to: Dev Dot Exe(cute)')

def start_menu():
    clear_terminal()
    welcome_message()
    player_name, max_score = Result.find_max_score()
    if player_name and max_score:
        print(f"The player with the highest score is {player_name} with a score of {max_score}")
    else:
        print("No results found.")
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
        time.sleep(5)
    elif choice == '2':
        new_game_menu(player_inst.id)
    elif choice == '3':
        help_menu()
    elif choice == '4':
        quit_game()
    else:
        prRed('Please enter valid option')

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
    while True:
        print('''AVAILABLE HELP:''')
        print('1) High Scores')
        print('2) About the game')
        print('3) Return to main menu')
        prRed("Please select an option")
        help = input(">>>") #tweak to make it look better in terminal
        if help == '1':
            top_scores = Result.get_top_scores()
            if top_scores:
                for score in top_scores:
                    print(f"Player: {score['Player']}, Word: {score['Word']}, Score: {score['Score']}")
            else:
                print("No top scores available.")
            time.sleep(5)
        
        elif help == '2':
            about_game()
        elif help == "3":
            break

def about_game():
    prGreen('Select a topic to learn more!')
    print('1) How score is calculated: ')
    print('2) How difficulty is determined')
    print('3) Extras')
    choice = input()
    if choice == '1':
        print('The following is used to determine your score after each game:')

        print('\nEach correct guess adds 10 points.')

        print('\nEach incorrect guess deducts 5 points.')

        print('\nThe word length is multiplied by 5 and added to the score.')

        print('\nThe number of unique letters in the word is multiplied by 10 and added to the score.')

        print('\nAdditional points are added based on selected difficulty.')

        time.sleep(10)
    elif choice == '2':
        print('The following is used to determine the difficulty of each word:')

        print('\nWord Length: The words in each difficulty category were chosen to have an average length appropriate for the difficulty level.')

        print('\nVocabulary: Commonly used words were prioritized in the easy category, while medium and hard words include more specialized vocabulary or less frequently used terms.')

        print('\nComplexity: The complexity of the words increases as the difficulty level rises. Easy words are simple and commonly known, while hard words are more challenging and might require specific knowledge or context.')

        print('\n*Variety: The list aims to include a diverse range of words, covering different themes, topics, and word structures.')
        time.sleep(10)
    elif choice == '3':
        print('there are no extras right now')
        time.sleep(10)
    else:
        print('Please enter a valid answer')

def quit_game():
    clear_terminal()
    sys.exit()

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
    """
    SELECT games.word, results.score
    FROM results
    INNER JOIN games ON results.game_id = games.id
    WHERE results.player_id = ?
    ORDER BY results.score DESC
    """, (player_inst_id,)
    )
    rows = CURSOR.fetchall()
    for row in rows:
        word, score = row
        print(f"Word: {word} | Score: {score}")   

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