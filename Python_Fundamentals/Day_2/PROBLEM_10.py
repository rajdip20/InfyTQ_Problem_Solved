'''
You have x no. of 5 rupee coins and y no. of 1 rupee coins. You want to purchase an item
for amount z. The shopkeeper wants you to provide exact change. You want to pay using
minimum number of coins. How many 5 rupee coins and 1 rupee coins will you use? If exact
change is not possible then display -1.

                 Sample Input                           |            Expected Output
________________________________________________________|___________________________________|
Available Rs. 1 |   Available Rs. 5   | Amount to be    |   Rs. 1 coins   |     Rs. 5 notes |
coins           |   notes             | made            |   needed        |     needed      |
________________|_____________________|_________________|_________________|_________________|
2               |     4               |     21          |       1         |         4       |
________________|_____________________|_________________|_________________|_________________|
11              |     2               |     11          |       1         |         2       |
________________|_____________________|_________________|_________________|_________________|
3               |     3               |     19          |       -1        |                 |
________________|_____________________|_________________|_________________|_________________|

'''

denominations = [1, 5]
denominations = sorted(denominations, reverse = True)
denomination_count = {}
used = {}

for denomination in denominations:
    used[denomination] = 0
    denomination_count[denomination] = int(input("Enter the number of " + str(denomination) + " coins: "))
amount = int(input("Enter the amount: "))

while amount > 0 and len(denomination_count) > 0:
    amount = amount - denominations[0]
    used[denominations[0]] = used[denominations[0]] + 1
    denomination_count[denominations[0]] = denomination_count[denominations[0]] - 1
    if (amount - denominations[0]) < 0 or denomination_count[denominations[0]] == 0:
        denomination_count.pop(denominations[0])
        denominations.remove(denominations[0])

if amount == 0:
    print("Success")
    print(used)
else:
    print(-1)
