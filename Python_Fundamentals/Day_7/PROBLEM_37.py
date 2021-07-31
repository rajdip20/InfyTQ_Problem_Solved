''' Write python function, sms_encoding() which accepts a sentence and converts it into an
    abbreviated sentence to be sent as SMS and returns the abbreviated sentence.
    
    Rules are as follows:
        a. Spaces are to be retained as is
        b. Each word should be encoded separately
            ● If a word has only vowels then retain the word as is
            ● If a word has a consonant (at least 1) then retain only those consonants
    Note: Assume that the sentence would begin with a word and there will be only a single space
    between the words.
    
        Sample Input                  |  Expected Output
   ___________________________________|______________________
    I love Python                     |I lv Pythn
   ___________________________________|______________________
    MSD says I love cricket and       |MSD sys I lv crckt nd
    tennis too                        |tnns t
   ___________________________________|______________________
    I will not repeat mistakes        |I wll nt rpt mstks
                                      |
    Estimated time: 45 minutes
'''

def sms_encoding(text):
    words = text.split(" ")
    encoded = []
    vowel_set = set("aeiouAeiou")
    for word in words:
        flag = 0
        for letter in word:
            if letter not in vowel_set:
                flag = 1
                break
        if flag == 0:
            encoded.append(word)
        else:
            enc = ''
            for letter in word:
                if letter not in vowel_set:
                    enc = enc + letter
            encoded.append(enc)
    return " ".join(encoded)


print(sms_encoding("MSD says I love cricket and tennis too"))
