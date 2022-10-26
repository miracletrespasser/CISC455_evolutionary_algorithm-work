"""
My collection of initialization methods for different representations

Student number: 20119632
Student name: Donghao Wang
"""

#imports
import random
import itertools

def initialization_permutation (lowerbound,upperbound,length):
    """initialize a population of permutation"""

    Constants=[1,2,3,4,5]
    method=["add","sub","multiply","residual"]
    # Random generation
    #output:r0
    #input: r1,r2
    #calculation:r3,r4
    #iteration in loop_size
    #train each element in sample
    list_of_instructions=[]
    for j in range(length):
        #initialize regitsters for a not possible number
        Registers=["r0","r1","r2","r3","r4"]
        Modifiable_registers=["r0","r3","r4"]
        this_program_length=random.randint(lowerbound,upperbound+1)
        #generate a set of instructions
        temp_list=[]
        #[destination,method,register1,register2/constant]
        for k in range(this_program_length):
            CorR=random.randint(0,1)
            if CorR:
                temp_list.append([Modifiable_registers[random.randint(0,2)],method[random.randint(0,3)],Constants[random.randint(0,4)],Registers[random.randint(0,4)]])
            else:
                CorR_2=random.randint(0,1)
                if CorR_2:
                    temp_list.append([Modifiable_registers[random.randint(0,2)],method[random.randint(0,3)],Registers[random.randint(0,4)],Constants[random.randint(0,4)]])
                else:
                    temp_list.append([Modifiable_registers[random.randint(0,2)],method[random.randint(0,3)],Registers[random.randint(0,4)],Registers[random.randint(0,4)]])
        list_of_instructions.append(temp_list)
    #student code end
    
    return list_of_instructions