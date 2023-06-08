from classes.player import Player
from classes.game import Game
from classes.result import Result
from classes.__init__ import CURSOR, CONN
from helpers import make_tables

# # from faker import Faker
# # faker = Faker()

make_tables()
#create sample players (name, username, password)
player1 = Player.create("Nolan", "nln99", 4567)
player2 = Player.create("Kevin", "kvn11", 1234)
player3 = Player.create("Bob", "bob11", 8900)
player4 = Player.create("Jane", "jne99", 8888)


#games
game1 = Game('Easy')
game2 = Game('Hard')

game1.create("Easy")

#results
result1 = Result(player1.id, game1.id)
result2 = Result(player2.id, game2.id)

# result1.score = 90
# result2.score = 150


#results update scores
result1.update_scores(player1.id, game1.id, 90)
result2.update_scores(player2.id, game2.id, 150)


# game1.play_hangman()
print("sample data table created")
