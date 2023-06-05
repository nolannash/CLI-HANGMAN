class Player:
    def __init__(self,name):
        self.name = name

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
#     results: [[easy games][med_games][hard_games]]