''' Write a code to find the sum of numbers divisible by 4.The code must allow the user to accept a number and add it to the sum if it is 
    divisible by 4. It should continue accepting numbers as long as the user wants to provide an input and should display the final sum. '''

sum = 0
while True:
    n = int(input("Enter your number: "))
    if n % 4 == 0:
        sum += n
    ch = input("Enter your choice [y/n]: ")
    if ch.upper() == 'N':
        break

print("Sum of numbers divisible by 4 is: ", sum)
