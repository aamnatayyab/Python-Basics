# Exercise: Write a function that "translates" a list of words! It expects a list of words and a dictionary of translations of words, 
# and replaces each word with its translation. It also has a keyword argument called "reverse" with a default value of False. 
# If it's true, then the translation should occur in the reverse direction.

from reverse_sequence import rev_str

words = ['the', 'happy', 'dog', 'was', 'happy', 'and', 'a', 'dog']
translate_dict = {'the': 'a',
                  'happy': 'boldog',
                  'dog': 'kutya',
                  'was': 'volt',
                  'and': 'es',
                  'a': 'egy'}
def translate(ls, dict, reverse):
    for i in range(len(ls)):
        if reverse:
           ls[i] = rev_str(dict[ls[i]])
        else:
            ls[i] = dict[ls[i]]
    return ls
print(translate(words, translate_dict, True))
# print(translate(words, translate_dict, False))