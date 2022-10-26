"""
My collection of fitness evaluation methods

Student number:20119632
Student name:Donghao Wang
"""

#imports
import math

def fitness(individual,Xsample,Ysample): 
    #[Destination,method,operator1,operator2]
    """Compute fitness of an invidual """    
    #sum of squared error
    fitness_1=0
    for x in range(len(Ysample)):
        r1=Xsample[x][0]
        r2=Xsample[x][1]
        r0,r3,r4=0,0,0
        for i in individual:
            if i[0]=="r0":
                r0=method(i,r0,r1,r2,r3,r4)
            elif i[0]=="r3":
                r3=method(i,r0,r1,r2,r3,r4)
            elif i[0]=="r4":
                r4=method(i,r0,r1,r2,r3,r4)
        fitness_1+=(Ysample[x]-r0)**2
    return fitness_1
def method(input,r0,r1,r2,r3,r4):
    if input[1]=="add":
        element1=element(input[2],r0,r1,r2,r3,r4)
        element2=element(input[3],r0,r1,r2,r3,r4)
        return element1+element2
    elif input[1]=="sub":
        element1=element(input[2],r0,r1,r2,r3,r4)
        element2=element(input[3],r0,r1,r2,r3,r4)
        return element1-element2
    elif input[1]=="multiply":
        element1=element(input[2],r0,r1,r2,r3,r4)
        element2=element(input[3],r0,r1,r2,r3,r4)
        return element1*element2
    elif input[1]=="residual":
        element1=element(input[2],r0,r1,r2,r3,r4)
        element2=element(input[3],r0,r1,r2,r3,r4)
        #deal with the 0 case
        return element1%element2 if element2 else element1
    return 0
def element(input,r0,r1,r2,r3,r4):
    if input=="r0":
        return r0
    elif input=="r1":
        return r1
    elif input=="r2":
        return r2
    elif input=="r3":
        return r3
    elif input=="r4":
        return r4
    else:
        return input
def mul(x,y):
    return x*y
def sub(x,y):
    return x-y
def res(x,y):
    return x%y if x%y else x
def add(x,y):
    return x+y