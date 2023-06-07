

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
    
    def __init__(self,player, difficulty,word=''):

        self.difficulty = difficulty
        self.letters_entered = set()

        self.player = player
        self.set_word(word)
        self.turns = 10
        self.score = 0

#properties and attributes
    def get_word(self):
        return self._word
   
    def set_word(self,difficulty):
        difficulty = self.difficulty
        if difficulty == "Easy":
            self._word = random.choice(Game.EASY_WORDS)

        elif difficulty == "Medium":
            self._word = random.choice(Game.MEDIUM_WORDS)

        else:
            self._word = random.choice(Game.HARD_WORDS)
    word = property(get_word,set_word)

#instance methods

    def game_over(self):
        print('im 100% working')

        return self.turns == 0 or self.letters_entered == set(list(self.get_word()))
    
    def play_hangman(self):
        guessmade = ''
        word = self._word
        turns = self.turns

        while turns > 0:
            main = ""
            for letter in word:
                if letter in guessmade:
                    main = main + letter
                else:
                    main = main + "_" + " "

            if main == self._word:
                print(main)
                print("You win!")
                return

            print("Guess the word:", main)
            guess = input()

            if guess in type(self).VALID_LETTERS:
                guessmade += guess
            else:
                print("Enter a valid character")
                continue 

            if guess not in word:
                turns -= 1
                if turns == 0:
                    self.hm_extract(
                        "You lose",
                        "You let a kind man die",
                        "  --------  "
                    )
                    print("     O_|    ")
                    print("    /|\\     ")
                    print("    / \\     ")
                elif turns == 1:
                    self.hm_extract(
                        "1 turn left",
                        "Last breaths counting, take care!",
                        "  --------  ",
                    )
                    print("   \\ O_|/   ")
                    print("     |      ")
                    print("    / \\     ")
                elif turns == 2:
                    self.hm_extract(
                        "2 turns left",
                        "  --------  ",
                        "   \\ O /|   "
                    )
                    print("     |      ")
                    print("    / \\     ")
                elif turns == 3:
                    self.hm_extract(
                        "3 turns left",
                        "  --------  ",
                        "   \\ O /    "
                    )
                    print("     |      ")
                    print("    / \\     ")
                elif turns == 4:
                    self.hm_extract(
                        "4 turns left",
                        "  --------  ",
                        "   \\ O      "
                    )
                    print("     |      ")
                    print("    / \\     ")
                elif turns == 5:
                    self.hm_extract(
                        "5 turns left",
                        "  --------  ",
                        "     O      "
                    )
                    print("     |      ")
                    print("    / \\     ")
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

    print("You ran out of turns. The word was:", word)
    # def play_hangman(self):
    #     # sourcery skip: hoist-statement-from-loop, use-fstring-for-concatenation
    #     #show how many tries left(?)
    #     guessmade = ''
    #     word = self._word
    #     turns = self.turns
        
    #     while turns > 0 :
    #         main = ""
            
    #         for letter in word:
    #             if letter in guessmade:
    #                 main = main + letter
    #         main = main + "_" + " "
    #     if main == word:
    #         print(main)
    #         print("You win!")

    #     print("Guess the word:" , main)
    #     guess = input()

    #     if guess in type(self).VALID_LETTERS:
    #         guessmade += guess

    #     else:
    #         print("Enter a valid character")
    #         guess = input()

    #     if guess not in word:
    #         turns -=1
    #         if turns == 0:
    #             self.hm_extract(
    #             "You loose", 
    #             "You let a kind man die",
    #             "  --------  "
    #             )
    #             print("     O_|    ")
    #             print("    /|\      ")
    #             print("    / \     ")

    #         elif turns == 1:
    #             self.hm_extract(
    #             "1 turns left",
    #             "Last breaths counting, Take care!",
    #             "  --------  ",
    #             )
    #             print("   \ O_|/   ")
    #             print("     |      ")
    #             print("    / \     ")

    #         elif turns == 2:
    #             self.hm_extract(
    #             "2 turns left", 
    #             "  --------  ", 
    #             "   \ O /|   "
    #             )
    #             print("     |      ")
    #             print("    / \     ")

    #         elif turns == 3:
    #             self.hm_extract(
    #             "3 turns left", 
    #             "  --------  ",
    #             "   \ O /    "
    #             )
    #             print("     |      ")
    #             print("    / \     ")

    #         elif turns == 4:
    #             self.hm_extract(
    #             "4 turns left", 
    #             "  --------  ",
    #             "   \ O      "
    #             )
    #             print("     |      ")
    #             print("    / \     ")

    #         elif turns == 5:
    #             self.hm_extract(
    #             "5 turns left",
    #             "  --------  ",
    #             "     O      "
    #             )
    #             print("     |      ")
    #             print("    / \     ")

    #         elif turns == 6:
    #             self.hm_extract(
    #             "6 turns left", 
    #             "  --------  ", 
    #             "     O      "
    #             )
    #             print("     |      ")
    #             print("    /       ")

    #         elif turns == 7:
    #             self.hm_extract(
    #             "7 turns left", 
    #             "  --------  ", 
    #             "     O      "
    #             )
    #             print("     |      ")

    #         elif turns == 8:
    #             self.hm_extract(
    #             "8 turns left",
    #             "  --------  ",
    #             "     O      "
    #             )

    #         elif turns == 9:
    #             print("9 turns left")
    #             print("  --------  ")

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
   
    @classmethod #create_table -> need to determine columns
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS games(
                id INTEGER PRIMARY KEY AUTOINCREMENTING,
                name TEXT NOT NULL,
                password INTEGER
            );        
        """)

import random
from classes.player import Player
from classes.__init__ import CONN,CURSOR