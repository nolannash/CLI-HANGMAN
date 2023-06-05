class Player:
    def __init__(self,name, username):
        self.name = name
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

#instance methods

#class methods
    @classmethod
    def create_table(cls):
        ...
        
# player:
#     id:1
#     name: nolan
#     results: [[easy games:[score:word][score:word]][med_games][hard_games]]