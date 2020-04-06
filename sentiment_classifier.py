punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            

def strip_punctuation(s):
    '''
    (string) -> string

    Return the string s with removed characters considered as punctuation chars.

    >>> strip_punctuation("#Amazing")
    Amazing
    >>> strip_punctuation("#in.cred..ible!")
    incredible
    '''
    for char in punctuation_chars:
        s = s.replace(char, '')
    return s
