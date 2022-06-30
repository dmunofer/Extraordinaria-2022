from Superheroes import Superheroes
from random import randint
class NoHumano(Superheroes):

    def __init__(self, id, alias, id_secret, inteligencia, fuerza, velocidad, resistencia, proy_energia, hab_lucha):
        return Superheroes.__init__(self, id, alias, id_secret, inteligencia=randint(4,6), fuerza=randint(1,7), velocidad=randint(1,7),resistencia= randint(3,7), proy_energia=randint(3,7),hab_lucha=randint(3,6))