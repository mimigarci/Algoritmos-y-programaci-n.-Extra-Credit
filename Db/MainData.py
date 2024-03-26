from Clases.Leader import Leader
from Clases.Player import Player
from Clases.Trainer import Trainer
from Clases.Town import Town
from Clases.Route import Route
from Clases.Pokemon import Pokemon
import pickle


#Pokemons:




#Rutas:

#Pueblo Rojo
route1 = Route(1, )
route2 = Route(2, )

#Pueblo Naranja
route3 = Route(3, )
route4 = Route(4, )

#Pueblo Amarillo
route5 = Route(5, )
route6 = Route(6, )

#Pueblo Verde
route7 = Route(7, )
route8 = Route(8, )

#Pueblo Azul
route9 = Route(9, )
route10 = Route(10, )

#Pueblo Morado
route11 = Route(11, )
route12 = Route(12, )

#Liga Pokemon
route13 = Route(13, )
route14 = Route(14, )

#Líderes:

red_town_leader = Leader("Andrés", 18, "Pueblo Rojo")
orange_town_leader = Leader("María", 19, "Pueblo Naranja")
yellow_town_leader = Leader("Jose", 20, "Pueblo Amarillo")
green_town_leader = Leader("Fernando", 21, "Pueblo Verde")
blue_town_leader = Leader("Luis", 18, "Pueblo Azul")
purple_town_leader = Leader("Michelle", 16, "Pueblo Morado")
league_leader = Leader("Ash Ketchum", 10, "Liga Pokemon")

#Compañeros:

comp_region1 = Trainer("Luis", 18)
comp_region2 = Trainer("Fernando", 17)
comp_region3 = Trainer("Michelle", 16)

#Pueblos:
red_town = Town("Pueblo Rojo", red_town_leader)
orange_town = Town("Pueblo Naranja", orange_town_leader)
yellow_town = Town("Pueblo Amarillo", yellow_town_leader)
green_town = Town("Pueblo Verde", green_town_leader)
blue_town = Town("Pueblo Azul", blue_town_leader)
purple_town = Town("Pueblo Morado", purple_town_leader)
league = Town("Liga Pokemon", league_leader)

pokemons = []

locations =  [route1, route2, red_town, route3, route4, orange_town, route5, route6, yellow_town, 
              route7, route8, green_town, route9, route10, blue_town,  route11, route12, purple_town, route13, route14, league]

trainers = [comp_region1, comp_region2, comp_region3, 
            red_town_leader, orange_town_leader, yellow_town_leader, 
            green_town_leader, blue_town_leader, purple_town_leader, league_leader]

main_data = [pokemons, locations, trainers]

#Dump info in pickle
with open("Db\Database.pickle", "wb") as f:
    pickle.dump(main_data, f)
