# from classes.player import Player
from classes.game import Game
from classes.result import Result

# from faker import Faker
# faker = Faker()

# Player.create_table()
# for _ in range(0,5):
#     Players.create(faker.name,faker.username,faker.password)

g1 = Game('Matteo',"Easy")
g1.play_hangman()
print('done')