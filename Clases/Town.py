from Clases.Location import Location
from Clases.Battle import Battle as Battle
from Clases.Functions import Functions as Fun

class Town(Location):
    
    def __init__(self, name, leader):
        super().__init__()
        self.name = name
        self.leader = leader

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

    def battle_oponent (self, player, oponent, location_list):

        player = self.player
        location = self.player.location

        print (f"Tu batalla es contra {oponent.name}")

        if self.battle_cleared == False:
            leader = self.leader
            self.battle_cleared = Battle.battle_trainer(player, leader)

            if self.battle_cleared == True:
                print ("\nFelicidades, has derrotado a tu oponente! Puedes acceder a la próxima zona.\n")
                self.move(location, location_list)
                player.towns = player.unlocked_towns(location_list)

            else:
                print ("\nLo lamento, no has derrotado a tu oponente. Puedes sanar a tu pokemon en el pueblo más cercano.\n")
<<<<<<< Updated upstream
            
                if len(player.unlocked_towns) > 0:
                    print ("Debes ir al pueblo más cercano para sanar a tu pokemon.")
=======
>>>>>>> Stashed changes

                unlocked_towns = player.unlocked_towns (location_list)

                if len(unlocked_towns) > 0:
                    for i in player.towns:
                        unlocked_towns.append(i.name)
                    
                    selected_town = Fun.manage_options(unlocked_towns)

                    for i in location_list:
                        if location_list.index(i)+1 == selected_town:
                            i.town_menu
                            player.location = i
                        else:
                            continue
                else:
                    print ("No has llegado a ningún pueblo, vamos a sanar a tu pokemon para que lo vuelvas a intentar!")
                    Town.heal_pokemon(self, player)

        else:
            print("Ya has ganado esta batalla!")
            


           