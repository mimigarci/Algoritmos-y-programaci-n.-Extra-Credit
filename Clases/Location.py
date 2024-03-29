from Clases.Functions import Functions 
from Clases.Battle import Battle
class Location (Functions):
    
    def __init__(self):
        self.battle_cleared = False
        self.battle = Battle()



    def move (self, player, location_list):
        
        while True:
            option = input ("""
    1. Avanzar
    2. Retroceder
    
    ---> """)
            
            if option == "1":
                new_location = Location.foward(self, player, location_list)
                print (f"\nHas llegado a {new_location.name}\n")
                new_location.menu(player, location_list)
                break
            elif option == "2":
                new_location = Location.backwards(self, player, location_list)
                print (f"\nHas llegado a {new_location.name}\n")
                new_location.menu(player, location_list)
                break
            else:
                print ("\nOpción inválida\n")


    def foward (self, player, locations_list):
        
        player_location = player.location
        location = locations_list.index(player_location)
        foward = location +1

        try:
            new_location = locations_list[foward]
            player.location = new_location

        except IndexError:
            print ("No puedes avanzar más.")

        return new_location

    
    def backwards (self, player, locations_list):
        
        player_location = player.location
        location = locations_list.index(player_location)
        backwards = location -1

        try:
            new_location = locations_list[backwards]
            player.location = new_location
            
        except IndexError:
            print ("No puedes retroceder más.")

        return new_location
