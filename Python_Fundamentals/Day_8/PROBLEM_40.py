''' Write a python program that accepts a text and displays a string which contains the word
    with the largest frequency in the text and the frequency itself separated by a space.
    
    Rules:
        1. The word should have the largest frequency.
        2. In case multiple words have the same frequency, then choose the word that has the
            maximum length.
    
    Assumptions:
        1. The text has no special characters other than space.
        2. The text would begin with a word and there will be only a single space between the
            words.

    Perform case insensitive string comparisons wherever necessary.
    
  |                     Sample Input                                           |  Expected |
  |                                                                            |  Output   |
  |____________________________________________________________________________|___________|
  | "Work like you do not need money love like you have never been hurt and    |  like 3   |
  | dance like no one is watching"                                             |           |
  |____________________________________________________________________________|___________|
  |"Courage is not the absence of fear but rather the judgement that something |  fear 2   |
  | else is more important than fear"                                          |           |
  |____________________________________________________________________________|___________|
'''

def largest_frequency_word(string):
    string = string.lower()
    words = string.split(" ")
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1
    max_freq = max(word_count.values())
    max_freq_words = []
    for word in word_count:
        if word_count[word] == max_freq:
            max_freq_words.append(word)
    if len(max_freq_words) == 1:
        return max_freq_words[0] + " " + str(max_freq)
    else:
        max_length = 0
        max_word = ''
        for word in max_freq_words:
            if len(word) > max_length:
                max_length = len(word)
                max_word = word
        return max_word + " " + str(max_freq)


print(largest_frequency_word("Work like you do not need money love like you have never been hurt and dance like no one is watching"))
