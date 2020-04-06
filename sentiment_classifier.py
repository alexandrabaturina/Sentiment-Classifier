punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# list of negative words to use
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


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


def get_pos(s):
    '''
    (string) -> int

    Return the number of occurrences of positive words in the string s
    which represents one or more sentences.
    '''
    count = 0
    for word in strip_punctuation(s.lower()).split():
        if word in positive_words:
            count +=1
    return count
