"""
My collection of parent selection methods

Student number: 20119632
Student name: Donghao Wang
"""

# imports
import random



def MPS(fitness, mating_pool_size):
    """Multi-pointer selection (MPS)"""

    selected_to_mate = []
    # student code starts
    #gengerate cumulative probability
    fitness_sum=sum(fitness)
    length=len(fitness)
    Cumulative=0
    Cumulative_probability_distribution=[]
    for i in range(0,length):
         Cumulative+=fitness[i]
         Cumulative_probability_distribution.append(float(Cumulative/fitness_sum))
    #generate multi-pionter selection
    current_number=0
    i=0
    r= random.uniform(0,float(1/mating_pool_size))
    while(current_number<mating_pool_size):
        while(r<=Cumulative_probability_distribution[i]):
            selected_to_mate.append(i)
            r+=float(1/mating_pool_size)
            current_number+=1
        i+=1
    # student code ends
    
    return selected_to_mate


def tournament(fitness, mating_pool_size, tournament_size):
    """Tournament selection without replacement"""

    selected_to_mate = []
    
    # student code starts
    length=len(fitness)
    for current_nubmer in range(0,mating_pool_size):
        list=random.sample(range(0,length),tournament_size)
        best_selection=list[0]
        for i in range(1,tournament_size):
            if fitness[list[i]]>best_selection:
                best_selection=list[i]
        selected_to_mate.append(best_selection)
    # student code ends
    
    return selected_to_mate


def random_uniform (population_size, mating_pool_size):
    """Random uniform selection"""

    selected_to_mate = []

    # student code starts
    selected_to_mate=random.sample(range(0,population_size),mating_pool_size)

    # student code ends
    
    return selected_to_mate

