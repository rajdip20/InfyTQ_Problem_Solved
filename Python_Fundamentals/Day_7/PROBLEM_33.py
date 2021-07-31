''' Write a python function, nearest_palindrome() which accepts a number and returns the
    nearest palindrome greater than the given number.
    
    Sample Input                        Expected Output
        12300                               12321
        12331                               12421
'''

def nearest_palindrome(n):
    while True:
        if str(n) == str(n)[::-1]:
            return n
        n += 1


print(nearest_palindrome(12331))
