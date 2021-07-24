# Write a code to find the minimum among three given numbers.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if (a < b):
    if (a < c):
        print(a)
    else:
        print(c)
elif (b < c):
    print(b)
else:
    print(c)
