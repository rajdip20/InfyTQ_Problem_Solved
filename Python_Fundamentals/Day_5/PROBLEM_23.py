''' A teacher is in the process of generating a few reports based on the marks scored by the
    students of her class in a project based assessment.
    
    Assume that the marks of her 10 students are available in a tuple. The marks are out of 25.
    
    Write a python program to implement the following functions:
        1. find_more_than_average(): Find and return the percentage of students who have scored
            more than the average mark of the class.
        2. generate_frequency(): Find how many students have scored the same marks. For
            example, how many have scored 0, how many have scored 1, how many have scored
            3….how many have scored 25. The result should be populated in a list and returned.
        3. sort_marks(): Sort the marks in the increasing order from 0 to 25. The sorted values
            should be populated in a list and returned.

    Sample Input               |            Expected Output
_______________________________|______________________________________________________________
   list_of_marks =             |70.0
(12,18,25,24,2,5,18,20,20,21)  |
                               |[0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 2,
                               |1, 0, 0, 1, 1]
                               |
                               |[2, 5, 12, 18, 18, 20, 20, 21, 24, 25]

'''

def find_more_than_avarage(marks):
    avg = sum(marks)/len(marks)
    count = 0
    for mark in marks:
        if mark > avg:
            count += 1
    return (count / len(marks))*100

def generate_frequency(marks):
    l = []
    for i in range(26):
        l.append(0)
    for mark in marks:
        l[mark] = l[mark] + 1
    return l

def sort_marks(marks):
    return sorted(list(marks))

list_of_marks = (12, 18, 25, 24, 2, 5, 18, 20, 20, 21)
print(find_more_than_avarage(list_of_marks))
print(generate_frequency(list_of_marks))
print(sort_marks(list_of_marks))
