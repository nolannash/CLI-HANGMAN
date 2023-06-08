class Result:
    
    #do I need "player", "name" as arguments in init? or ID is the reference
    def __init__(self, score, player_id, game_id):
        self.player_id = player_id
        self.game_id = game_id
        self.score = score
        self.id = None

    # #player getter
    # @property
    # def player(self):
    #     return self._player
    
    # #player setter
    # @player.setter
    # def player(self, player):
    #     if isinstance(player, Player):
    #         self._player = player
    #     else:
    #         raise TypeError("Must be of type Player")

    # #game getter
    # @property
    # def game(self):
    #     return self._game

    # #game setter
    # @game.setter
    # def game(self, game):
    #     if isinstance(game, Game):
    #         self._game = game
    #     else:
    #         raise TypeError("Must be of type Game")

    #score getter
    @property
    def score(self):
        return self._score
    
    #score setter
    @score.setter
    def score(self, score):
        if isinstance(score, int):
            self._score = score
        else:
            raise TypeError("Must be of type Game")
    
    def update_game_result(self, score, game_id):
        CURSOR.execute("""
            UPDATE results
            SET score =?
            WHERE game_id =?;
        """, (score, game_id)
        )
        CONN.commit()

    #save
    def save(self):
        CURSOR.execute (
            """
            INSERT INTO results (score, player_id, game_id)
            VALUES (?, ?, ?)
        """,
            (self.score, self.player_id, self.game_id)
        )
        CONN.commit()
        self.id = CURSOR.lastrowid

#class methods
    #create
    @classmethod
    def create(cls, score, player_id, game_id):
        new_result = Result(score, player_id, game_id)
        # new_result.score = score
        new_result.save()
        return new_result
   
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
    
    def update_game_result(self, game_id, score):
        CURSOR.execute(
            """
            UPDATE results
            SET score = ?
            WHERE game_id = ?;
            """,
            (score, game_id),
        )
        CONN.commit()

    @classmethod
    def find_by_game(cls, game_id):
        CURSOR.execute(
            """
            SELECT * FROM results
            WHERE game_id = ?;
            """, (game_id, )
        )
        row = CURSOR.fetchone()
        if row:
            result = Result(row[1], row[2], row[3])  # Adjust the parameter order if necessary
            return result
        else:
            return None


from classes.player import Player
from classes.game import Game
from classes.__init__ import CONN,CURSOR