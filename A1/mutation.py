"""
My colleciton of mutation methods

Student number:20119632
Student name:Donghao Wang
"""

# imports
import random

def permutation_swap (individual):
    """Mutate a permutation"""

    mutant = individual.copy()
    
    # student code starts
    #choose two position from the mutant
    length = len(individual)
    Mutation_positions = random.sample(range(0,length),2)
    #swap the position
    mutant[Mutation_positions[0]],mutant[Mutation_positions[1]]= mutant[Mutation_positions[1]],mutant[Mutation_positions[0]]
    # student code ends
    
    return mutant
