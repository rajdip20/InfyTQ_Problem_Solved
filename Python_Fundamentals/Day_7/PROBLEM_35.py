''' Write a python function, find_correct() which accepts a dictionary and returns a list as per
    the rules mentioned below.
    The input dictionary will contain correct spelling of a word as key and the spelling provided by a
    contestant as the value.
    
    The function should identify the degree of correctness as mentioned below:
    CORRECT, if it is an exact match
    
    ALMOST CORRECT, if no more than 2 letters are wrong
    WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by
    contestant) mismatches.
    
    and return a list containing the number of CORRECT answers, number of ALMOST CORRECT
    answers and number of WRONG answers.
    Assume that the words contain only uppercase letters and the maximum word length is 10.
    
    Also write the pytest test cases to test the program.
    
                        Sample Input                                    |           Expected
                                                                        |           Output
    ____________________________________________________________________|______________________
    {"THEIR": "THEIR", "BUSINESS":                                      |           [2, 2, 1]
    "BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}    |

    Estimated Time: 40 minutes
'''


def find_correct(word_dict):
    correct_count = 0
    almost_count = 0
    wrong_count = 0
    for word, input_word in word_dict.items():
        if len(word) == len(input_word):
            flag = 0
            for i in range(0, len(word)):
                if word[i] != input_word[i]: 
                    flag = flag + 1
            if flag == 0: 
                correct_count = correct_count + 1
            elif flag <= 2: 
                almost_count = almost_count + 1
            else: 
                wrong_count = wrong_count + 1
        else: 
            wrong_count = wrong_count + 1
    return list((correct_count, almost_count, wrong_count))
            
word_dict = {"THEIR": "THEIR", "BUSINESS": "BISINESS", "WINDOWS": "WINDMILL", "WERE": "WEAR", "SAMPLE": "SAMPLE"}
print(find_correct(word_dict))
