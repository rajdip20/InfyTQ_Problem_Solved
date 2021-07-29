''' The below function is written to check whether a given three digit number is an Armstrong
    number.

    Hint: An “Armstrong number” is an n-digit number that is equal to the sum of the nth powers of
    its individual digits.
    
    Example: 371 is an Armstrong number as 371 = 3^3 +7^3+ 1^3
'''

def is_Armstrong(n):
    temp = 0
    number = n
    while n != 0:
        x = n % 10
        n = n // 10
        temp += (x * x * x)

    if number == temp:
        print("It's an Armstrong number.")
    else:
        print("It's Not an Armstrong number.")

is_Armstrong(371)
