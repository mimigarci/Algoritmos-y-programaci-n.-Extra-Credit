from Clases.Leader import Leader
from Clases.Player import Player
from Clases.Trainer import Trainer
from Clases.Town import Town
from Clases.Route import Route
from Clases.Pokemon import Pokemon
from Clases.Battle import Battle
import pickle

class App:

    def __init__(self):
        self.pokemons = []
        self.locations = []
        self.trainers = []
        self.player = ""

    def read_data (self, file_name):
        with open(f"{file_name}", "rb") as f:
            info = pickle.load(f)

            self.pokemons = info[0]
            self.locations = info[1]
            self.trainers = info[2]

    #Aparece al entrar a una ciudad
    def save_data(self):
        pass
    
    def menu (self):
        while True:
            option = input ("""

    1. Empezar una partida nueva
    2. Cargar partida
    3. Salir                        

    ---> """)
            if option == "1":

                select = input("""
        1. Guardado 1
        2. Guardado 2
        3. Guardado 3
            
            ---> """)
                
                if select == "1":
                    App.start_game(self, "Db\Save1.pickle")
                elif select == "2":
                    App.start_game(self, "Db\Save2.pickle")
                elif select == "3":
                    App.start_game(self, "Db\Save3.pickle")
                else:
                    print ("Opción inválida")

            elif option == "2":
                
                select = input("""
        1. Guardado 1
        2. Guardado 2
        3. Guardado 3
            
            ---> """)
                
                if select == "1":
                    App.read_data(self, "Db\Save1.pickle")
                    App.start_game(self, "Db\Save1.pickle")
                    
                elif select == "2":
                    App.read_data(self, "Db\Save2.pickle")
                    App.start_game(self, "Db\Save2.pickle")
                    
                elif select == "3":
                    App.read_data(self, "Db\Save3.pickle")
                    App.start_game(self, "Db\Save3.pickle")
                    
                else:
                    print ("\nOpción inválida\n")
                

            elif option == "3":
                break
            else:
                print ("Opción inválida")


    def start_game(self, file_name):
        while True:
            print ("Bienvenido a tu aventura pokemon! ")

            name = input ("\n¿Cuál es tu nombre? ")
            age = input ("\nEdad: ")
            region = input ("""\nDe qué región eres?
        
        1. Barinas
        2. Maracaibo
        3. Zona en reclamación
            
            ---> """)

            if region == "1":
                partner = self.trainers[0]
                pokemon1 = self.pokemons[0]
                pokemon2 = self.pokemons[1]
                pokemon3 = self.pokemons[2]

                selected_pokemon = App.select_pokemon(self, pokemon1, pokemon2, pokemon3)

                print (f"Tu compañero es {partner} y tu pokemon inicial es {selected_pokemon.name}!")

                player = Player(name, age, region, partner)
                player.location = self.locations[0]

                print ("\n...Comienza la aventura! ")


            elif region == "2":
                partner = self.trainers[1]
                pokemon4 = self.pokemons[3]
                pokemon5 = self.pokemons[4]
                pokemon6 = self.pokemons[5]

                selected_pokemon = App.select_pokemon(self, pokemon4, pokemon5, pokemon6)

                print (f"Tu compañero es {partner} y tu pokemon inicial es {selected_pokemon.name}!")

                player = Player(name, age, region, partner)
                player.location = self.locations[0]

                print ("\n...Comienza la aventura! ")

                break
            

            elif region == "3":
                partner = self.trainers[2]
                pokemon7 = self.pokemons[6]
                pokemon8 = self.pokemons[7]
                pokemon9 = self.pokemons[8]

                selected_pokemon = App.select_pokemon(self, pokemon7, pokemon8, pokemon9)

                print (f"Tu compañero es {partner} y tu pokemon inicial es {selected_pokemon.name}!")

                player = Player(name, age, region, partner)
                player.location = self.locations[0]

                print ("\n...Comienza la aventura! ")

                break
            else:
                print ("\nOpción inválida\n")



    def select_pokemon (self, pokemon1, pokemon2, pokemon3):
        while True:
            starter_pokemon = input (f"""Seleccione un pokemon:
                1.{pokemon1.name}
                2.{pokemon2.name}
                3.{pokemon3.name}
                
                    ---> """)

            if starter_pokemon == "1":
                return pokemon1
            elif starter_pokemon == "2":
                return pokemon2
            elif starter_pokemon == "3":
                return pokemon3
            else:
                print ("\nOpción inválida\n")


    def unlocked_towns_menu (self):
        unlocked_towns = []
        registered_locations = len(self.locations)

        if registered_locations > 0:
            for i in self.locations:
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


    def battle_menu (self, oponent):
        player = self.player
        location = self.player.location
        location_list = self.locations

        print (f"Tu batalla es contra {oponent.name}")
        if Battle.battle_trainer(self, player, oponent) == True:
            print ("\nFelicidades, has derrotado a tu oponente! Puedes acceder a la próxima zona.\n")
            Town.move(self, location, location_list)
        else:
            print ("\nLo lamento, no has derrotado a tu oponente. Puedes sanar a tu pokemon en el pueblo más cercano.\n")
            
            if len(App.unlocked_towns_menu(self)) > 0:
                print (App.unlocked_towns_menu(self))
            else:
                print ("No has llegado a ningún pueblo, vamos a sanar a tu pokemon para que lo vuelvas a intentar!")
                Town.heal_pokemon(self, player)

