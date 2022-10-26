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
    len_1=len(parent1)
    len_2=len(parent2)
    if len_1 == 1 and len_2== 1:
        return parent2,parent1
    if len_1<len_2:
        length=len_1
    else:
        length=len_2
    #choose a random crossover point
    if length>1:
        cross_over_point=random.randint(1,length-1)
        #slice the parents
        slice_firsthalf=slice(cross_over_point)
        slice_secondhalf=slice(cross_over_point,length)
        #cross_and_fill
        new_parent2_first_half=parent1[slice_firsthalf]
        new_parent1_first_half=parent2[slice_firsthalf]
        new_parent2_second_half=parent2[slice_secondhalf]
        new_parent1_second_half=parent1[slice_secondhalf]
        #generate offsprings
        offspring1=new_parent1_first_half+new_parent1_second_half
        offspring2=new_parent2_first_half+new_parent2_second_half
    else:
        temp_list=parent1[-1]
        p1=parent1.copy()
        p2=parent2.copy()
        p1[-1]=p2[-1]
        p2[-1]=temp_list
        offspring1,offspring2=p1,p2
    # student code begin
    
    # student code end
    
    return offspring1, offspring2
