main.py: the main program execution, prints the best program and the fitness every 100 iteration.
initialization: initializes the setting 
evaluation.py: calculate fitness, less the value more fitter
parent selection: do two rounds of tournament selection, get the index of the best and worst parents
recombination: one-point crossover, 0.8 rate
mutation:0.25 micromutation that only changes the program internally like changing the register or method
         0.75 macromutation that could add or delete a instruction in program
survival selection: the offspring replaced the best and worst parent in population
