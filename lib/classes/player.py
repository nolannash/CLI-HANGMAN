from .__init__ import CONN, CURSOR
class Player:
    def __init__(self,name, username, password):
        self.name = name
        self.username = username
        self.password = int(password)


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
        elif  pin != int:
            raise Exception('Your Pin Must Be A Sequence Of 4 Numbers')
        else:
            raise AttributeError('Please enter a valid password')
#instance methods

#class methods
    @classmethod
    def create_table(cls):
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS players(
                id INTEGET PRIMARY KEY,
                name TEXT NOT NULL,
                password INTEGER
            );        
        ''')
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute("""
            DROP TABLE IF EXISTS players;
            """)

    @classmethod
    def create (cls,name,username,password):
        player = Player(name,username,password)
        CURSOR.execute(f'''
            INSERT INTO players (name, username, password)
            VALUES('{player.name}','{player.username}','{player.password}')
            ''')
        new_player_id = CURSOR.execute("SELECT last_insert_rowid() FROM players").fetchone()[0]
        CONN.commit()