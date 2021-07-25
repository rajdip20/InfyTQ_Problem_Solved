''' 
Write a python program to find and display the product of three positive integer values
based on the rule mentioned below:

    It should display the product of the three values except when one of the integer value is 7. In
        that case, 7 should not be included in the product and the values to its left also should not be
        included.
    If there is only one value to be considered, display that value itself. If no values can be included
        in the product, display - 1.

Note: Assume that if 7 is one of the positive integer values, then it will occur only once. Refer
    the sample I/O given below.

     Sample          Expected
     Input           Output

    1, 5, 3             15
    3, 7, 8             8
    7, 4, 3             12
    1, 5, 7             -1 
'''

numbers = []
for i in range(3):
    numbers.append(int(input("Enter the number: ")))

prod = 1
if 7 in numbers:
    index = numbers.index(7)
    temp = numbers[index + 1:]
    if len(temp) == 0:
        prod = -1
    else:
        for i in temp:
            prod = prod * i
else:
    for i in numbers:
        prod = prod * i

print(prod)
