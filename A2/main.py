import initialization
import evaluation
import intron_removal
import evaluation
import parent_selection
import recombination
import mutation
import random
def main(size):
    f=open("trainingSamples.txt","r")
    # read in works well
    X_sample=[]
    Y_sample=[]
    count=0
    for x in f:
        temp=x.split()
        if count>0:
            X_sample.append([float(temp[0]),float(temp[1])])
            Y_sample.append(float(temp[2]))
        count+=1
    population=initialization.initialization_permutation (5,10,size)
    #structural intron removal algorithm
    pop_size=len(population)
    for i in range(pop_size):
        new_list=intron_removal.remove(population[i])
        population[i]=new_list
    new_population=[x for x in population if x != []]
    #most remaining program this time is below 5 instructions
    for i in range(1,10001):
        #parent selection
        nts=3
        best_parent=[]
        worst_parent=[]
        best_parent,worst_parent=parent_selection.tournament(nts,new_population,X_sample,Y_sample)
        #recombination
        parent1=new_population[best_parent[0]]
        parent2=new_population[best_parent[1]]
        offspring1=[]
        offspring2=[]
        #0.8 rate to mutate 
        p=random.randint(1,5)
        if p==1:
            offspring1,offspring2=parent1,parent2
        else:
            offspring1,offspring2=recombination.permutation_cut_and_crossfill(parent1,parent2)
        #mutation
        for k in range(10):
            offspring1 = mutation.mutation(offspring1)
            offspring2 = mutation.mutation(offspring2)
        offspring1 = intron_removal.remove(offspring1)
        offspring2 = intron_removal.remove(offspring2)
        #survival selection
        if offspring1:
            new_population[worst_parent[0]]=offspring1
        if offspring2:
            new_population[worst_parent[1]]=offspring2
        #evaluate the fittest program very 100 instructions
        if not i%100:
            bestfitness=evaluation.fitness(new_population[0],X_sample,Y_sample)
            best=0
            for i in range(1,len(new_population)):
                currentfitness=evaluation.fitness(new_population[i],X_sample,Y_sample)
                if currentfitness<bestfitness:
                    bestfitness=currentfitness
                    best=i
            print("Bestprogram:")
            print(new_population[best])
            print("Fitenss:")
            print(bestfitness)
            print()
main(100)