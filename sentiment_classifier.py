punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(s):
    '''
    (string) -> string

    Return the string s with removed characters considered as punctuation chars.

    >>> strip_punctuation("#Amazing")
    Amazing
    >>> strip_punctuation("#in.cred..ible!)
    incredible
    '''
    for char in punctuation_chars:
        s = s.replace(char, '')
    return s
