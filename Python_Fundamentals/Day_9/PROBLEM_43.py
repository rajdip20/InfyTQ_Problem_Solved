'''  Write a python function to check whether the given number is a perfect number or not. The
    function should returns true if the number is a perfect number, else it should returns false.
    
    Hint: Perfect number is a positive whole number that is equal to the sum of its proper divisors.
    The first perfect number is 6 as the sum of its proper positive divisors, 1,2 and 3 is 6. Other
    perfect numbers are 28, 496, 8128 ...
    
    Extend the program written for the above problem to write another function to find all perfect
    numbers in a given list of numbers. Populate the perfect numbers in a list and return the list. If
    no perfect numbers are found, return an empty list.

    Note- Reuse the code wherever possible.
'''

def get_divisors(n):
    l = []
    for i in range(1,n):
        if n % i == 0:
            l.append(i)
    return l

def is_perfect(n):
    if sum(get_divisors(n)) == n:
        return True
    else:
        return False

def check_perfect_numbers(l):
    perfect_numbers = []
    for i in l:
        if is_perfect(i):
            perfect_numbers.append(i)
    return perfect_numbers

print(check_perfect_numbers([28, 110, 200, 496, 500, 8128]))
