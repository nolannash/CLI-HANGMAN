from classes.player import Player
from classes.game import Game
from classes.result import Result
from classes.__init__ import CURSOR, CONN

# from faker import Faker
# faker = Faker()


Player.drop_table()
Player.create_table()

#create sample players (name, username, password)
player1 = Player.create("Nolan", "nln99", 4567)
player2 = Player.create("Kevin", "kvn11", 1234)
player3 = Player.create("Bob", "bob11", 8900)
player4 = Player.create("Jane", "jne99", 8888)

game1 = Game('Nolan','Easy')
game1.play_hangman()
print("sample data table created")
