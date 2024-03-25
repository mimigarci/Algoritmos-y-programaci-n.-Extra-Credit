from Clases.Leader import Leader
from Clases.Player import Player
from Clases.Trainer import Trainer
from Clases.Town import Town
from Clases.Route import Route
from Clases.Pokemon import Pokemon
class App:

    def __init__(self):
        self.pokemons = []
        self.locations = []
        self.trainers = []

    #Se debería de activar después de cada batalla
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
                    file_name = "Save1.pickle"
                elif select == "2":
                    file_name = "Save2.pickle"
                elif select == "3":
                    file_name = "Save3.pickle"
                else:
                    print ("Opción inválida")

            elif option == "2":
                
                select = input("""
        1. Guardado 1
        2. Guardado 2
        3. Guardado 3
            
            ---> """)
                
                if select == "1":
                    #pickle.load(Save1)
                    pass
                elif select == "2":
                    #pickle.load(Save2)
                    pass
                elif select == "3":
                    #pickle.load(Save3)
                    pass
                else:
                    print ("Opción inválida")
                

            elif option == "3":
                break
            else:
                print ("Opción inválida")

        

    def start (self):
        App.menu(self)
