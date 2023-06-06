import random
# from player.py import Player
from .__init__.py import CONN,CURSOR
class Game:
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
    
    VALID_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    
    def __init__(self,game_player, difficulty):
        self.difficulty = difficulty
        self.letters_entered = set()
        self.word 
        self.player = game_player
        self.turns = 10
        self.score = 0

#properties and attributes
    @property
    def word(self):
        setattr(self,'_word','')
        return self._word
    
    @word.setter
    def word(self):
        if self.difficulty == "Easy":
            self._word = random.choice(Game.EASY_WORDS)

        elif self.difficulty == "Medium":
            self._word = random.choice(Game.MEDIUM_WORDS)

        else:
            self._word = random.choice(Game.HARD_WORDS)
        return self._word

#instance methods
    def play_hangman(self):
        missed = 0
        guessmade = ''

        while len(self._word) >0:
            main = ""
            
            for letter in self._word:
                main = main + letter if letter in guessmade else f"{main}_ "
                
            if main == self._word:
                print(main)
                print("You win!")


            print("Guess the word:" , main)
        guess = input()

        if guess in type(self).VALID_LETTERS:
            guessmade += guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in self._word:
            turns = turns - 1
            if turns == 0:
                self.hm_extract(
                "You loose", 
                "You let a kind man die",
                "  --------  "
                )
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")

            elif turns == 1:
                self.hm_extract(
                "1 turns left",
                "Last breaths counting, Take care!",
                "  --------  ",
                )
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")

            elif turns == 2:
                self.hm_extract(
                "2 turns left", 
                "  --------  ", 
                "   \ O /|   "
                )
                print("     |      ")
                print("    / \     ")

            elif turns == 3:
                self.hm_extract(
                "3 turns left", 
                "  --------  ",
                "   \ O /    "
                )
                print("     |      ")
                print("    / \     ")

            elif turns == 4:
                self.hm_extract(
                "4 turns left", 
                "  --------  ",
                "   \ O      "
                )
                print("     |      ")
                print("    / \     ")

            elif turns == 5:
                self.hm_extract(
                "5 turns left",
                "  --------  ",
                "     O      "
                )
                print("     |      ")
                print("    / \     ")

            elif turns == 6:
                self.hm_extract(
                "6 turns left", 
                "  --------  ", 
                "     O      "
                )
                print("     |      ")
                print("    /       ")

            elif turns == 7:
                self.hm_extract(
                "7 turns left", 
                "  --------  ", 
                "     O      "
                )
                print("     |      ")

            elif turns == 8:
                self.hm_extract(
                "8 turns left",
                "  --------  ",
                "     O      "
                )

            elif turns == 9:
                print("9 turns left")
                print("  --------  ")
    #connected to play hangman --> meant to reduce redundant typing
    def hm_extract(self, arg0, arg1, arg2):
        print(arg0)
        print(arg1)
        print(arg2)

    def calculate_score(self):
        if self.difficulty == "Easy":
            self.score + 10
        elif self.difficulty == "Medium":
            self.score + 15
        else:
            self.score + 25

#classmethods
    @classmethod
    def create_table(cls):
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS games(
                id INTEGET PRIMARY KEY,
                player_id,
                result INTEGER,
                FORIEGN KEY (player_id) REFERENCES players(id)
            );        
        ''')
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        CURSOR.execute("""
            DROP TABLE IF EXISTS games;
            """)


    # def game_status(self):
    #     for letter in self.word_to_be_guessed:
    #         if letter in self.letters_entered:
    #             print ("You have guessed the word!")
    #             return True

        # return False
        
    
    # def enter_letter(self):
    #     letter_entered = input("Enter letter to guess: ")
    #     for letter in self.letters_entered:
    #         if letter_entered is not letter:
    #             self.letters_entered.add(letter_entered)
    #         else: 
    #             raise Exception("You already guessed that letter!")
    
    

