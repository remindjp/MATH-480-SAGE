#Power group
import directions 

class power_group:
                
    def __init__(self, id, turn, board, board_groups, master_set, ko_piece, black_caps, white_caps):
        
        self.id = id
        self.turn = turn
        self.board = board
        self.size = 19
        self.board_groups = board_groups
        self.master_set = master_set
        self.ko_piece = ko_piece
        
        self.members = set([id])
        
        self.liberties = set([])
            
        self.immediate_enemies = set([])
        self.black_caps = black_caps
        self.white_caps = white_caps
        
        #Initialize up down left right and liberties, members, enemies update   
        directions.directions(self.id, self.check_direction)
        
        #handles suicide as a pass
        if self.liberties == 0:
            self.self_capture()

                    
    #on initialzation    
    def check_direction(self, direction):
                
        direction_group = self.locate(direction)
        if self.board[direction] == -1: #empty
            self.liberties.add(direction)
        #same color, power group must be associated with it    
        elif self.board[direction] % 2 == self.turn % 2:
            self.union(direction_group)   
        else: #different color, add to enemies group, remove liberties
            self.immediate_enemies.add(direction)  
            other = self.locate(direction)
            other.immediate_enemies.add(self.id)
            other.liberties.remove(self.id)

        
    def __repr__(self):
       return str(self.members) + "lib:" + str(self.liberties) + "direm" + str(self.immediate_enemies)   
 
    #combines other group with this group           
    def union(self, other):
        self.members.update(other.members)
        self.liberties.update(other.liberties)
        self.liberties.difference_update(self.members)
        self.immediate_enemies.update(other.immediate_enemies)
        
        self.board_groups[other.id] = other.id   
        #delete other group
        self.master_set.remove(other)
        del other 
           
    
    #locates the main group, only one per group of id's 
    def locate(self, id):
        #will make faster, check for local group
        
        for member in self.master_set:
            for element in member.members:
                if id == element:
                    return member
    
    #returns liberties
    def liberty_return(self, direction):
        for enemy in self.immediate_enemies:
            other = self.locate(enemy)
            if isinstance(other, power_group):
                other.liberties.add(self.id)

                                                                                          
    #Considers this piece captured   
    def self_capture(self):
        #returns liberties
        directions.directions(self.id, self.liberty_return)
              
            
        #removes members and reassigns
        killed = 0
        for member in self.members:
            self.board[member] = -1
            self.board_groups[member] = -1    
            self.master_set.discard(self.locate(member))
            killed += 1
        
        if self.turn % 2  == 1:
            self.white_caps += 1
        else:
            self.black_caps += 1


            
                        
    def help_ved(self, place):
        self.board[place] = -2
        self.ko_piece.add(place)
                                                      
    #capture check     
    def verify_enemy_dead(self, place):
        
        if self.board_groups[place] != -1:
            place_group = self.locate(place)
            if len(place_group.liberties) == 0:
                
                                                                                                   
                    place_group.self_capture() 
                    
                    #ko
                    if len(place_group.members) == 1:
                        up = self.id - 19
                        down = self.id + 19  
                        left = self.id - 1 
                        right = self.id + 1            
                        adjacents = 0
                        
                        if up >= 0 and self.board[up] > 0 and self.turn % 2 != self.board[up]:
                            adjacents +=1
                        if down <= 19 * 19 - 19 and self.board[down] > 0 and self.turn % 2 != self.board[down]:
                            adjacents +=1
                        if left >= 0 and left % 19 != 18 and self.board[left] > 0 and self.turn % 2 != self.board[left]:
                            adjacents +=1
                        if right < 19 * 19 and right % 19 != 0 and self.board[right] > 0 and self.turn % 2 != self.board[right]:
                            adjacents +=1            
    
                        #corner edge and other ko conditions    
                        if self.id == 0 or self.id == 18 or self.id == 342 or self.id == 360:
                            if adjacents == 1: 
                                self.help_ved(place)
                        elif self.id % 19 > 342 or self.id <19 or self.id % 19 == 18 or self.id % 19 == 0:   
                            if adjacents == 2:
                                self.help_ved(place)
                        elif adjacents ==3:                  
                                self.help_ved(place)                     