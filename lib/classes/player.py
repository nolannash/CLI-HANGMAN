from classes.__init__ import CONN, CURSOR

class Player:

    def __init__(self, name, username, password, id=None):
        self.name = name
        self.username = username
        self.password = int(password)
        self.id = id
        


#instance properties/attributes
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name,str) and 0<len(name)<=20:
            self._name = name
        else:
            raise AttributeError('Your name must be a String of 20 characters or less')

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self,username):
        if isinstance(username,str) and 0< len(username)<=20:
            self._username = username
        else:
            raise AttributeError('Please Enter A Valid Name')
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,pin):
        if isinstance(pin,int):
            self._password = pin
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

    #validate username
    @classmethod
    def auth_user(cls, username, password):
        CURSOR.execute(
            """
            SELECT * FROM players
            WHERE username = ? AND password = ?
            """, (username, password)
        )
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[0]) if row else None

    @classmethod
    def create_table(cls):
        CURSOR.execute(
            """
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY,
                name TEXT,
                username TEXT,
                password INTEGER
            );        
        """
        )
        CONN.commit()

    @classmethod
    def create(cls, name,username,password):
        new_player = Player(name,username,password)
        new_player.save()
        return new_player

    
    @classmethod #drop_table
    def drop_table(cls):
        CURSOR.execute("""
            DROP TABLE IF EXISTS players;
        """
        )
        CONN.commit()

    @classmethod #find_by_id
    def find_by_id(cls, id):
        if isinstance(id, int) and id > 0:
            CURSOR.execute("""
            SELECT * FROM players
            WHERE id =?;
            """, (id,),
            )
            row = CURSOR.fetchone()
            return cls(row[1], row[2], row[0]) if row else None