'''  Write a python function, encrypt_sentence() which accepts a message and encrypts it based
    on rules given below and returns the encrypted message.
    
    Words at odd position -> Reverse It
    Words at even position -> Rearrange the characters so that all consonants appear before the
    vowels and their order should not change
    
    Note:
        1. Assume that the sentence would begin with a word and there will be only a single space
            between the words.
        2. Perform case sensitive string operations wherever necessary.
    
    Also write the pytest test cases to test the program.
    
        Sample Input                                Expected Output
    the sun rises in the east                   eht snu sesir ni eht stea
    
    Estimated Time: 40 minutes
'''
def encrypt_sentence(sentence):
    words = sentence.split(" ")
    encrypt = []
    for i in range(len(words)):
        if i % 2 == 0:
            encrypt.append(words[i][::-1])
        else:
            vowel_set = set("aeiouAEIOU")
            vowels = []
            consonants = []
            for letter in words[i]:
                if letter in vowel_set:
                    vowels.append(letter)
                else:
                    consonants.append(letter)
            encrypt.append("".join(consonants + vowels))
    return " ".join(encrypt)

print(encrypt_sentence("the sun rises in the east"))
