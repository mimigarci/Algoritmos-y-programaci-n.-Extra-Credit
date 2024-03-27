class Location:
    
    def __init__(self):
        self.battle_cleared = False


    def foward (self, player_location, locations_list):
        
        location = locations_list.index(player_location)
        foward = location +1
        try:
            new_location = locations_list[foward]
        except IndexError:
            print ("No puedes avanzar más.")

        return new_location

    
    def backwards (self, player_location, locations_list):
        
        location = locations_list.index(player_location)
        backwards = location -1

        try:
            new_location = locations_list[backwards]
        except IndexError:

