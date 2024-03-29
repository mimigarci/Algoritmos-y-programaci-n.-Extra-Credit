from Clases.Location import Location
from Clases.Battle import Battle
import random

class Route(Location):
    
    def __init__(self, number, name, wild_pokemon):
        super().__init__()
        self.number = number
        self.name = name
        self.wild_pokemon = wild_pokemon
        self.battle = Battle ()

    def encounter(self, player):
        if self.battle_cleared == False:
            if self.number in range(1, 5):
                print (f"\nUn pokemon salvaje! {self.wild_pokemon.name} se ha atravesado en tu camino! ")
                self.battle_cleared = self.battle.battle_pokemon(player, self.wild_pokemon)
            elif self.number in range(5, 9):
                aux = random.randrange(4)
                if aux in range(3):
                    print (f"\nUn pokemon salvaje! {self.wild_pokemon.name} se ha atravesado en tu camino! ")
                    self.battle_cleared = self.battle.battle_pokemon(player, self.wild_pokemon)
            elif self.number in range(9, 13):
                aux = random.randrange(2)
                if aux == 0:
                    print (f"\nUn pokemon salvaje! {self.wild_pokemon.name} se ha atravesado en tu camino! ")
                    self.battle_cleared = self.battle.battle_pokemon(player, self.wild_pokemon)
            else:
                aux = random.randrange(100)
                if aux in range(2):
                    print (f"\nUn pokemon salvaje! {self.wild_pokemon.name} se ha atravesado en tu camino! ")
                    self.battle_cleared = self.battle.battle_pokemon(player, self.wild_pokemon)


    def menu (self, player, location_list, pokemons, trainers, file_name):
        
        for i in player.pokemons:
            if i.HP[0] > 0:
                self.encounter(player)
            else:
                continue

        next_location = self.move(player, location_list, pokemons, trainers, file_name)

        return next_location
                
