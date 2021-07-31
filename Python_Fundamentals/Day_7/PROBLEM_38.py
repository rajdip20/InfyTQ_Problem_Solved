''' Consider sample data as follows: sample_data=range(1,11)
    
    Create two functions: odd() and even()
    The function even() returns a list of all the even numbers from sample_data
    The function odd() returns a list of all the odd numbers from sample_data
    
    Create a function sum_of_numbers() which will accept the sample data and/or a function.
    If a function is not passed, the sum_of_numbers() should return the sum of all the numbers
    from sample_data
    If a function is passed, the sum_of_numbers() should return the sum of numbers returned from
    the function passed.
'''

def even(l):
    even = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
    return even

def odd(l):
    odd = []
    for i in l:
        if i % 2 != 0:
            odd.append(i)
    return odd

def sum_of_numbers(l, func=None):
    if func is None:
        return sum(l)
    else:
        return sum(func(l))

print(sum_of_numbers(range(1, 11), even))
