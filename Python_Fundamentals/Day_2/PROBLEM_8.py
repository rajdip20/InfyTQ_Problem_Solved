''' A teacher in a school wants to find and display the grade of a student based on his/her
percentage score. The criterion for grades is as given below:
    Score (both inclusive)                      Grade

    Between 80 and 100                            A
    Between 73 and 79                             B
    Between 65 and 72                             C
    Between 0 and 64                              D
    Any other value                               Z

Assume that the percentage score is a whole number. Write a python program for the above
requirement. '''

while True:
    n = int(input("Enter the student's percentage: "))
    
    if n >= 80 and n <= 100:
        print("A")
    elif n >= 73 and n <= 79:
        print("B")
    elif n >= 65 and n <= 72:
        print("C")
    elif n >= 0 and n <= 64:
        print("D")
    else:
        print("Z")

    ch = input("Do you want to continue?[Y/N] ")

    if ch.upper() == 'N':
        break
