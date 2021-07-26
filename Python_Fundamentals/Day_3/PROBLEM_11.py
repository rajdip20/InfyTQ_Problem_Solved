''' Write a Python program to generate the next 15 leap years starting from a given year.
    Populate the leap years into a list and display the list. '''

def is_leap_year(year):
    if year % 4 == 0 and year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False

y = int(input("Enter your year: "))
count = 0
leap_year_list = []

while count < 15:
    if is_leap_year(y):
        leap_year_list.append(y)
        count += 1
    y += 1
print(leap_year_list)
