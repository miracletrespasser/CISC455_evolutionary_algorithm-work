"""
My collection of parent selection methods

Student number: 20119632
Student name: Donghao Wang
"""

# imports
import random
import evaluation
def tournament(tournament_size,population,X,Y):
    """Tournament selection without replacement"""
    # student code starts
    #two rounds
    length=len(population)
    bestnumber=[]
    worstnumber=[]
    #make sure the 2 parent and 2 worst produced is not the same
    while len(bestnumber)<2 or len(worstnumber)<2:
        #list of index number in population
        list=random.sample(range(0,length),tournament_size)
        #best selection at the top
        best_selection=list[0]
        worst_selection=list[0]
        for i in range(1,tournament_size):
            if evaluation.fitness(population[i],X,Y)<evaluation.fitness(population[best_selection],X,Y):
                best_selection=list[i]
            elif evaluation.fitness(population[i],X,Y)>evaluation.fitness(population[worst_selection],X,Y):
                worst_selection=list[i]
        if (not best_selection in bestnumber) and (not worst_selection in worstnumber):
            bestnumber.append(best_selection)
            worstnumber.append(worst_selection)
        # student code ends
    
    return bestnumber,worstnumber