''' Given a number n, write a program to find the sum of the largest prime factors of each of
    nine consecutive numbers starting from n.
    
    g(n) = f(n) + f(n+1) + f(n+2) + f(n+3) + f(n+4) + f(n+5) + f(n+6) + f(n+7) + f(n+8)
    where, g(n) is the sum and f(n) is the largest prime factor of n
    
    For example,
    g(10)=f(10)+f(11)+f(12)+f(13)+f(14)+f(15)+f(16)+f(17)+f(18)
         =5 + 11 + 3 + 13 + 7 + 5 + 2 + 17 + 3
         =66
'''

def f(n):
    largest_prime = 2
    while n != 1:
        if n % largest_prime == 0:
            n = n / largest_prime
            continue
        largest_prime += 1
    return largest_prime

def g(n):
    s = 0
    for i in range(9):
        s = s + f(n + i)
    return s

print(g(10))
