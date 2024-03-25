from Clases.Location import Location

class Town(Location):
    
    def __init__(self, name, leader):
        super().__init__()
        self.name = name
        self.leader = leader
        self.routes = []

    def battle_leader (self):
        leader = self.leader

    def heal_pokemon (self, pokemon):
        pass