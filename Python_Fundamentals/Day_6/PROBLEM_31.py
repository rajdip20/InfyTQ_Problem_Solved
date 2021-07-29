''' Write a python function find_duplicates(), which accepts a list of numbers and returns
    another list containing all the duplicate values in the input list. If there are no duplicate values,
    it should return an empty list.
    
    Sample Input                                Expected Output
[12,54,68,759,24,15,12,68,987,758,25,69]            [12, 68]
'''

def find_duplicates(l):
    unique = []
    duplicate = []
    for i in l:
        if i in unique:
            if i not in duplicate:
                duplicate.append(i)
        else:
            unique.append(i)
    return duplicate

print(find_duplicates([12, 54, 68, 759, 24, 15, 12, 68, 987, 758, 25, 69]))
