"""Generate Markov text from text files."""

import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    long_text = open(file_path).read()  #.decode('utf-8', 'ignore')
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
    #Split text
    words = text_string.split()

    #Loop through text
    for num in range(len(words) -2):  #Add pairs (as keys) and values to dictionary
        key = (words[num], words[num + 1])
        value = words[num + 2]

        if chains.get(key) is None:
            chains[key] = [value]
        else:
            chains[key].append(value)
    # your code goes here

    return chains


def make_text(chains):
    """Return text from chains."""

    word_text = []
    # add random key to start
    random_key = choice(chains.keys())
    word_text.extend(random_key)
    # loop through word_text
    while True:
        if chains.get((word_text[-2], word_text[-1])):
            value = chains[(word_text[-2], word_text[-1])]
            word_text.append(choice(value))

        else:
            break

    return " ".join(word_text)


def make_n_text(chains, n):
    """Return text from chains."""

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

        if chains.get(key):
            value = chains[key]
            word_text.append(choice(value))

        else:
            break


    return " ".join(word_text)


def make_n_chain(text_string, n):
    chains = {}
    #Split text
    words = text_string.split()

    #Loop through text
    for num in range(len(words) - n):  # Add pairs (as keys) and values to dictionary
        key = []  # (words[num], words[num + 1])
        value = words[num + n]

        #create key of n length
        for index in range(num, num + n):
            key.append(words[index])

        key = tuple(key)

        if chains.get(key) is None:
            chains[key] = [value]
        else:
            chains[key].append(value)
    # your code goes here

    return chains


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

chains = make_n_chain(input_text, 4)

random_text = make_n_text(chains, 4)

# Get a Markov chain
#chains = make_chains(input_text)

# Produce random text
#random_text = make_text(chains)

print random_text
