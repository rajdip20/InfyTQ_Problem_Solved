# Write a code to check whether a given number is a palindrome.

n = int(input("Enter the number: "))
n_str = str(n)
flag = 0

for i in range(len(n_str)//2):
    if n_str[i] != n_str[len(n_str) - i - 1]:
        flag = 1
        break

if flag == 1:
    print("The given number is not a Palindrome number.")
else:
    print("The given number is a Palindrome number.")
