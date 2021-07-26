''' Write a python function to check whether three given numbers can form the sides of a
triangle.
Hint: 
    Three numbers can be the sides of a triangle if none of the numbers are greater than or equal
    to the sum of the other two numbers. 
'''

def is_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return "Can't form a triangle"
    else:
        return "Can form a triangle"

a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

print(is_triangle(a, b, c))
