from Clases.Trainer import Trainer

class Leader(Trainer):
    
    def __init__(self, name, age, town, p1, p2):
        super().__init__(name, age)

        self.town = town
        self.pokemons = [p1, p2]