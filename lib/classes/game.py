import random
from .player import Player
from .__init__ import CONN,CURSOR
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
    
    def __init__(self, player, difficulty,word='Easy'):

        self.difficulty = difficulty
        self.letters_entered = set()
        self.player = player
        self.set_word(self)
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
        return self.turns ==0 or self.letters_entered == set(list(self.word))

    def play_hangman(self):
        guessmade = self.letters_entered
        word = self._word
        turns = self.turns

        while turns > 0:
            main = ""

        for letter in word:
            if letter in guessmade:
                main += letter
            else:
                main += "_"
            main += " "

        if main == word:
            print(main)
            print("You win!")
            

        print("Guess the word:", main)
        guess = input().lower()

        if len(guess) != 1 or guess not in Game.VALID_LETTERS:
            print("Enter a single valid letter.")
            

        if guess in guessmade:
            print("You have already guessed that letter. Try again.")
            

        guessmade.add(guess)
        if guess not in word:
            turns -= 1

            if turns == 0:
                print("You lose!")
                print("You let a kind man die.")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                
            elif turns == 1:
                print("1 turn left")
                print("Last breaths counting, take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            elif turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            elif turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            elif turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            elif turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            elif turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            elif turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            elif turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            elif turns == 9:
                print("9 turns left")
                print("  --------  ")
        else:
            print("Enter a valid letter.")

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
