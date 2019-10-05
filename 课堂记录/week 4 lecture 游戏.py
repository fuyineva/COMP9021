from random import random

grid = [[0] * 12 for _ in range(12)] 
density = 0.4
for i in range(1,11):
    for j in range(1,11):
        if random() < density:
            grid[i][j] = 1
        
new_grid = [[None] * 12 for _ in range(12)]

def next_generation():
    global grid
    for i in range(1,11):
        for j in range(1,11):
            #
            nb_of_nerighbours = sum((grid[i - 1][j - 1],
                                    grid[i - 1][j],
                                    grid[i - 1][j + 1],
                                    grid[i][j - 1],
                                    grid[i][j + 1],
                                    grid[i + 1][j - 1],
                                    grid[i + 1][j],
                                    grid[i + 1][j + 1]))
            new_grid[i][j] = 1 if nb_of_nerighbours == 3 or\
            nb_of_nerighbours == 2 and grid[i][j]\
            else 0
    grid = new_grid
                                    


def print_grid():
    for i in range(1,11):
        print (' '.join(str(e) for e in grid[i][1:11]))
print_grid()
print()
next_generation()
print_grid()
print()
