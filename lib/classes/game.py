EASY_WORDS = ['Hat','Bed','Cup','Fish','Jump','Milk'
,'Park','Duck','Sing','Beach','Frog','Baby','Cake'
,'Moon','Smile','Bear','Boat',"Train","Apple","Dance"
,"Flower","Grass","House","Key","Star","Duck","Mouse"
,"Chair","Bird","Frog","Kite","Lion","Orange","Pear"
,"Rabbit","Ship","Snake","Tiger","Water","Elephant"
]

MEDIUM_WORDS =['Bicycle','Camera','Jacket'
,'Ocean','Puzzle','Rainbow','Soccer','Telescope','Banana'
,'Candle','Dolphin','Feather','Guitar','Mountain','Puzzle'
,'Robot','Spider','Turtle','Wallet','Chocolate','Elephant'
,'Fireworks','Guitar','Jellyfish','Monkey','Penguin','Rainbow'
,'Scissors','Tomato','Butterfly','Dragonfly','Football','Honey'
,'Lollipop','Mushroom','Octopus','Panda','Raccoon','Seashell'
,'Turtle','Watermelon','Zebra','Clock','Dragon','Firefly'
,'Hedgehog','Lantern','Marshmallow','Parrot','Sunflower'
]

HARD_WORDS =['Extraterrestrial'
,'Metamorphosis','Cryptocurrency','Chrysanthemum','Nostalgia'
,'Paradox','Phenomenon','Ambiguous','Hieroglyphics'
,'Synesthesia','Cacophony','Epiphany','Xylophone',
'Quixotic','Onomatopoeia','Kaleidoscope','Schadenfreude'
,'Phantasmagoria','Esoteric','Ubiquitous','Zealous'
,'Capricious','Euphoria','Aberration','Mellifluous'
,'Labyrinth','Serendipity','Pseudonym','Discombobulate'
,'Mellifluous','Exacerbate'
,'Vexatious','Serendipity','Ineffable','Serendipity'
,'Perseverance','Unfathomable','Phantasmagoric','Serendipity'
,'Perspicacious','Conundrum','Serendipity','Mellifluous'
,'Inscrutable','Esoteric','Schadenfreude'
]

class Game:

    VALID_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.letters_entered = set()
        self.set_word(self)
        self.turns = 10
        self.score = 0

####!properties and attributes

#word property
    def get_word(self):
        return self._word

    def set_word(self,difficulty):
        difficulty = self.difficulty
        if difficulty == "Easy":
            self._word = random.choice(EASY_WORDS).lower()

        elif difficulty == "Medium":
            self._word = random.choice(MEDIUM_WORDS).lower()

        else:
            self._word = random.choice(HARD_WORDS).lower()

    word = property(get_word,set_word)

#player property --> not done needs to set player (?)
    def get_player(self):
        return self._player
    
    def set_player(self,player):
        if isinstance(player,Player):
            self._player = player


####!instance methods

#method to display the word as the game goes along
    def display_word(self):
        # sourcery skip: assign-if-exp, inline-immediately-returned-variable, use-fstring-for-concatenation, use-join
        display = ''
        for letter in self.word:
            if letter in self.letters_entered:
                display += letter + ' '
            else:
                display += '_ '
        return display

#method for when player makes a guess
    def guess(self,letter):
        letter = letter.lower()
        if letter in self.letters_entered:
            return "You've already guessed that letter!"
        self.letters_entered.add(letter)
        if letter not in self.word:
            self.turns -= 1
        return self.display_word()

#method for determining when game is over
    def is_game_over(self):
        return all(letter in self.letters_entered for letter in self.word)

#method to actually display the hangman
    def display_hangman(self):
        if self.turns == 0:
            self.hm_extract("You let a good dev die", "  --------  ")
            print("     O_|    ")
            print("    /|\      ")
            print("    / \     ")

        elif self.turns == 1:
            self.hm_extract(
            "1 turns left",
            "Last breaths counting, Take care!",
            "  --------  ",
            )
            print("   \ O_|/   ")
            print("     |      ")
            print("    / \     ")

        elif self.turns == 2:
            self.hm_extract("2 turns left", "  --------  ", "   \ O /|   ")
            print("     |      ")
            print("    / \     ")

        elif self.turns == 3:
            self.hm_extract("3 turns left", "  --------  ", "   \ O /    ")
            print("     |      ")
            print("    / \     ")

        elif self.turns == 4:
            self.hm_extract("4 turns left", "  --------  ", "   \ O      ")
            print("     |      ")
            print("    / \     ")

        elif self.turns == 5:
            self.hm_extract("5 turns left", "  --------  ", "     O      ")
            print("     |      ")
            print("    / \     ")

        elif self.turns == 6:
            self.hm_extract("6 turns left", "  --------  ", "     O      ")
            print("     |      ")
            print("    /       ")

        elif self.turns == 7:
            self.hm_extract("7 turns left", "  --------  ", "     O      ")
            print("     |      ")

        elif self.turns == 8:
            self.hm_extract("8 turns left", "  --------  ", "     O      ")

        elif self.turns == 9:
            print("9 turns left")
            print("  --------  ")

#the game itself (uses ^ methods)
    def play(self):
        while not self.is_game_over():
            print("\n" + self.display_word())
            # print("Guesses left:", self.max_guesses)
            self.display_hangman()
            letter = input("Enter a letter: ")
            result = self.guess(letter)
            print(result)
            if self.turns > 0 and self:
                print("\nCongratulations! You guessed the word:", self.word)
            else:
                print("\nGame over! The word was:", self.word)
                self.score = 0

#extractor for display hangman
    def hm_extract(self, arg0, arg1, arg2):
        print(arg0)
        print(arg1)
        print(arg2)

#method for calculating the score of a given game
    def score_calculator(self):
        word_length = len(self.word)
        unique_letters = len(set(self.word))
        correct_guesses = len(self.letters_entered.intersection(set(self.word)))
        incorrect_guesses = len(self.letters_entered.difference(set(self.word)))
        score = (correct_guesses * 10) - (incorrect_guesses * 5) + (word_length * 5) + (unique_letters * 10)
        self.score = max(0, score)

####!classmethods
#make the table if it doesnt exist
    @classmethod
    def create_table(cls):
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS games(
                id INTEGER PRIMARY KEY,
                score INTEGER,
                player_id INTEGER,
                FOREIGN KEY (player_id) REFERENCES players(id)
            );        
        ''')
        CONN.commit()

    
#drop the table
    @classmethod
    def drop_table(cls):
        CURSOR.execute("""
            DROP TABLE IF EXISTS games;
            """)

####!imports
import random
from classes.player import Player
from classes.__init__ import CONN,CURSOR
