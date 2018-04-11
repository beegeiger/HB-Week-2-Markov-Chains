"""Generate Markov text from text files."""
import string
import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    long_text = open(file_path).read()  # .decode('utf-8', 'ignore')
    return long_text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    # Split text
    words = text_string.split()

    # Loop through text
    for num in range(len(words) - 2):  # Add pairs (as keys) and values to dictionary
        key = (words[num], words[num + 1])
        value = words[num + 2]

        if chains.get(key) is None:
            chains[key] = [value]
        else:
            chains[key].append(value)

    return chains


def make_text(chains):
    """Return text from chains."""

    word_text = []
    
    # add random key to start
    random_key = choice(chains.keys())
    word_text.extend(random_key)
    
    # loop through word_text
    while True:
        key = (word_text[-2], word_text[-1])
        if chains.get(key):
            value = chains[key]
            word_text.append(choice(value))

        else:
            break

    return " ".join(word_text)


def make_n_text(chains, n):
    """Return text from chains."""
    loop = 0
    word_text = []
    # add random key to start
    random_key = choice(chains.keys())
    word_text.extend(random_key)
    # loop through word_text
    while True:

        #create key of n length
        key = []

        for word in word_text[-n:]:
            key.append(word)

        key = tuple(key)

        # Add new words to text
        if chains.get(key):
            if len(word_text) < 1000:
                value = chains[key]  # look up value of key
                random_value = choice(value)
                word_text.append(random_value) # pick random word and append to text
            else:
                break        #break

        else:
            break

    return " ".join(word_text)


def return_n_tweet(markov_text, n = 280):
    # Find start of sentence "Capital letter"
    # terminate end of sentence.
    # n/2
    index = 0
    while True:
        
        if markov_text[index] == ".":
            markov_text = markov_text[index + 2:]
            break
        
        index += 1
    print markov_text

def make_n_chain(text_string, n):
    chains = {}
    text_string = text_string.translate(None, string.digits)
    index = 0
    new_string = ''


    while index < len(text_string):
        
        if text_string[index] == "[":
            index += 3
        else:
            new_string = new_string + text_string[index]
            index += 1

    # for index, character in enumerate(text_string, 0):
    #     print character
    #     if character == "[":
    #         print 'found'
    #         new_string = text_string[:index]


    words = new_string.split()

    # Loop through text
    for num in range(len(words) - n):  # Add keys and values to dictionary
        value = words[num + n]

        # create key of n length
        key = []

        for index in range(num, num + n):
            key.append(words[index])

        key = tuple(key)

        # add values to key as a list
        if chains.get(key) is None:
            chains[key] = [value]
        else:
            chains[key].append(value)

    return chains


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
#chains = make_chains(input_text)
n = int(sys.argv[2])
chains = make_n_chain(input_text, n)

# Produce random text
#random_text = make_text(chains)
random_text = make_n_text(chains, n)

return_n_tweet(random_text)

print random_text
