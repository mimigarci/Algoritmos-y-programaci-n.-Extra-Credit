from Clases.Leader import Leader as Leader
from Clases.Trainer import Trainer as Trainer
from Clases.Town import Town as Town
from Clases.Route import Route as Route
from Clases.Pokemon import Pokemon as Pokemon
from Clases.Movement import Movement as Movement
import pickle


#Moves
moves = []
movements = [
        {
        "name": "Scratch",
        "decription": "Daña al oponente",
        "power": 40,
        "effect": {"debuff": None,"buff": None},
        },
        {
            "name": "Growl",
            "decription": "Reduce el ataque del opotente",
            "power": None,
            "effect": {"debuff": {"atk": 1/5, "def": None},"buff": None}
        },
        {
            "name": "Tackle",
            "decription": "Daña al oponente",
            "power": 40,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Leer",
            "decription": "Reduce la defensa del oponente",
            "power": None,
            "effect": {"debuff": {"atk": None, "def": 1/5},"buff": None}
        },
        {
            "name": "Ember",
            "decription": "Daña al oponente",
            "power": 40,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Water Gun",
            "decription": "Daña al oponente",
            "power": 40,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Vine Whip",
            "decription": "Daña al oponente",
            "power": 45,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Tail Whip",
            "decription": "Reduce la defensa del oponente",
            "power": None,
            "effect": {"debuff": {"atk": None, "def": 1/5},"buff": None}
        },
        {
            "name": "Spark",
            "decription": "Daña al oponente y reduce levemente su defensa, y aumenta el ataque del usuario",
            "power": 65,
            "effect": {"debuff": {"atk": None, "def": 1/10},"buff": {"atk": 1/3, "def": None}}
        },
        {
            "name": "Air Slash",
            "decription": "Daña al oponente y reduce su ataque levemente",
            "power": 75,
            "effect": {"debuff": {"atk": 1/10, "def": None},"buff": None}
        },
        {
            "name": "Gust",
            "decription": "Daña al oponente",
            "power": 40,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Psycho Cut",
            "decription": "Daña al oponente y aumenta fuertemente el ataque del usuario",
            "power": 70,
            "effect": {"debuff": None,"buff": {"atk": 1/2, "def": None}}
        },
        {
            "name": "Psybeam",
            "decription": "Daña al oponente, reduce su defensa y su ataque levemente",
            "power": 65,
            "effect": {"debuff": {"atk": 1/10, "def": 1/10},"buff": None}
        },
        {
            "name": "Bulldoze",
            "decription": "Daña al oponente y reduce su defensa",
            "power": 60,
            "effect": {"debuff": {"atk": None, "def": 1/5},"buff": None}
        },
        {
            "name": "Defense Curl",
            "decription": "Aumenta la defensa del usuario",
            "power": None,
            "effect": {"debuff": None,"buff": {"atk": None, "def": 1/5}}
        },
        {
            "name": "Crunch",
            "decription": "Daña al oponente y reduce su defensa gravemente",
            "power": 60,
            "effect": {"debuff": {"atk": None, "def": 1/3},"buff": None}
        },
        {
            "name": "Hone Claws",
            "decription": "Aumenta la defensa y fuertemente el ataque del usuario ",
            "power": None,
            "effect": {"debuff": None,"buff": {"atk": 1, "def": 1/5}}
        },
        {
            "name": "Swagger",
            "decription": "Reduce gravemente la defensa del oponente y aumenta la defensa del usuario",
            "power": None,
            "effect": {"debuff": {"atk": None, "def": 1/2},"buff": {"atk": None, "def": 1/5}}
        },
        {
            "name": "Flamethrower",
            "decription": "Daña al oponente",
            "power": 90,
            "effect": {"debuff": None,"buff": None},
        },
        {
            "name": "Extrasensory",
            "decription": "Daña al oponente y reduce su defensa levemente",
            "power": 80,
            "effect": {"debuff": {"atk": None, "def": 1/10},"buff": None}
        },
        {
            "name": "Focus Punch",
            "decription": "Daña al oponente y aumenta muy fuertemente el ataque del usuario",
            "power": 150,
            "effect": {"debuff": None,"buff": {"atk": 3/2, "def": None}}
        },
        {
            "name": "Bulk Up",
            "decription": "Aumenta el ataque y la defensa del usuario",
            "power": None,
            "effect": {"debuff": None,"buff": {"atk": 1/5, "def": 1/5}}
        },
        {
            "name": "Endure",
            "decription": "Aumenta fuertemente la defensa del usuario",
            "power": None,
            "effect": {"debuff": None,"buff": {"atk": None, "def": 1/2}}
        },
        {
            "name": "Force Palm",
            "decription": "Daña al oponente y reduce su defensa levemente",
            "power": 60,
            "effect": {"debuff": {"atk": None, "def": 1/10},"buff": None}
        },
        {
            "name": "Dragon Rush",
            "decription": "Daña al oponente y aumenta el ataque del usuario",
            "power": 100,
            "effect": {"debuff": None,"buff": {"atk": 1/5, "def": None}}
        },
        {
            "name": "Dragon Tail",
            "decription": "Daña al oponente",
            "power": 60,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Wing Attack",
            "decription": "Daña al oponente",
            "power": 65,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Lick",
            "decription": "Daña al oponente y reduce su defensa",
            "power": 30,
            "effect": {"debuff": {"atk": None, "def": 1/5},"buff": None}
        },
        {
            "name": "Tail Glow",
            "decription": "Aumenta muy fuertemente el ataque del usuario",
            "power": None,
            "effect": {"debuff": None,"buff": {"atk": 1.5, "def": None}}
        },
        {
            "name": "Octazooka",
            "decription": "Daña al oponente y reduce su defensa",
            "power": 65,
            "effect": {"debuff": {"atk": None, "def": 1/5},"buff": None}
        },
        {
            "name": "Roar",
            "decription": "Reduce el ataque y la defensa del oponente",
            "power": None,
            "effect": {"debuff": {"atk": 1/5, "def": 1/5},"buff": None}
        },
        {
            "name": "Bite",
            "decription": "Daña al oponente",
            "power": 70,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Darkest Lariat",
            "decription": "Daña al oponente y reduce su defensa",
            "power": 85,
            "effect": {"debuff": {"atk": None, "def": 1/5},"buff": None}
        },
        {
            "name": "Curse",
            "decription": "Aumenta la defensa y el ataque del usuario, y reduce la defensa y el ataque del oponente",
            "power": None,
            "effect": {"debuff": {"atk": 1/5, "def": 1/5},"buff": {"atk": 1/5, "def": 1/5}}
        },
        {
            "name": "Razor Leaf",
            "decription": "Daña al oponente",
            "power": 65,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Leaf Storm",
            "decription": "Daña al oponente",
            "power": 130,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Ice Fang",
            "decription": "Daña al oponente y reduce su defensa levemente",
            "power": 65,
            "effect": {"debuff": {"atk": None, "def": 1/10},"buff": None}
        },
        {
            "name": "Screech",
            "decription": "Reduce gravemente la defensa del oponente",
            "power": None,
            "effect": {"debuff": {"atk": None, "def": 1/2},"buff": None}
        },
        {
            "name": "Slash",
            "decription": "Daña al oponente",
            "power": 70,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Hydro Pump",
            "decription": "Daña al oponente",
            "power": 110,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Dragon Breath",
            "decription": "Daña al oponente",
            "power": 60,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Scary Face",
            "decription": "Reduce la defensa y el ataque del oponente",
            "power": None,
            "effect": {"debuff": {"atk": 1/5, "def": 1/5},"buff": None}
        },
        {
            "name": "Fire Fang",
            "decription": "Daña al oponente",
            "power": 65,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Peck",
            "decription": "Daña al oponente",
            "power": 35,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Shadow Sneak",
            "decription": "Daña al oponente y aumenta el ataque del usuario",
            "power": 40,
            "effect": {"debuff": None,"buff": {"atk": 1/5, "def": None}}
        },
        {
            "name": "Pluck",
            "decription": "Daña al oponente",
            "power": 60,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Feather Dance",
            "decription": "Aumenta fuertemente el ataque del usuario",
            "power": None,
            "effect": {"debuff": None,"buff": {"atk": 1, "def": None}}
        },
        {
            "name": "Protect",
            "decription": "Aumenta fuertemente la defensa del usuario",
            "power": None,
            "effect": {"debuff": None,"buff": {"atk": None, "def": 1/2}}
        },
        {
            "name": "Rock Smash",
            "decription": "Daña al oponente y reduce su defensa gravemente",
            "power": 40,
            "effect": {"debuff": {"atk": None, "def": 1/2},"buff": None}
        },
        {
            "name": "Rock Throw",
            "decription": "Daña al oponente",
            "power": 50,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Water Pulse",
            "decription": "Daña al oponente",
            "power": 60,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Mud Shot",
            "decription": "Daña al oponente y reduce su ataque",
            "power": 55,
            "effect": {"debuff": {"atk": 1/5, "def": None},"buff": None}
        },
        {
            "name": "Seed Bomb",
            "decription": "Daña al oponente",
            "power": 80,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Wood Hammer",
            "decription": "Daña al oponente",
            "power": 120,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Iron Defense",
            "decription": "Aumenta fuertemente la defensa del usuario",
            "power": None,
            "effect": {"debuff": None,"buff": {"atk": None, "def": 1/2}}
        },
        {
            "name": "Nuzzle",
            "decription": "Daña al oponente",
            "power": 20,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Thunderbolt",
            "decription": "Daña al oponente",
            "power": 90,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Psyshock",
            "decription": "Daña al oponente",
            "power": 80,
            "effect": {"debuff": None,"buff": None}
        },
        {
            "name": "Psychic",
            "decription": "Daña al oponente y reduce su ataque y defensa",
            "power": 90,
            "effect": {"debuff": {"atk": 1/5, "def": 1/5},"buff": None}
        },
        {
            "name": "Earthquake",
            "decription": "Daña al oponente",
            "power": 100,
            "effect": {"debuff": None,"buff": None}
        },
    ]


for m in movements:
           moves.append(Movement(m["name"], m["description"], m["power"], m["effect"]))

#Pokemons:
pokemon1 = Pokemon("Litten", (70,70), (98,98), (60,60), 1, ["Scratch", "Growl", "Ember"], ["Lick", "Roar", "Bite", "Swagger", "Darkest Lariat", "Flamethrower", "Splash"])
pokemon2 = Pokemon("Turtwig", (83,83), (80,80), (96,96), 1, ["Tackle", "Growl", "Vine Whip"], ["Razor Leaf", "Curse", "Lick", "Bite", "Crunch", "Leaf Storm", "Splash"])
pokemon3 = Pokemon("Totodile", (75,75), (98,98), (96,96), 1, ["Scratch", "Leer", "Water Gun"], ["Bite", "Ice Fang", "Crunch", "Slash", "Screech", "Hydro Pump", "Splash"])
pokemon4 = Pokemon("Charmander", (59,59), (78,78), (65,65), 1, ["Scratch", "Growl", "Ember"], ["Dragon Breath", "Slash", "Scary Face", "Fire Fang", "Flamethrower", "Dragon Rush", "Splash"])
pokemon5 = Pokemon("Rowlet", (102,102), (82,82), (82,82), 1, ["Tackle", "Growl", "Vine Whip"], ["Peck", "Shadow Sneak", "Razor Leaf", "Pluck", "Feather Dance", "Wing Attack", "Splash"])
pokemon6 = Pokemon("Mudkip", (75,75), (105,105), (75,75), 1, ["Tackle", "Growl", "Water Gun"], ["Rock Smash", "Protect", "Rock Throw", "Water Pulse", "Screech", "Hydro Pump", "Splash"])
pokemon7 = Pokemon("Tepig", (98, 98), (95,95), (68,68), 1, ["Scratch", "Tail Whip", "Ember"], ["Defense Curl", "Mud Shot", "Tail Glow", "Roar", "Curse", "Flamethrower", "Splash"])
pokemon8 = Pokemon("Chespin", (84,84), (92,92), (98,98), 1, ["Tackle", "Growl", "Vine Whip"], ["Bite", "Seed Bomb", "Mud Shot", "Curse", "Roar", "Wood Hammer", "Splash"])
pokemon9 = Pokemon("Squirtle", (66,66), (72,72), (98,98), 1, ["Tackle", "Tail Whip", "Water Gun"], ["Bite", "Water Pulse", "Protect", "Octazooka", "Iron Defense", "Hydro Pump", "Splash"])
pokemon10 = Pokemon("Pikachu", (75,75), (85,85), (60,60), 1, ["Spark", "Growl"], ["Nuzzle", "Tail Glow", "Screech", "Thunderbolt", "Tail Whip", "Splash"])
pokemon11 = Pokemon("Butterfree", (90,90), (93,93), (98,98), 1, ["Air Slash", "Gust"], ["Tackle", "Endure", "Psybeam", "Iron Defense", "Splash"])
pokemon12 = Pokemon("Kadabra", (65,65), (115,115), (75,75), 1, ["Psycho Cut", "Psybeam"], ["Protect", "Psyshock", "Psychic", "Splash"])
pokemon13 = Pokemon("Graveler", (83,83), (125,125), (120,120), 1, ["Bulldoze", "Defense Curl"], ["Rock Throw", "Mud Shot", "Earthquake", "Splash"])
pokemon14 = Pokemon("Krookodile", (140,140), (137,137), (105,105), 1, ["Crunch", "Hone Claws", "Swagger"], ["Earthquake", "Splash"])
pokemon15 = Pokemon("Ninetails", (110,110), (115,115), (131,131), 1, ["Flamethrower", "Tail Whip", "Extrasensory"], ["Fire Fang", "Splash"])
pokemon16 = Pokemon("Hariyama", (200,200), (120,120), (90,90), 1, ["Focus Punch", "Bulk Up", "Endure", "Force Palm"], ["Splash"])
pokemon17 = Pokemon("Dragonite", (136,136), (175,175), (146,146), 1, ["Dragon Rush", "Dragon Tail", "Wing Attack", "Leer"], ["Splash"])



#Pokemons:
pokemon1 = Pokemon("Litten", (70,70), (98,98), (60,60), 1, ["Scratch", "Growl", "Ember"])
pokemon2 = Pokemon("Turtwig", (83,83), (80,80), (96,96), 1, ["Tackle", "Growl", "Vine Whip"])
pokemon3 = Pokemon("Totodile", (75,75), (98,98), (96,96), 1, ["Scratch", "Leer", "Water Gun"])
pokemon4 = Pokemon("Charmander", (59,59), (78,78), (65,65), 1, ["Scratch", "Growl", "Ember"])
pokemon5 = Pokemon("Rowlet", (102,102), (82,82), (82,82), 1, ["Tackle", "Growl", "Vine Whip"])
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
route1 = Route(1, pokemon4)
route2 = Route(2, pokemon5)

#Pueblo Naranja
route3 = Route(3, pokemon6)
route4 = Route(4, pokemon7)

#Pueblo Amarillo
route5 = Route(5, pokemon8)
route6 = Route(6, pokemon9)

#Pueblo Verde
route7 = Route(7, pokemon10)
route8 = Route(8, pokemon11)

#Pueblo Azul
route9 = Route(9, pokemon12)
route10 = Route(10, pokemon13)

#Pueblo Morado
route11 = Route(11, pokemon14)
route12 = Route(12, pokemon15)

#Liga Pokemon
route13 = Route(13, pokemon16)
route14 = Route(14, pokemon17)

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


pokemons = [pokemon1, pokemon2, pokemon3, # Opciones starter
            pokemon4, pokemon5, # Pokemons rutas: 1, 2  
            pokemon6, pokemon7, # Pokemons rutas: 3, 4
            pokemon8, pokemon9, # Pokemons rutas: 5, 6  
           pokemon10, pokemon11, # Pokemons rutas: 7, 8                                         
           pokemon12, pokemon13, # Pokemons rutas: 9, 10
           pokemon14, pokemon15, # Pokemons rutas: 11, 12
           pokemon16, pokemon17] # Pokemons rutas: 13, 14

locations =  [route1, route2, red_town, route3, route4, orange_town, route5, route6, yellow_town, 
              route7, route8, green_town, route9, route10, blue_town,  route11, route12, 
              purple_town, route13, route14, league]

trainers = [comp_region1, comp_region2, comp_region3, league_leader]

#Assign moves to pokemons
for p in pokemons:
           for m in p.movements:
                      for move in moves:
                                 if move.name == m:
                                            p.movements[p.movements.index(m)] = move
           for m in p.learnset:
                      for move in moves:
                                 if move.name == m:
                                            p.learnset[p.learnset.index(m)] = move


main_data = [pokemons, locations, trainers]

#Dump info in pickle
                                        
def dump_info_in_pickle ():
    with open("Db\Database.pickle", "wb") as f:
        pickle.dump(main_data, f)

dump_info_in_pickle()