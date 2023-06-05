import random
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
,'Metamorphosis','Cryptocurrency','Serendipity'
,'Chrysanthemum','Nostalgia','Paradox','Phenomenon'
,'Ambiguous','Hieroglyphics','Synesthesia','Cacophony'
,'Epiphany','Xylophone','Quixotic','Onomatopoeia'
,'Kaleidoscope','Schadenfreude','Phantasmagoria','Esoteric'
,'Serendipity','Ubiquitous','Zealous','Capricious','Euphoria'
,'Aberration','Mellifluous','Labyrinth','Serendipity'
,'Pseudonym','Discombobulate','Mellifluous','Exacerbate'
,'Vexatious','Serendipity','Ineffable','Serendipity'
,'Perseverance','Unfathomable','Phantasmagoric','Serendipity'
,'Perspicacious','Conundrum','Serendipity','Mellifluous'
,'Inscrutable','Esoteric','Schadenfreude'
]
    def __init__(self, difficulty=None):
        self.difficulty = difficulty
        self.letters_entered = set()
        self.word_to_be_guessed = ""

    @property
    def word(self):
        return self._word
    @word.setter
    def word(self):
        if self.difficulty == "Easy":
            self._word = random.choice(Game.EASY_WORDS)
        elif self.difficulty == "Medium":
            self._word = random.choice(Game.MEDIUM_WORDS)
        else:
            self._word = random.choice(Game.HARD_WORDS)
    def enter_letter(self):
        letter_entered = input("Enter letter to guess: ")
        for letter in self.letters_entered:
            if letter_entered is not letter:
                self.letters_entered.add(letter_entered)
            else: 
                raise Exception("You already guessed that letter!")
            
    def game_status(self):
        for letter in self.word_to_be_guessed:
            if letter in self.letters_entered:
                print ("You have guessed the word!")
                return True
            
        return False

