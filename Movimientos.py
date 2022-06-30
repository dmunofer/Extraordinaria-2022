from Superheroes import Superheroes


class Movimientos():

    mov_attack= int(Superheroes.fuerza)*0.8+int(Superheroes.velocidad)+int(Superheroes.hab_lucha)*0.75+int(Superheroes.proy_energia)
    mov_def= int(Superheroes.inteligencia)+int(Superheroes.velocidad)*0.75+int(Superheroes.hab_lucha)*0.25+int(Superheroes.fuerza)*0.2




def fight_defense(self,points_of_damage):
       if points_of_damage<=Superheroes.resistencia:
           return False
       else:
           Superheroes.energia_vital -=(points_of_damage-Superheroes.resistencia)


def fight_attack(self, superheroe_to_attack):
       return superheroe_to_attack.fight_defense(Superheroes.fuerza)