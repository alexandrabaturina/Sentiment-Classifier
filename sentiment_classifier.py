twitter_file = open('files/project_twitter_data.csv', 'r')
data_file = open('fies/resulting_data.csv', 'w')

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# list of positive words to use
positive_words = []
with open('files/positive_words.txt') as pos_f:
    for line in pos_f:
        if line[0] != ';' and line[0] != '\n':
            positive_words.append(line.strip())

# list of negative words to use
negative_words = []
with open('files/negative_words.txt') as pos_f:
    for line in pos_f:
        if line[0] != ';' and line[0] != '\n':
            negative_words.append(line.strip())


def strip_punctuation(s):
    '''(string) -> string

    Return the string s with removed characters considered as punctuation chars.
    '''
    for char in punctuation_chars:
        s = s.replace(char, '')
    return s


def get_pos(s):
    ''' (string) -> int

    Return the number of occurrences of positive words in the string s
    which represents one or more sentences.
    '''
    count = 0
    for word in strip_punctuation(s.lower()).split():
        if word in positive_words:
            count +=1
    return count


def get_neg(s):
    ''' (string) -> int

    Return the number of occurrences of negative words in the string s
    which represents one or more sentences.
    '''
    count = 0
    for word in strip_punctuation(s.lower()).split():
        if word in negative_words:
            count +=1
    return count


def write_to_file(file):
    ''' (file open to read)

    Read, calculate, and write some data from file opened to read to other file.
    '''
    data_file.write("Number of Retweets, Number of Replies, Positive Score, \
                    Negative Score, Net Score\n")
    lines = file.readlines()[1:]
    for line in lines:
        # read line contents ignoring the header
        l_contents = line.strip().split(',')
        data_file.write("{}, {}, {}, {}, {} \n".format (
                        l_contents[1],
                        l_contents[2],
                        get_pos(l_contents[0]),
                        get_neg(l_contents[0]),
                        (get_pos(l_contents[0]) - get_neg(l_contents[0]))))

write_to_file(twitter_file)
twitter_file.close()
data_file.close()
