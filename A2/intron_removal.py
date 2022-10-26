def remove(program):
    Registers=["r0","r1","r2","r3","r4"]
    Modifiable_registers=["r0","r3","r4"]
    Constants=[1,2,3,4,5]
    method=["add","sub","multiply","residual"]
    list_length=len(program)
    startup_register=["r0"]
    temp_list=[]
    #go backwards
    for i in range(list_length-1,-1,-1):
        if program[i][0] in startup_register:
            #add effective program in 
            temp_list.append(program[i])
            #add effective register in)
            startup_register.remove(program[i][0])
            if not type(program[i][2]) == int:
                startup_register.append(program[i][2])
            if not type(program[i][3]) == int:
                startup_register.append(program[i][3])
            startup_register=list(dict.fromkeys(startup_register))
            if "r1" in startup_register:
                startup_register.remove("r1")
            if "r2" in startup_register:
                startup_register.remove("r2")
            if not startup_register:
                break
    #remove the read only registers
    temp_list.reverse()
    if startup_register:
        return []
    else:
        return temp_list