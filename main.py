from Superheroes import Superheroes










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

