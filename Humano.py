from Superheroes import Superheroes
from random import randint
class Humano(Superheroes):

    def __init__(self, id, alias, id_secret, inteligencia, fuerza, velocidad, resistencia, proy_energia, hab_lucha):
        return Superheroes.__init__(self, id, alias, id_secret, inteligencia=randint(3,7), fuerza=randint(1,6), velocidad=randint(2,5),resistencia= randint(2,5), proy_energia=randint(1,6),hab_lucha=randint(1,7))