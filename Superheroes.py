
from random import randint
from Escenarios import Escenarios

class Superheroes(Escenarios):

    def __init__(self, id, alias, id_secret, inteligencia, fuerza, velocidad, resistencia, proy_energia, hab_lucha  ):

        self.id = id
        self.alias = alias
        self._id_secret = id_secret
        self.inteligencia= inteligencia
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.resistencia= resistencia
        self.proy_energia = proy_energia
        self.hab_lucha= hab_lucha
        self.coste= (Escenarios.monedas_iniciales/Escenarios.miembros_equipo)*(self.inteligencia+self.fuerza+self.velocidad+self.resistencia+self.proy_energia+self.hab_lucha/30)
        self.energia= Escenarios.energia_vital*self.resistencia


    def get_id(self):
        return self.id
    def get_alias(self):
        return self.alias
    def get_id_secret(self):
        return self._id_secret
    def get_inteligencia(self):
        return self.inteligencia
    def get_fuerza(self):
        return self.fuerza
    def get_velocidad(self):
        return self.velocidad
    def get_resistencia(self):
        return self.velocidad
    def get_resistencia(self):
        return self.resistencia
    def get_proy_energia(self):
        return self.proy_energia
    def get_hab_lucha(self):
        return self.hab_lucha

    def is_alive(self):
        return self.energia_vital>0

    def set_id(self,new_id):
        self.id=new_id

    def set_alias(self,new_alias):
        self.alias=new_alias

    def set_id_secret(self,new_id_secret):
        self.id_secret=new_id_secret

    #Los demás setters no son necesarios ya que son estadísticas random que dependen de si el superheroe es humano o extraterrestre

