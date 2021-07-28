''' Write a python function, find_pairs_of_numbers() which accepts a list of positive integers
    with no repetitions and returns count of pairs of numbers in the list that adds up to n. The
    function should return 0, if no such pairs are found in the list.

    Sample Input                    Expected Output
[1, 2, 7, 4, 5, 6, 0, 3], 6                 3
[3, 4, 1, 8, 5, 9, 0, 6], 9                 4

'''

def find_pairs_of_numbers(l, n):
    count = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == n:
                count += 1
    return count


print(find_pairs_of_numbers([3, 4, 1, 8, 5, 9, 0, 6], 9))
