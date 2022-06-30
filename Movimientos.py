from Superheroes import Superheroes


class Movimientos():

   def fight_defense(self,points_of_damage):
       if points_of_damage<=Superheroes.resistencia:
           return False
       else:
           Superheroes.energia_vital -=(points_of_damage-Superheroes.resistencia)


   def fight_attack(self, superheroe_to_attack):
       return superheroe_to_attack.fight_defense(Superheroes.fuerza)