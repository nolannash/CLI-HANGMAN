class Player:
    def __init__(self,name, username, password):
        self.name = name
        self.username = username
        self.password = password
        #keyword or password type thing to set player = username or not
        #you can enter into your "account" or create new user

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
        if isinstance(pin,int) and len(pin) ==4:
            self._password = pin
        elif len(pin) !=4 or pin != type(int):
            raise Exception('Your Pin Must Be A Sequence Of 4 Numbers')
        else:
            raise AttributeError('Please enter a valid password')
#instance methods

#class methods
    @classmethod
    def create_table(cls):
        ...
        
# player:
#     id:1
#     name: nolan
#     results: [[easy games:[score:word][score:word]][med_games][hard_games]]