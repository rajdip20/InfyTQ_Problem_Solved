''' The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and
    719, are themselves prime.
    
    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
    
    Write a python program to find and display the number of circular primes less than the given
    limit.
'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True

def is_circuler_prime(n):
    for i in range(len(str(n))):
        l = [d for d in str(n)]
        l = l[i:len(str(n))] + l[:i]
        if not is_prime(int("".join(l))):
            return False
    return True

def find_circular_primes(limit):
    l = []
    for i in range(limit):
        if is_circuler_prime(i):
            l.append(i)
    return l

print(find_circular_primes(100))
