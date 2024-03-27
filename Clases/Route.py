from Clases.Location import Location
from Clases.Battle import Battle
import random

class Route(Location):
    
    def __init__(self, number, wild_pokemon):
        super().__init__()
        self.number = number
        self.wild_pokemon = wild_pokemon

    def encounter(self, player):
        if self.battle_cleared == False:
            if self.number in range(1, 5):
                self.battle_cleared = Battle.battle_pokemon(player, self.wild_pokemon)
            elif self.number in range(5, 9):
                aux = random.randrange(4)
                if aux in range(3):
                    self.battle_cleared = Battle.battle_pokemon(player, self.wild_pokemon)
            elif self.numer in range(9, 13)
                aux = random.randrange(2)
                if aux == 0:
                    self.battle_cleared = Battle.battle_pokemon(player, self.wild_pokemon)
            else:
                aux = random.randrange(100)
                if aux in range(2):
                    self.battle_cleared = Battle.battle_pokemon(player, self.wild_pokemon)
                
