class Result:
    
    #do I need "player", "name" as arguments in init? or ID is the reference
    def __init__(self, player_id, game_id):
        self.player_id = player_id
        self.game_id = game_id
        self.score = 0
    #player getter
    @property
    def player(self):
        return self._player
    
    #player setter
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise TypeError("Must be of type Player")

    #game getter
    @property
    def game(self):
        return self._game

    #game setter
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise TypeError("Must be of type Game")

    #score getter
    @property
    def score(self):
        return self.score
    
    #score setter
    @score.setter
    def score(self, game):
        if isinstance(game, Game) and game.id == self.game_id:
            self._score = game.score
        else:
            raise TypeError("Must be of type Game")
        
#class methods
    #create_table
    @classmethod
    def create_table(cls):
        CURSOR.execute(
            """
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY,
                score INTEGER,
                player_id INTEGER,
                game_id INTEGER,
                FOREIGN KEY (player_id) REFERENCES players(id),
                FOREIGN KEY (game_id) REFERENCES games(id)
            );        
        """
        )
        CONN.commit()

    #drop table
    @classmethod
    def drop_table(cls):
        CURSOR.execute("""
            DROP TABLE IF EXISTS results;
            """)
        
    #update difficiculty scores
    @classmethod
    def update_scores(cls, player_id, game_id, score):
        CURSOR.execute(
            """
            UPDATE results
            SET score = ?
            WHERE player_id = ? and game_id = ?;
            """,
            (score, player_id, game_id),
        )
        CONN.commit()

    


from classes.player import Player
from classes.game import Game
from classes.__init__ import CONN,CURSOR