from Clases.Leader import Leader
from Clases.Player import Player
from Clases.Trainer import Trainer
from Clases.Town import Town
from Clases.Route import Route
from Clases.Pokemon import Pokemon
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
        print ("Bienvenido a tu aventura pokemon! ")

        region = input ("""De qué región eres?
    
    1. Barinas
    2. Barinas
    3. Barinas
        
        ---> """)

        if region == "1":
            companion = self.trainers[0]
            starter_pokemon = input ("""Seleccione un pokemon:
        1.
        2.
        3.
        
            ---> """)
        elif region == "2":
            companion = self.trainers[1]
            starter_pokemon = input ("""Seleccione un pokemon:
        1.
        2.
        3.
        
            ---> """)
        elif region == "3":
            companion = self.trainers[2]
            starter_pokemon = input ("""Seleccione un pokemon:
        1.
        2.
        3.
        
            ---> """)

        else:
            print ("\nOpción inválida\n")



    def start (self):
        App.menu(self)
        
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
        print ("Bienvenido a tu aventura pokemon! ")

        region = input ("""De qué región eres?
    
    1. Barinas
    2. Barinas
    3. Barinas
        
        ---> """)

        if region == "1":
            companion = self.trainers[0]
            starter_pokemon = input ("""Seleccione un pokemon:
        1.
        2.
        3.
        
            ---> """)
        elif region == "2":
            companion = self.trainers[1]
            starter_pokemon = input ("""Seleccione un pokemon:
        1.
        2.
        3.
        
            ---> """)
        elif region == "3":
            companion = self.trainers[2]
            starter_pokemon = input ("""Seleccione un pokemon:
        1.
        2.
        3.
        
            ---> """)

        else:
            print ("\nOpción inválida\n")


        starter_pokemon = input ("")


    def get_location (self):
        pass

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
            print ("No hay pueblos desbloqueados")

        starter_pokemon = input ("")

