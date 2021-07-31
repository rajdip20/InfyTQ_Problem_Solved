''' In a fair coin we have an equal chance (50%) of either getting a ‘head’ or ‘tail’. That is if
    we toss the coin a large number of times we would observe head approximately 50% of the
    time. Write a program to implement a biased coin toss where the chance of getting a head is
    70% (and tail 30%). That is if we invoke the program 1000 times we should see the head
    randomly approximately 700 times.
'''

import random

def biased_toss(prob):
    if random.randint(1, 100) < prob:
        return "H"
    else:
        return "T"

def count(flips, prob):
    heads = 0
    tails = 0
    for i in range(flips):
        if biased_toss(prob) == "H":
            heads += 1
        else:
            tails += 1
    return heads, tails

print(count(1000, 70))
