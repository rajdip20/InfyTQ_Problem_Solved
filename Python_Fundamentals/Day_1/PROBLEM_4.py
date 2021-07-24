''' A three digit number is said to be an “Armstrong number” if the sum of the third power of its individual digits is equal to the number itself.
    Write a program to check whether a number is armstrong or not. '''

n = int(input("Enter your number: "))
temp = n
count = 0

while temp != 0:
    temp = temp // 10
    count += 1

temp = n
sum = 0

while temp != 0:
    digit = temp % 10
    temp = temp // 10
    sum = sum + digit ** count

if sum == n:
    print("It's an Armstrong number.")
else:
    print("It's Not an Armstrong number.")
