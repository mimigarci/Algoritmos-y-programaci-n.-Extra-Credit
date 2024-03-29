from Clases.Player import Player
from Clases.Town import Town
from Clases.Battle import Battle
from Clases.Functions import Functions as Fun
import pickle
import os

class App:

    def __init__(self):
        self.pokemons = []
        self.locations = []
        self.trainers = []
        self.player = ""
        self.battle = Battle()


    def read_data (self, file_name):
        with open(file_name, "rb") as f:
            info = pickle.load(f)

            self.pokemons = info[0]
            self.locations = info[1]
            self.trainers = info[2]
            self.player = info[3]
       
    def menu (self):
        os.system('cls')
        while True:
            
            options = ["Empezar una partida nueva", "Cargar Partida", "Salir"]
            option = Fun.manage_options(options)
            
            if option == 1:
                
                saves = ["Guardado 1", "Guardado 2", "Guardado 3"]
                select = Fun.manage_options(saves)
                App.read_data(self, "Db\Database.pickle")

                if select == 1:
                    App.register_user(self, self.locations, self.pokemons, self.trainers, "Db\Save1.pickle")
                    break
                elif select == 2:
                    App.register_user(self, self.locations, self.pokemons, self.trainers, "Db\Save2.pickle")
                    break
                elif select == 3:
                    App.register_user(self, self.locations, self.pokemons, self.trainers, "Db\Save3.pickle")
                    break
                else:
                    pass

            elif option == 2:
                
                saves = ["Guardado 1", "Guardado 2", "Guardado 3"]
                select = Fun.manage_options(saves)
                
                if select == 1:
                    App.read_data(self,"Db\Save1.pickle")
                    App.start_game(self, self.player, self.locations, self.pokemons, self.trainers, "Db\Save1.pickle")
                    break
                elif select == 2:
                    App.read_data(self,"Db\Save2.pickle")
                    App.start_game(self, self.player, self.locations, self.pokemons, self.trainers, "Db\Save2.pickle")
                    break
                elif select == 3:
                    App.read_data(self,"Db\Save3.pickle")
                    App.start_game(self, self.player, self.locations, self.pokemons, self.trainers, "Db\Save3.pickle")
                    break
                else:
                    print ("\nOpción inválida\n")
                    
            elif option == 3:
                break
            
            else:
                print ("\nOpción inválida\n")


    def start_game(self, player, locations, pokemons, trainers, file_name):
        print ("\n...Comienza la aventura! ")
        player.location.menu(player, locations, pokemons, trainers, file_name)


    def user_select_pokemon (self, pokemon1, pokemon2, pokemon3):
        while True:
            starter_pokemon = input (f"""Seleccione un pokemon:
                1.{pokemon1.name}
                2.{pokemon2.name}
                3.{pokemon3.name}
                
                    ---> """)

            if starter_pokemon == "1":
                return pokemon1, pokemon2
            elif starter_pokemon == "2":
                return pokemon2, pokemon3
            elif starter_pokemon == "3":
                return pokemon3, pokemon1
            else:
                print ("\nOpción inválida\n")


    def register_user (self, locations, pokemons, trainers, file_name):
        while True:
            print ("Bienvenido a tu aventura pokemon! ")

            name = input ("\n¿Cuál es tu nombre? ")
            age = input ("\nEdad: ")
            while not age.isnumeric():
                age = input("\nEsa no puede ser tu edad! Edad (en números): ")
            regiones = ["Barinas", "Maracaibo", "Zona en Reclamación"]
            region = Fun.manage_options(regiones)

            if region == 1:
                partner = self.trainers[0]
                pokemon1 = self.pokemons[0]
                pokemon2 = self.pokemons[1]
                pokemon3 = self.pokemons[2]

                selected_pokemon1, selected_pokemon2 = App.user_select_pokemon(self, pokemon1, pokemon2, pokemon3)
                partner.pokemons.append(selected_pokemon2)
                
                print (f"Tu compañero es {partner.name} y tu pokemon inicial es {selected_pokemon1.name}!")

                player = Player(name, age, region, partner)
                player.pokemons.append(selected_pokemon1)
                player.location = self.locations[0]
                self.player = player

                #Primera batalla (Contra el compañero)
                App.first_battle(self, player, locations, pokemons, trainers, file_name)
                break


            elif region == 2:
                partner = self.trainers[1]
                pokemon4 = self.pokemons[3]
                pokemon5 = self.pokemons[4]
                pokemon6 = self.pokemons[5]

                selected_pokemon1, selected_pokemon2 = App.user_select_pokemon(self, pokemon4, pokemon5, pokemon6)
                partner.pokemons.append(selected_pokemon2)
                
                print (f"Tu compañero es {partner.name} y tu pokemon inicial es {selected_pokemon1.name}!")

                player = Player(name, age, region, partner)
                player.pokemons.append(selected_pokemon1)
                player.location = self.locations[0]
                self.player = player

                #Primera batalla (Contra el compañero)
                App.first_battle(self, player, locations, pokemons, trainers, file_name)
                break
                    

            elif region == 3:
                partner = self.trainers[2]
                pokemon7 = self.pokemons[6]
                pokemon8 = self.pokemons[7]
                pokemon9 = self.pokemons[8]

                selected_pokemon1, selected_pokemon2 = App.user_select_pokemon(self, pokemon7, pokemon8, pokemon9)
                partner.pokemons.append(selected_pokemon2)
                
                print (f"Tu compañero es {partner.name} y tu pokemon inicial es {selected_pokemon1.name}!")

                player = Player(name, age, region, partner)
                player.pokemons.append(selected_pokemon1)
                player.location = self.locations[0]
                self.player = player

                #Primera batalla (Contra el compañero)
                App.first_battle(self, player, locations, pokemons, trainers, file_name)

            
                

    def first_battle (self, player, locations, pokemons, trainers, file_name):
        while True:
            battle = Battle.battle_trainer(self.battle, player, player.partner)
            
            if battle == True:
                Town.heal_pokemon(Town, player)
                App.start_game(self, player, locations, pokemons, trainers, file_name)
            else:
                print ("\nNo has derrotado a tu oponente, vamos a sanar a tu pokemon para que lo vuelvas a intentar!")
                Town.heal_pokemon(Town, player)
            
