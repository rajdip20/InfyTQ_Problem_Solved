''' Write a python function, check_double(number) which accepts a whole number and returns
    True if it satisfies the given conditions.
        1. The number and its double should have exactly the same number of digits.
        2. Both the numbers should have the same digits ,but in different order.
    
    Otherwise it should return False.

    Example: If the number is 125874 and its double, 251748, contain exactly the same digits, but
    in a different order.
'''

def find_length(number):
    return len(str(number))

def is_anagram(num1, num2):
    str1 = str(num1)
    str2 = str(num2)
    digits_count = {}
    for digit in str1:
        if digit in digits_count:
            digits_count[digit] = digits_count[digit] + 1
        else:
            digits_count[digit] = 1
    for digit in str2:
        if digit in digits_count:
            digits_count[digit] = digits_count[digit] - 1
            if digits_count[digit] == 0:
                digits_count.pop(digit)
        else:
            return False
    if len(digits_count) == 0:
        return True
    else:
        return False

def check_double(number):
    double = 2 * number
    if find_length(number) == find_length(double):
        if is_anagram(number, double):
            return True
        else:
            return False
    else:
        return False

print(check_double(125874))
