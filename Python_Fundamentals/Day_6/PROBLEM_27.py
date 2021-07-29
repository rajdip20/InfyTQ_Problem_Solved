''' Write a recursive function, is_palindrome() to find out whether a string is a palindrome or
    not. The function should return true, if it is a palindrome. Else it should return false.
    
    Note- Perform case insensitive operations wherever necessary.
'''

def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:len(word) - 1])

print(is_palindrome('ABBA'))
