"""
My collection of fitness evaluation methods

Student number:20119632
Student name:Donghao Wang
"""

#imports
import math

def fitness_8queen (individual): 
    """Compute fitness of an invidual for the 8-queen puzzle (maximization)"""    
    fitness = 0
    # student code begin
    length=len(individual)
    #Iterate through each row, to update the fitness
    for piece_row in range(length):
        piece_col=individual[piece_row]
        #check conflicts
        for other_piece_row in range(length):
            #check not to be same row
            if other_piece_row == piece_row:
                pass
            #check not to be same co
            elif individual[other_piece_row] == piece_col:
                pass
            #check not on the upper diagonal
            elif other_piece_row + individual[other_piece_row]==piece_row+piece_col:
                pass
            #check not on the down diagonal
            elif other_piece_row - individual[other_piece_row]==piece_row-piece_col:
                pass
            #update fitness as the pieces are not conflicting
            else:
                fitness+=1
    #remove the duplicate calculation
    fitness/=2
    # student code end
    
    return fitness


