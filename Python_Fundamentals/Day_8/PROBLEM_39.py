''' Write a python function, check_anagram() which accepts two strings and returns True, if
    one string is an anagram of another string. Otherwise returns False.
    
    The two strings are considered to be an anagram if they contain repeating characters but none
    of the characters repeat at the same position. The length of the strings should be the same.
    
    Note: Perform case insensitive comparison wherever applicable.

    Sample Input           |                Expected Output
   ________________________|__________________________________________
    eat, tea               |                True
   ________________________|__________________________________________
    backward,drawback      |                False
                           |        (Reason: character 'a' repeats at
                           |        position 6, not an anagram)
   ________________________|__________________________________________
    Reductions,discounter  |                True
   ________________________|__________________________________________
    About, table           |                False
'''

def check_anagram(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    letter_count = {}
    position_check = {}
    for i in range(len(str1)):
        if str1[i] in letter_count:
            letter_count[str1[i]] = letter_count[str1[i]] + 1
            position_check[str1[i]].append(i)
        else:
            letter_count[str1[i]] = 1
            position_check[str1[i]] = list()
            position_check[str1[i]].append(i)

    for i in range(len(str2)):
        if str2[i] in letter_count:
            letter_count[str2[i]] = letter_count[str2[i]] - 1
            if letter_count[str2[i]] == 0:
                letter_count.pop(str2[i])
            if i in position_check[str2[i]]:
                return False
        else:
            return False
    if len(letter_count) == 0:
        return True
    else:
        return False


print(check_anagram('About', 'table'))
