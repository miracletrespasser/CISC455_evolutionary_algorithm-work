"""
My collection of survivor selection methods

Student number:20119632
Student name: Donghao Wang
"""

#imports

import random

def mu_plus_lambda(current_pop, current_fitness, offspring, offspring_fitness):
    """mu+lambda selection"""
    population = []
    fitness = []

    # student code starts
    combined_population = current_pop+offspring
    combined_fitness=current_fitness+offspring_fitness
    ranked_fitness=[]
    #get the ranked fitness
    for x in range(len(combined_fitness)):
        ranked_fitness.append([combined_fitness[x],x])
    ranked_fitness.sort(reverse=True)
    #find the top (population size) number of index surviors 
    for y in range(len(current_pop)):
        population.append(combined_population[ranked_fitness[y][1]])
        fitness.append(ranked_fitness[y][0])
    # student code ends
    
    return population, fitness


def replacement(current_pop, current_fitness, offspring, offspring_fitness):
    """replacement selection"""

    population = []
    fitness = []

    # student code starts
    ranked_fitness=[]
    # if mu<=lambda
    if len(current_pop)<=len(offspring):
        print('Population size smaller than offspring size')
        population=offspring(slice(len(current_pop)))
        fitness=offspring_fitness(slice(len(current_fitness)))
    #normal case mu>lambda
    else:
        #rank the population
        for x in range(len(current_pop)):
            ranked_fitness.append([current_fitness[x],x])
        ranked_fitness.sort(reverse=True)
        remained_population_length=len(current_pop)-len(offspring)
        sliced_ranked_fitness=ranked_fitness[slice(remained_population_length)]
        #generate the part kept in population
        for y in sliced_ranked_fitness:
            population.append(current_pop[y[1]])
            fitness.append(y[0])
        #replace the latter lambda items
        population+=offspring
        fitness+=offspring_fitness
    
    # student code ends
    
    return population, fitness


def random_uniform(current_pop, current_fitness, offspring, offspring_fitness):
    """random uniform selection"""
    population = []
    fitness = []

    # student code starts
    combined_population = current_pop+offspring
    combined_fitness=current_fitness+offspring_fitness
    sample_fitness=[]
    selected_fitness=[]
    #choose (population size) of inividuals randomly from the pool
    for x in range(len(combined_fitness)):
        sample_fitness.append([combined_fitness[x],x])
    selected_fitness=random.sample(sample_fitness,len(current_pop))
    for e in selected_fitness:
        fitness.append(e[0])
        population.append(combined_population[e[1]])
    # student code ends
    
    return population, fitness


