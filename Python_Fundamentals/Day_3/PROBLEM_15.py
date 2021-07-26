''' Write a python program which finds the maximum number from num1 to num2 
    (num2 inclusive) based on the following rules.

    1. Always num1 should be less than num2

    2. Consider each number from num1 to num2 (num2 inclusive). Populate the number into a
    list, if the below conditions are satisfied
        1. Sum of the digits of the number is a multiple of 3
        2. Number has only two digits
        3. Number is a multiple of 5

    3. Display the maximum element from the list

    In case of any invalid data or if the list is empty, display -1.
'''

def get_max(n1, n2):
    if n1 < n2:
        l = []
        for i in range(n1, n2 + 1):
            n = [int(d) for d in str(i)]
            if sum(n) % 3 == 0 and len(n) == 2 and i % 5 == 0:
                l.append(i)
        if len(l) > 0:
            return max(l)
        else:
            return -1
    else:
        return -1

num1 = int(input("Enter the minimum number: "))
num2 = int(input("Enter the maximum number: "))
print(get_max(num1, num2))
