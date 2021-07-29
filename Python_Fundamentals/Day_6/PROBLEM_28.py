''' A 10-substring of a number is a substring of its digits that sum up to 10.

    For example, the 10-substrings of the number 3523014 are:
    3523014, 3523014, 3523014, 3523014
    
    Write a python function, find_ten_substring(num_str) which accepts a string and returns the list
    of 10-substrings of that string.
    
    Handle the possible errors in the code written inside the function.
    
    Sample Input                                Expected Output
    '3523014'                           ['5230', '23014', '523', '352']
'''

def find_ten_substring(num_str):
    l=[]
    for i in range(len(num_str)):
        for j in range((i + 1), (len(num_str) + 1)):
            if sum([int(d) for d in num_str[i:j]]) == 10:
                l.append(num_str[i:j])
    return l

print(find_ten_substring("3523014"))
