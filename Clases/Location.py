class Location:
    
    def __init__(self):
        self.battle_cleared = False

    def move (self, player_location, locations_list):
        
        choice = input ("""
    1. Avanzar
    2. Retroceder
        
    ---> """)
        
        if choice == "1":
            pass
        elif choice == "2":
            pass
        else:
            print ("\nOpción inválida\n")

    def foward (self, locations_list):
        pass
