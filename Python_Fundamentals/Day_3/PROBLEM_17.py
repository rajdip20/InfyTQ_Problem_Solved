''' Represent a small bilingual (English-Swedish) glossary given below as a Python dictionary

    {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

    and use it to translate your Christmas wishes from English into Swedish.

    That is, write a python function translate() that accepts the bilingual dictionary and a list of
    English words (your Christmas wish) and returns a list of equivalent Swedish words. 
'''

def translate(bil_dict, wish):
    wish_list = wish.split(" ")
    translated_list = []
    for word in wish_list:
        translated_list.append(bil_dict[word])
    t_wish = " ".join(translated_list)
    return t_wish

bil_dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
wish = "merry christmas and happy new year"
print(translate(bil_dict, wish))
