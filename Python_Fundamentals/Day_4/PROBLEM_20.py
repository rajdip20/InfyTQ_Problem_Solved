'''  Write a function, check_palindrome() to check whether the given string is a palindrome or
    not. The function should return true if it is a palindrome else it should return false.

    Note: Initialize the string with various values and test your program. Assume that all the letters
    in the given string are all of the same case. Example: MAN, civic, WOW etc.
'''

def is_palindrome(word):
    half = len(word) // 2
    for i in range(half):
        if word[i] != word[-(i + 1)]:
            return "Not a Palindrome"
    return "Palindrome"

w = input("Enter your word: ")
print(is_palindrome(w))
