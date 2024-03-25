from Clases.Trainer import Trainer

class Player(Trainer):
    
    def __init__(self, name, age, region):
        super().__init__(name, age)

        self.region = region
        self.partner = ""
        self.pokemons = []
        self.location = ""

