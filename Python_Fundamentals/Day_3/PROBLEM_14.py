''' Write a python program to solve a classic ancient Chinese puzzle.
    We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
    
    How many rabbits and how many chickens do we have?

    Sample Input                Expected Output

    heads-150 legs-400              100 50
    heads-3 legs-11                 No solution
    heads-3 legs-12                 0 3
    heads-5 legs-10                 5 0 
'''

import math

heads = int(input("Enter the number of heads: "))
legs = int(input("Enter the number of legs: "))

r = 0.5 * legs - heads
if math.ceil(r) == math.floor(r):
    r = int(r)
    c = heads - r
    print("Chickens: ", c, "Rabbits: ", r)
else:
    print("No Solution.")
