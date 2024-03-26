from Clases.Location import Location

class Town(Location):
    
    def __init__(self, name, leader):
        super().__init__()
        self.name = name
        self.leader = leader

    def battle_leader (self):
        leader = self.leader

    def heal_pokemon (self, player):
        
        for i in player.pokemons:
            print(f"{player.pokemons.index(i)+1}{i.name}")
        pokemon_to_heal = input ("Pokemon que desea sanar: ")

        for i in player.pokemons:
            if pokemon_to_heal == player.pokemons.index(i)+1 and i.HP[1] < 100:
                #Sanar pokemon
                pass
            else:
                continue
        
    def town_menu (self, player, locations_list):
        
        choice = input (f""" Estás en el {self.name}!
                        
1. Sanar a mi pokemon
2. Luchar contra el líder
3. Avanzar
4. Retroceder                        

""")
        
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
