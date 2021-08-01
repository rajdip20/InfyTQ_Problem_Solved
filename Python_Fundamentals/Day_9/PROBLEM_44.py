''' Write a python function, remove_duplicates() which accepts a string and removes all
    duplicate characters from the given string and return it.
    
            Sample Input                Expected Output
    1122334455ababzzz@@@123#*#*            12345abz@#*
'''

def remove_duplicates(string):
    output = ''
    for c in string:
        if c not in output:
            output = output + c
    return output


print(remove_duplicates("1122334455ababzzz@@@123#*#*"))
