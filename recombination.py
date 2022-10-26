"""
My collection of recombination methods

Student number:20119632
Student name:Donghao Wang
"""

#imports
import random

def permutation_cut_and_crossfill (parent1, parent2):
    """cut-and-crossfill crossover for permutation representations"""

    offspring1 = []
    offspring2 = []
    
    # student code begin
    length=len(parent1)
    #choose a random crossover point
    cross_over_point=random.randint(1,length-1)
    #slice the parents
    slice_firsthalf=slice(cross_over_point)
    slice_secondhalf=slice(cross_over_point,length)
    new_parent2_first_half=parent1[slice_firsthalf]
    new_parent1_first_half=parent2[slice_firsthalf]
    new_parent2_second_half=parent2[slice_secondhalf]
    new_parent1_second_half=parent1[slice_secondhalf]
    #generate offsprings
    offspring1=new_parent1_first_half+new_parent1_second_half
    offspring2=new_parent2_first_half+new_parent2_second_half
    # student code end
    
    return offspring1, offspring2
