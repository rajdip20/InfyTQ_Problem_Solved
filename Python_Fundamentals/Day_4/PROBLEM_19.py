''' Given a string containing uppercase characters (A-Z), compress the string using Run Length
    encoding. Repetition of character has to be replaced by storing the length of that run.
    Write a python function which performs the run length encoding for a given String and returns
    the run length encoded String.

    Provide different String values and test your program.

    Sample Input            Expected Output
    AAAABBBBCCCCCCCC            4A4B8C
    AABCCA                     2A1B2C1A
'''

def run_length_encoding(string):
    string = string.upper()
    prev_letter = string[0]
    prev_letter_count = 0
    output = ""

    for current_letter in string:
        if current_letter == prev_letter:
            prev_letter_count += 1
        else:
            output = output + str(prev_letter_count) + prev_letter
            prev_letter = current_letter
            prev_letter_count = 1
    output = output + str(prev_letter_count) + prev_letter
    return output

s = input("Enter your string: ")
print(run_length_encoding(s))
