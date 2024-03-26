from Clases.Leader import Leader
from Clases.Player import Player
from Clases.Trainer import Trainer
from Clases.Town import Town
from Clases.Route import Route
from Clases.Pokemon import Pokemon
import pickle


#Pokemons:
pokemon1 = Pokemon("Litten", (70,70), (98,98), (60,60), 1, ["Scratch", "Growl", "Ember"])
pokemon2 = Pokemon("Turtwig", (83,83), (80,80), (96,96), 1, ["Tackle", "Growl", "Vine Whip"])
pokemon3 = Pokemon("Totodile", (75,75), (98,98), (96,96), 1, ["Scratch", "Leer", "Water Gun"])
pokemon4 = Pokemon("Charmander", (59,59), (78,78), (65,65), 1, ["Scratch", "Growl", "Ember"])
pokemon5 = Pokemon("Rowlet", (102,102), (82,82), (82,82), 1, ["Tackle", "Growl", "Leafage"])
pokemon6 = Pokemon("Mudkip", (75,75), (105,105), (75,75), 1, ["Tackle", "Growl", "Water Gun"])
pokemon7 = Pokemon("Tepig", (98, 98), (95,95), (68,68), 1, ["Scratch", "Tail Whip", "Ember"])
pokemon8 = Pokemon("Chespin", (84,84), (92,92), (98,98), 1, ["Tackle", "Growl", "Vine Whip"])
pokemon9 = Pokemon("Squirtle", (66,66), (72,72), (98,98), 1, ["Tackle", "Tail Whip", "Water Gun"])
pokemon10 = Pokemon("Pikachu", (75,75), (85,85), (60,60), 1, ["Spark", "Growl"])
pokemon11 = Pokemon("Butterfree", (90,90), (93,93), (98,98), 1, ["Air Slash", "Gust"])
pokemon12 = Pokemon("Kadabra", (65,65), (115,115), (75,75), 1, ["Psycho Cut", "Psybeam"])
pokemon13 = Pokemon("Graveler", (83,83), (125,125), (120,120), 1, ["Bulldoze", "Defense Curl"])
pokemon14 = Pokemon("Krookodile", (140,140), (137,137), (105,105), 1, ["Crunch", "Hone Claws", "Swagger"])
pokemon15 = Pokemon("Ninetails", (110,110), (115,115), (131,131), 1, ["Flamethrower", "Tail Whip", "Extrasensory"])
pokemon16 = Pokemon("Hariyama", (200,200), (120,120), (90,90), 1, ["Focus Punch", "Bulk Up", "Endure", "Force Palm"])
pokemon17 = Pokemon("Dragonite", (136,136), (175,175), (146,146), 1, ["Dragon Rush", "Dragon Tail", "Wing Attack", "Leer"])

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
