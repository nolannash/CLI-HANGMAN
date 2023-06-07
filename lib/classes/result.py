class Result:
    
    #do I need "player", "name" as arguments in init? or ID is the reference
    def __init__(self, player_id, game_id):
        self.easy_score = 0
        self.medium_score = 0
        self.hard_score = 0
        self.player_id = player_id
        self.game_id = game_id

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

    #easy score getter
    @property
    def easy_score(self):
        return self.easy_score

    #easy score setter
    @easy_score.setter
    def easy_score(self, score):
        if isinstance(score, int):
            self.easy_score = score
        else:
            raise ValueError("Score must be an integer")
    
    #medium score getter
    @property
    def medium_score(self):
        return self.medium_score

    #medium score setter
    @medium_score.setter
    def medium_score(self, score):
        if isinstance(score, int):
            self.medium_score = score
        else:
            raise ValueError("Score must be an integer")
        
    #hard score getter
    @property
    def hard_score(self):
        return self.hard_score

    #hard score setter
    @hard_score.setter
    def hard_score(self, score):
        if isinstance(score, int):
            self.hard_score = score
        else:
            raise ValueError("Score must be an integer")
        
#class methods
    #create_table
    @classmethod
    def create_table(cls):
        CURSOR.execute(
            """
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY,
                easy_score INTEGER,
                medium_score INTEGER,
                hard_score INTEGER,
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
    def update_scores(cls, player_id, easy_score, medium_score, hard_score):
        CURSOR.execute(
            """
            UPDATE results
            SET easy_score = ?,
                medium_score = ?,
                hard_score = ?
            WHERE player_id = ?;
            """,
            (easy_score, medium_score, hard_score, player_id),
        )
        CONN.commit()

    


from .player import Player
from .game import Game
from .__init__ import CONN,CURSOR