# -*- coding: utf-8 -*-

from pylab import *
from power_group import power_group
import directions
import random

class board:
    def __init__(self, size):
        self.size = size
        self.board = [-1 for x in xrange(size*size)]
        self.board_value = [[0 for x in xrange(size)] for y in xrange(size)]        
        
        self.white_caps = 0
        self.black_caps = 0
        self.ko_piece = set([])
        self.board_groups = [-1 for x in xrange(size*size)]
        
        self.master_set = set([])

 
                
    def move(self, turn, moves, ai = True, plots = False, plot_every = True):

        if not ai:
            x = int(raw_input("row:"))
            y = int(raw_input("col:"))
        else:
            x = random.randint(0,18)
            y = random.randint(0,18)
            print "turn # = " + str(turn)
            
        id = 19 * x + y
        while self.board[id] != -1: # while not placing on empty
            if not ai:
                x = int(raw_input("row:"))
                y = int(raw_input("col:"))
            else:
                x = random.randint(0,18)
                y = random.randint(0,18)

            id = 19 * x + y
            
      
        #ko, 1 member set
        for piece in self.ko_piece:
            self.board[piece] = -1
        self.ko_piece.clear()
        

        #creates a new group for each new move
        self.board_groups[id] = power_group(id, turn, self.board, self.board_groups, \
            self.master_set, self.ko_piece, self.black_caps, self.white_caps)
        
        self.board[id] = turn
        self.master_set.add(self.board_groups[id])
        directions.directions(id, self.board_groups[id].verify_enemy_dead)
        
   
        self.value_update(x,y,turn, moves, plot_every)

        if plot_every or turn == moves:
            #prints board    
            for j in xrange(self.size):
                for i in xrange(self.size):
                    print str(self.board[j * 19 + i]),
                print " "
            print " "
    
            for j in xrange(self.size):
                for i in xrange(self.size):
                    print str(self.board_groups[j * 19 + i]),
                print " "
            print " "
 
#prints liberties using heat graph

        colors = [0 for x in xrange(self.size*self.size)]

        for member in self.board_groups:
            if isinstance(member, power_group):
                for liberty in member.liberties:
                    if member.turn % 2 ==0:
                        colors[liberty] = -2
                    else:
                        colors[liberty] = -1
                        
        self.heat_graph(colors, 'alexnoob2.png', 1, 's', 300)         
        
        
    #adjust ai moves                  
    def play(self, moves = 100):
        turn = 1 #black starts first
        while turn <= moves:
            self.move(turn, moves)
            turn += 1
        self.calculate_winner()
        
    def heat_graph(self, c, name, v, symbol, s):
        clf()
        x = [i % 19 for i in xrange(self.size * self.size)]

        y = []
        for i in xrange(self.size -1 , -1 , -1):
            for j in xrange(self.size):
                y.append(i)

        scatter(x,y,s=s,c = c, vmin=-1 * v , vmax= v  , marker = symbol)
        savefig(name)
        
    def value_update(self, x, y, turn, moves, plot_every):
        if turn %2 == 1:
            sign = 1
        else:
            sign = -1

            #uses inverse square law centered on x and y
        local_value = [[round( sign/(((x - i) ** 2 + (y - j) ** 2)**.5), 1) \
                        if x !=i or y !=j else sign for i in xrange(self.size)] for j in xrange(self.size)]


        for i in xrange(self.size):
            for j in xrange(self.size):
                self.board_value[i][j] += local_value[i][j]
        
        if plot_every or turn == moves:
            #plotting
            self.heat_graph([[self.board_value[x][y] for x in xrange(self.size)] for y in xrange(self.size)], 'alexnoob1.png', .75, 's', 300)
                            
    #used to estimate influence or  calculate endgame score    
    def calculate_winner(self):
        #komi
        net_score = 6.5
        for i in xrange(self.size ** 2):
            net_score += self.board[i]
            
        if net_score > 0:
            print "black leads"
        else:
            print "white leads"