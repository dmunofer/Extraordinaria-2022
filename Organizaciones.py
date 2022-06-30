

class Organizaciones():

    def __init__(self, name, heroes_list):
        if type(name) is str:
            self.name = name
        else:
            raise ValueError("Name is not a string")
        if type(heroes_list) is list and len(heroes_list)>0:
            self.heroes_list= heroes_list
        else:
            raise ValueError("Heroes list empty or not a list")