"""
My colleciton of mutation methods

Student number:20119632
Student name:Donghao Wang
"""

# imports
import random

def mutation (individual):
    """Mutate a permutation"""
    # student code 
    Constants=[1,2,3,4,5]
    method=["add","sub","multiply","residual"]
    Registers=["r0","r1","r2","r3","r4"]
    Modifiable_registers=["r0","r3","r4"]
    combine=Constants+Registers
    i=individual.copy()
    p=random.randint(1,4)
    if p==1:
        #micromutation
        #choose one of the lines to modify
        r=random.randint(0,len(i)-1)
        selection=random.randint(0,3)
        if selection == 0:
            i[r][selection]=Modifiable_registers[random.randint(0,2)]
        elif selection == 1:
            i[r][selection] =method[random.randint(0,3)]
        else:
            if type(i[r][selection]) == int:
                i[r][selection] = Constants[random.randint(0,4)]
            else:
                if selection==2:
                    if type(i[r][3])==int:
                        i[r][selection] = Registers[random.randint(0,4)]
                    else:
                        i[r][selection] = combine[random.randint(0,8)]
                else:
                    if type(i[r][2])==int:
                        i[r][selection] = Registers[random.randint(0,4)]
                    else:
                        i[r][selection] = combine[random.randint(0,8)]
    else:
        #macro mutation
        if len(i)>5:
            p=random.randint(0,1)
            r=random.randint(0,len(i)-1)
            if p==0:
                #delete
                i.pop(r)
            else:
                #add
                i.insert(r,[Modifiable_registers[random.randint(0,2)],method[random.randint(0,3)],Constants[random.randint(0,4)],Registers[random.randint(0,4)]])
        elif len(i)>49:
            r=random.randint(0,len(i)-1)
            i.pop(r)
        else:
            #add 
            r=random.randint(0,len(i)-1)
            i.insert(r,[Modifiable_registers[random.randint(0,2)],method[random.randint(0,3)],Constants[random.randint(0,4)],Registers[random.randint(0,4)]])
            
    # student code ends
    return i
