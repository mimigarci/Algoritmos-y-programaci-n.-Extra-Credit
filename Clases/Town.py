from Clases.Location import Location
from Clases.Battle import Battle as Battle
from Clases.Functions import Functions as Fun

class Town(Location):
    
    def __init__(self, name, leader):
        super().__init__()
        self.name = name
        self.leader = leader
        self.battle = Battle()

    def heal_pokemon (self, player):
        
        for i in player.pokemons:
            print(f"{player.pokemons.index(i)+1}. {i.name}")

        pokemon_to_heal = input ("\nPokemon que desea sanar: ")
        
        try:
            pokemon_to_heal = int (pokemon_to_heal)
            player_pokemons = len(player.pokemons)

            for i in player.pokemons:
                if player_pokemons > 0:
                    player_pokemons -= 1
                    if pokemon_to_heal == player.pokemons.index(i)+1:
                        aux = i.HP[1]
                        i.HP = (aux, i.HP[1])
                        print ("\n=== Pokemon sano ===\n")
                        break
                    else:
                        continue
                else:
                    break
        
        except ValueError:
            pokemon_to_heal = input ("\nNúmero inválido. Pokemon que desea sanar: ")
            
        
    def menu (self, player, locations_list):

        while True:
            options = ["Sanar a mi pokemon", "Luchar contra el líder", "Moverse"]
            choice = Fun.manage_options(options)
            
            if choice == 1:
                Town.heal_pokemon(self, player)
                
            elif choice == 2:
                Town.battle_leader(self, player, self.leader, locations_list)

            elif choice == 3:
                if self.battle_cleared == False:
                    print ("\nDebes derrotar al líder antes de salir de la ciudad!\n")
                else:
                    player.location.move(player, locations_list) 

            else:
                print ("\nOpción inválida\n")

    def battle_leader (self, player, oponent, location_list):

        location = player.location

        print (f"\nTu batalla es contra {oponent.name}")

        if self.battle_cleared == False:
            leader = self.leader
            self.battle_cleared = Battle.battle_trainer(self.battle, player, leader)
            player.towns = player.unlocked_towns(location_list)

            if self.battle_cleared == True:
                print ("\nFelicidades, has derrotado a tu oponente! Puedes acceder a la próxima zona.\n")
                self.move(player, location_list)

            else:
                print ("\nLo lamento, no has derrotado a tu oponente. Puedes sanar a tu pokemon en el pueblo más cercano.\n")

                if len(player.towns) > 0:
                    print ("Debes ir al pueblo más cercano para sanar a tu pokemon.")

                    unlocked_towns = []
                    for i in player.towns:
                        unlocked_towns.append(i.name)

                    selected_town = Fun.manage_options(unlocked_towns)

                    for i in player.towns:
                        if player.towns.index(i)+1 == selected_town:
                            i.menu
                            player.location = i
                        else:
                            continue
                else:
                    print ("No has llegado a ningún pueblo, vamos a sanar a tu pokemon para que lo vuelvas a intentar!")
                    Town.heal_pokemon(self, player)

        else:
            print("Ya has ganado esta batalla!")
            


           