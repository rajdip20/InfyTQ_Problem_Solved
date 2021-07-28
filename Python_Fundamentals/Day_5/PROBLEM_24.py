''' Write a python function, create_largest_number(), which accepts a list of numbers and
    returns the largest number possible by concatenating the list of numbers.

    Note: Assume that all the numbers are two digit numbers.

    Sample Input                    Expected Output

      23,34,55                          553423

'''


def create_largest_number(numbers):
    numbers.sort(reverse = True)
    largest = ''
    for num in numbers:
        largest = largest + str(num)
    return int(largest)

numbers = [23, 34, 55]
print(create_largest_number(numbers))
