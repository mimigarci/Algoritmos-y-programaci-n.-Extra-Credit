import random
from Clases.Functions import Functions as Fun
import sys

class Battle:
    def __init__(self):
        pass

    def dmg_calc(self, level, atk, defs, power):

        if level > 5:
            dmg = ((( level + 2 )* power *( atk/defs ))/20 ) + 2
        else:
            dmg = (((level + 2) * power *((2*atk)/defs))/15) + 2

        crit = random.randrange(1,3)

        dmg = dmg*crit

        if dmg == 1:
            rolls = 1
        else:
            rolls = (random.randrange(217, 256)) / 255

        dmg = dmg*rolls

        return int(dmg)

    def debuff_calc(self, stat, effect):
        stat = stat - stat*effect
        if stat < 1:
            stat = 1

        return int(stat)

    def buff_calc(self, stat, effect):
        stat = stat + stat*effect
        return int(stat)

    def change_pokemon(self, active_pokemon, player):
        if len(player.pokemons) > 1:
            last_pokemon = active_pokemon
            while last_pokemon == active_pokemon or active_pokemon.HP[0] >= 0:
                pokemons = []
                for p in player.pokemons:
                    pokemons.append(p.name)
                pokemon = Fun.manage_options(pokemons)
                for p in player.pokemons:
                    aux = p.name
                    if aux == pokemons[pokemon-1]:
                        if active_pokemon == p:
                            print("Ese es tu pokemon activo!")
                        else:
                            active_pokemon = p
                            print (f"Has cambiado tu pokemon a {active_pokemon.name}")
                            return active_pokemon
        else:
            print ("\nNo puedes cambiar de pokemon, solo tienes uno!")


    def players_turn(self, active_pokemon, enemy_pokemon, player):
        
        p_def = active_pokemon.defense[0]
        p_atk = active_pokemon.atk[0]
        e_hp = enemy_pokemon.HP[0]
        e_def = enemy_pokemon.defense[0]
        e_atk = enemy_pokemon.atk[0]

        options = ["Luchar", "Cambiar Pokemon"]
        option = Fun.manage_options(options)

        if option == 1:
            aux = []
            for m in active_pokemon.movements:
                aux.append(f"{m.name} ({m.description})")
            print("\nElige qué movimiento deseas que tu pokemon haga:")
            movement = Fun.manage_options(aux)
            for m in active_pokemon.movements:
                aux2 = f"{m.name} ({m.description})"
                if aux2 == aux[movement-1]:
                    if m != "Splash":
                        print(f"\nTu {active_pokemon.name} ha usado {m.name}!")
                        if m.power != None:
                            dmg = self.dmg_calc(active_pokemon.level, p_atk, e_def, m.power)
                            print(f"\nHa inflingido {dmg} puntos de daño")
                            e_hp -= dmg
                        if m.effects["debuff"] != None:
                            if m.effects["debuff"]["atk"] != None:
                                e_atk = self.debuff_calc(e_atk, m.effects["debuff"]["atk"])
                                print(f"\nHa reducido el ataque del {enemy_pokemon.name} oponente")
                            if m.effects["debuff"]["def"] != None:
                                e_def = self.debuff_calc(e_def, m.effects["debuff"]["def"])
                                print(f"\nHa reducido la defensa del {enemy_pokemon.name} oponente")
                        if m.effects["buff"] != None:
                            if m.effects["buff"]["atk"] != None:
                                p_atk = self.buff_calc(p_atk, m.effects["buff"]["atk"])
                                print(f"\nHa aumentado su ataque")
                            if m.effects["buff"]["def"] != None:
                                p_def = self.buff_calc(p_def, m.effects["buff"]["def"])
                                print(f"\nHa aumentado su defensa")
                    else:
                        print(f"\nTu {active_pokemon.name} ha usado Splash!")
                        aux3 = random.randrange(100)
                        if aux3 == 0:
                            print(f"\nWow que suerte! Ha inflingido {e_hp} puntos de daño")                            
                            e_hp -= e_hp
                        elif aux3 in range(1,21):
                            print(f"\nNada mal! Ha inflingido {(e_hp/2)} puntos de daño")
                            e_hp -= (e_hp/2)
                        else:
                            print("\nParece que no hizo nada...")
                            
        else:
            active_pokemon = self.change_pokemon(active_pokemon, player)

        if type(active_pokemon) == None:
            print ("\nNo tienes pokemones activos!")
            return
        else:
            p_def = active_pokemon.defense[0]
            p_atk = active_pokemon.atk[0]
            atk = (p_atk, active_pokemon.atk[1])
            defs = (p_def, active_pokemon.defense[1])
            active_pokemon.atk = atk
            active_pokemon.defense = defs
            hp = (e_hp, enemy_pokemon.HP[1])
            atk = (e_atk, enemy_pokemon.atk[1])
            defs = (e_def, enemy_pokemon.defense[1])
            enemy_pokemon.HP = hp
            enemy_pokemon.atk = atk
            enemy_pokemon.defense = defs

        return active_pokemon

    def enemy_turn(self, active_pokemon, enemy_pokemon):
        p_hp = active_pokemon.HP[0]
        p_def = active_pokemon.defense[0]
        p_atk = active_pokemon.atk[0]
        e_def = enemy_pokemon.defense[0]
        e_atk = enemy_pokemon.atk[0]

        movement = random.randrange(len(enemy_pokemon.movements))
        m = enemy_pokemon.movements[movement]
        
        if m != "Splash":
            print(f"\nEl {enemy_pokemon.name} oponente ha usado {m.name}!")
            
            if m.power != None:
                dmg = self.dmg_calc(active_pokemon.level, e_atk, p_def, m.power)
                print(f"\nHa inflingido {dmg} puntos de daño")
                p_hp -= dmg
                
            if m.effects["debuff"] != None:
                
                if m.effects["debuff"]["atk"] != None:
                    p_atk = self.debuff_calc(p_atk, m.effects["debuff"]["atk"])
                    print("\nHa reducido el ataque de tu pokemon")
                    
                if m.effects["debuff"]["def"] != None:
                    p_def = self.debuff_calc(p_def, m.effects["debuff"]["def"])
                    print("\nHa reducido la defensa de tu pokemon")
                    
            if m.effects["buff"] != None:
                
                if m.effects["buff"]["atk"] != None:
                    e_atk = self.buff_calc(e_atk, m.effects["buff"]["atk"])
                    print("\nHa aumentado su ataque")
                    
                if m.effects["buff"]["def"] != None:
                    e_def = self.buff_calc(e_def, m.effects["buff"]["def"])
                    print("\nHa reducido su ataque")
                    
        else:
            print(f"\nEl {enemy_pokemon.name} oponente ha usado Splash!")
            aux3 = random.randrange(100)
            
            if aux3 == 0:
                print(f"\nWow que suerte! Ha inflingido {p_hp} puntos de daño")                            
                p_hp -= p_hp
                
            elif aux3 in range(1,20):
                print(f"\nNada mal! Ha inflingido {(p_hp/2)} puntos de daño")
                p_hp -= (p_hp/2)
                
            else:
                print("\nParece que no hizo nada...")

        hp = (p_hp, active_pokemon.HP[1])
        atk = (p_atk, active_pokemon.atk[1])
        defs = (p_def, active_pokemon.defense[1])
        active_pokemon.HP = hp
        active_pokemon.atk = atk
        active_pokemon.defense = defs
        atk = (e_atk, enemy_pokemon.atk[1])
        defs = (e_def, enemy_pokemon.defense[1])
        enemy_pokemon.atk = atk
        enemy_pokemon.defense = defs

    def level_up(self, pokemon):
        pokemon.level += 1
        aux = random.randrange(3)
        pokemon.HP = (pokemon.HP[0]+aux, pokemon.HP[1]+aux)
        aux = random.randrange(3)
        pokemon.atk = (pokemon.atk[0]+aux, pokemon.atk[1]+aux)
        aux = random.randrange(3)
        pokemon.defense = (pokemon.defense[0]+aux, pokemon.defense[1]+aux)
        
        if pokemon.level > 1 and not pokemon.level%2==0:
            pokemon.movements.append(pokemon.learnset[0])
            if pokemon.learnset[0] != "Splash":
                print(f"{pokemon.name} ha aprendido {pokemon.learnset[0].name}!\n")
            else:
                print (f"{pokemon.name} ha aprendido Splash! (this is useless! (no))")
            pokemon.learnset.pop(pokemon.learnset.index(pokemon.learnset[0]))

    def battle_trainer(self, player, trainer):
        active_pokemon = player.pokemons[0]
        enemy_pokemon = trainer.pokemons[0]

        if active_pokemon.HP[0] <= 0:
            for i in player.pokemons:
                if i.HP[0] > 0:
                    active_pokemon = i
                else:
                    active_pokemon = active_pokemon
                    break
        
        while True:
            turn = random.randrange(0,2)
            
            if active_pokemon.HP[0] > 0:
                if turn == 0:
                    active_pokemon = self.players_turn(active_pokemon, enemy_pokemon, player)
                    
                    if enemy_pokemon.HP[0] <= 0:
                        if trainer.pokemons.index(enemy_pokemon)+1 in range(len(trainer.pokemons)):
                            enemy_pokemon = trainer.pokemons[trainer.pokemons.index(enemy_pokemon)+1] 
                            print (f"\nEl oponente ha cambiado de pokemon a {enemy_pokemon.name}")
                        else:  
                            break
                            
                    self.enemy_turn(active_pokemon, enemy_pokemon)
                    
                    if active_pokemon.HP[0] <= 0:
                        active_pokemon = self.change_pokemon(active_pokemon, player)
   
                else:
                    self.enemy_turn(active_pokemon, enemy_pokemon)
                    
                    if active_pokemon.HP[0] <= 0:
                        active_pokemon = self.change_pokemon(active_pokemon, player)
                        
                    active_pokemon = self.players_turn(active_pokemon, enemy_pokemon, player)
                    
                    if enemy_pokemon.HP[0] <= 0:
                        if trainer.pokemons.index(enemy_pokemon)+1 in range(len(trainer.pokemons)):
                            enemy_pokemon = trainer.pokemons[trainer.pokemons.index(enemy_pokemon)+1] 
                            print (f"El oponente ha cambiado de pokemon a {enemy_pokemon.name}")
                        else:  
                            break
            else:
                print ("Todos tus pokemon han sido debilitados!")
                break
                
        for p in trainer.pokemons:
            if p.HP[0] > 0:
                print("\nHas perdido la batalla...")
                return False

        print("\nHas ganado la batalla!")
        
        for p in player.pokemons:
            print(f"\n{p.name} ha subido de nivel!")
            self.level_up(p)

        if trainer.name != "Ash Ketchum":
            print("\nHas ganado la batalla!")
            return True
        else:
            
            print ("Has ganado el juego!")
            print ("Tu equipo ganador: ")
            for i in player.pokemons:
                print (f"👏 {i.name} 👏")
            
            sys.exit()
            

    def battle_pokemon(self, player, enemy_pokemon):
        active_pokemon = player.pokemons[0]
        
        if active_pokemon.HP[0] <= 0:
            for i in player.pokemons:
                if i.HP[0] > 0:
                    active_pokemon = i
                else:
                    active_pokemon = active_pokemon
                    break
                
        while True:
            turn = random.randrange(0,2)
            if active_pokemon.HP[0] > 0:
                if turn == 0:
                    active_pokemon = self.players_turn(active_pokemon, enemy_pokemon, player)
                    
                    if enemy_pokemon.HP[0] <= 0:
                        break           
                        
                    self.enemy_turn(active_pokemon, enemy_pokemon)
                    
                    if active_pokemon.HP[0] <= 0:
                        active_pokemon = self.change_pokemon(active_pokemon, player)
                        break           
                        
                else:
                    self.enemy_turn(active_pokemon, enemy_pokemon)
                    
                    if active_pokemon.HP[0] <= 0:
                        active_pokemon = self.change_pokemon(active_pokemon, player)
                        break 
                        
                    active_pokemon = self.players_turn(active_pokemon, enemy_pokemon, player)
                    
                    if enemy_pokemon.HP[0] <= 0:
                        break
            else:
                print ("Todos tus pokemon han sido debilitados!")
                break

        if enemy_pokemon.HP[0] > 0:
            print("\nHas perdido la batalla...")
            for p in player.pokemons:
                aux1 = p.atk[1]
                p.atk = (aux1, p.atk[1])

                aux = p.defense[1]
                p.defense = (aux, p.defense[1])
                
            return False

        print("\nHas ganado la batalla!")
        for p in player.pokemons:
            print(f"\n{p.name} ha subido de nivel!")
            self.level_up(p)
            aux1 = p.atk[1]
            p.atk = (aux1, p.atk[1])

            aux = p.defense[1]
            p.defense = (aux, p.defense[1])

        while True:
            choice = input (f"Deseas capturar al {enemy_pokemon.name} salvaje? Y/N: ")

            if choice == "Y" or choice == "y":
                player.pokemons.append(enemy_pokemon)
                print (f"\nHas capturado a {enemy_pokemon.name} salvaje!")
                break
            elif choice == "N" or choice == "n":
                print ("...Continuando aventura\n")
                break
            else:
                print ("\nOpción inválida\n")

        return True
