''' Write a python function find_smallest_number() which accepts a number n and returns the
    smallest number having n divisors.

    Sample Input                Expected Output
        16                          120
'''

def find_smallest_number(n):
    num = 1
    while True:
        if len([i for i in range(1, num + 1) if num % i == 0]) == n:
            return num
        num += 1

print(find_smallest_number(16))
