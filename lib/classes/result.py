class Result:
    
    #do I need "player", "name" as arguments in init? or ID is the reference
    def __init__(self, score, player_id, game_id):
        self.player_id = player_id
        self.game_id = game_id
        self.score = score
        self.id = None

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
        
    #find max score
    @classmethod
    def find_max_score(cls):
        CURSOR.execute(
        """
        SELECT players.username AS player, results.score AS score
        FROM players
        INNER JOIN results
        ON players.id = results.player_id
        ORDER BY results.score DESC
        LIMIT 1;
        """
        )
        row = CURSOR.fetchone()
        if row:
            player_name, max_score = row
            return player_name, max_score
        else:
            return None
        
    @classmethod
    def get_top_scores(cls):
        CURSOR.execute(
        """
        SELECT players.username AS player, games.word AS word, results.score AS score
        FROM players
        INNER JOIN results ON players.id = results.player_id
        INNER JOIN games ON games.id = results.game_id
        ORDER BY results.score DESC
        LIMIT 3;
        """
        )
        rows = CURSOR.fetchall()
        if rows:
            top_scores = []
            for row in rows:
                player_name, word, score = row
                top_scores.append({"Player": player_name, "Word": word, "Score": score})
            return top_scores
        else:
            return None

from .player import Player
from .game import Game
from .__init__ import CONN,CURSOR