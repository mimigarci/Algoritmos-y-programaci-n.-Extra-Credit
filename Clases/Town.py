from Clases.Location import Location
from Clases.Battle import Battle as Battle

class Town(Location):
    
    def __init__(self, name, leader):
        super().__init__()
        self.name = name
        self.leader = leader

    def battle_leader (self, player):
        leader = self.leader
        self.battle_cleared = Battle.battle_trainer(player, leader)

    def heal_pokemon (self, pokemon):
        pass

    def town_menu (self, player_location, file_name):
        
        choice = input (f""" Estás en el {self.name}!
                        
1. Sanar a mi pokemon
2. Luchar contra el líder
3. Moverse                        

""")
        
        if choice == "1":
            pass
