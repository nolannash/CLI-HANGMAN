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
    

def new_player_menu():
    ...

def help_menu():
    ...

def quit_game():
    clear_terminal()
    sys.exit()

