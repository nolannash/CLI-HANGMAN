
class Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.letters_entered = set()
        self.word_to_be_guessed = ""

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