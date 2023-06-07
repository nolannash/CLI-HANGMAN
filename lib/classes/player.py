

class Player:

    def __init__(self,name, username, password):

        self.name = name
        self.username = username
        self.password = int(password)


#instance properties/attributes

    #name getter
    @property
    def name(self):
        return self._name
    #name setter
    @name.setter
    def name(self,name):
        if isinstance(name,str) and 0 < len(name) <= 20:
            self._name = name
        else:
            raise AttributeError('Your name must be a String of 20 characters or less')
        
    #username getter
    @property
    def username(self):
        return self._username
    
    #username setter
    @username.setter
    def username(self,username):
        if isinstance(username,str) and 0< len(username)<=20:
            self._username = username
        else:
            raise AttributeError('Please Enter A Valid Name')

    #password getter -> do we want to let the user get the password?
    @property
    def password(self):
        return self._password
    
    #password setter
    @password.setter
    def password(self,pin):
        if isinstance(pin,int):
            self._password = pin
        elif  pin != int:
            raise Exception('Your Pin Must Be A Sequence Of 4 Numbers')
        else:
            raise AttributeError('Please enter a valid password')
        
#instance methods

    #save()
    def save(self):
        CURSOR.execute(
            """
            INSERT INTO players(name, username, password)
            VALUES (?, ?, ?)
        """,
            (self.name, self.username, self.password),
        )
        CONN.commit()
        self.id = CURSOR.lastrowid

#class methods

    #create_table()
    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY,
                name TEXT,
                username TEXT,
                password INTEGER,
                easy_score INTEGER,
                medium_score INTEGER,
                hard_score INTEGER    
            );        
        """
        )
        CONN.commit()
    
    #create()
    @classmethod
    def create(cls,name,username,password):
        new_player = Player(name,username,password)
        new_player.save()
        return new_player

    #drop_table
    @classmethod
    def drop_table(cls):
        CURSOR.execute("""
            DROP TABLE IF EXISTS players;
        """
        )
        CONN.commit()

    #find_by_id
    @classmethod 
    def find_by_id(cls, id):
        if isinstance(id, int) and id > 0:
            CURSOR.execute("""
            SELECT id, name, username FROM players
            WHERE id is ?;
            """, (id,),
            )
            row = CURSOR.fetchone()
            return cls(row[1], row[2], row[0]) if row else None


from classes.game import Game
from classes.result import Result
from classes.__init__ import CONN, CURSOR