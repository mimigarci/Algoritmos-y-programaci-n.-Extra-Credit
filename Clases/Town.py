from Clases.Location import Location
from Clases.Battle import Battle as Battle
from Clases.Functions import Funtions as Fun

class Town(Location):
    
    def __init__(self, name, leader):
        super().__init__()
        self.name = name
        self.leader = leader

    def battle_leader (self, player):
        if self.battle_cleared == False:
            leader = self.leader
            self.battle_cleared = Battle.battle_trainer(player, leader)
        else:
            print("Ya has ganado esta batalla!")

    def heal_pokemon (self, player):
        
        for i in player.pokemons:
            print(f"{player.pokemons.index(i)+1}{i.name}")
        pokemon_to_heal = input ("Pokemon que desea sanar: ")

        for i in player.pokemons:
            if pokemon_to_heal == player.pokemons.index(i)+1 and i.HP[0] < i.HP[1]:
                i.HP = (i.HP[1], i.HP[1])
            else:
                continue
        
    def town_menu (self, player, locations_list):

        options = ["Sanar a mi pokemon", "Luchar contra el líder", "Avanzar", "Retroceder"]
        choice = Fun.manage_options(options)
        
        if choice == "1":
            Town.heal_pokemon(self, player)
            
        elif choice == "2":
            Town.battle_leader()

        elif choice == "3":
            player.location = Town.foward(self, player.location, locations_list)

        elif choice == "4":
            player.location = Town.backwards(self, player.location, locations_list)

        else:
            print ("\nOpción inválida\n")
