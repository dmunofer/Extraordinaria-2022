from Superheroes import Superheroes



def get_data_from_user(filename):
    file= open(filename, "r")
    final= []
    for line in file.readlines():
      data= line.split(",")
      id= int(data[0])
      alias= data[1]
      id_secret= int(data[3])
      inteligencia= int(data[4])
      fuerza= int(data[5])
      velocidad= int(data[6])
      resistencia= int(data[7])
      proy_energia= int(data[8])
      hab_lucha= int(data[9])
      superheroe= Superheroes(id,id, alias, id_secret, inteligencia, fuerza, velocidad, resistencia, proy_energia, hab_lucha)
      final.append(superheroe)
    return final







def get_Superheroe_in_a_list_of_Superheroes(player,list_of_heroes):

    final=[]
    for heroe in list_of_heroes:
        if heroe.is_alive():
            final.append(heroe)
    for heroe in final:
        print(heroe)
    return final

def squad_is_undefeated(list_of_heroes):
    is_undefeated= False
    for heroe in list_of_heroes:
        if heroe.is_alive():
            is_undefeated=True
    return is_undefeated

