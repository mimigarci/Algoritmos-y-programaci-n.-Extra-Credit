from Clases.Location import Location

class Route(Location):
    
    def __init__(self, number, wild_pokemon):
        super().__init__()
        self.number = number
        self.wild_pokemon = wild_pokemon