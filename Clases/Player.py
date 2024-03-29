from Clases.Trainer import Trainer
from Clases.Town import Town

class Player(Trainer):
    
    def __init__(self, name, age, region, partner):
        super().__init__(name, age)

        self.region = region
        self.partner = partner
        self.pokemons = []
        self.location = ""
        self.towns = None

    def unlocked_towns (self, location_list):
        unlocked_towns = []
        registered_locations = len(location_list)

        if registered_locations > 0:
            for i in location_list:
                registered_locations -= 1
                if type(i) == Town:
                    if i.battle_cleared == True:
                        unlocked_towns.append(i)
                    else:
                        continue
                else:
                    continue
        else:
            print ("No hay pueblos desbloqueados. Debe ingresar a una ruta para llegar a uno.")

        return unlocked_towns