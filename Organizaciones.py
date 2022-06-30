from Superheroes import Superheroes
from Movimientos import Movimientos

class Organizaciones(Superheroes):

    def __init__(self, name, heroes_list):
        if type(name) is str:
            self.name = name
        else:
            raise ValueError("Name is not a string")
        if type(heroes_list) is list and len(heroes_list)>0:
            self.heroes_list= heroes_list
        else:
            raise ValueError("Heroes list empty or not a list")

    def is_undefeated(self):
        is_undefeated = False
        for heroe in self.heroes_list:
            if heroe.is_alive():
                is_undefeated=True
        return is_undefeated

    def surrender(self):
        for heroe in self.heroes_list:
            heroe.energia_vital=0

    def __str__(self):
        cadena= str(Superheroes.alias)+ " with a "+ str(Movimientos.name)+ " and health: "+ str(Superheroes.energia_vital)
        return cadena
    def __repr__(self):
        cadena= str(Superheroes.id) + 'with name '+ str(Superheroes.alias)+ 'and move: '+ str(Movimientos.name)

