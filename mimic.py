#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = "Paul Racisz, Ruben Espino"

import random
import sys


def create_mimic_dict(filename):
    with open(filename, "r") as textfile:
        """ https://github.com/geetarista/google-python-exercises/blob/master/basic/solution/mimic.py We re-wrote 
        the answer with our own variables, making sure that we understood the solution"""
        # see comments below for our demonstration of understanding! VVVV
        wordDict = {}
        words = textfile.read()
        splitWords = words.split()
        previousWord = ''
        for word in splitWords:
            # check to see if word is already in dict
            if previousWord not in wordDict:
                # if previousWord isn't there add it,
                wordDict[previousWord] = [word]
                word
            else:
                # else append the new previousWord
                wordDict[previousWord].append(word)
                previousWord = word
        return print(wordDict)
    """Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """
    """

        PART A:
    1.) Open the file
    2.) make an empty dictionary
    3.) set the dictionary to a list of the words that come after each word
        "my dog is small"
         0  1   2  3
         i[0] = key
         [my, dog, is, small]
         i[1] = value
         {"": [my] "my": ["dog", "sister"] "dog": [is]
         "is" :[small] "sister": [hates]
         "hates": [me] "me": ""}
        "my sister hates me"
        duplicate key ^^^
        # look up how to add keys and values to dictionaries
    4.) find a duplicate in the dictionary
    5.) if a duplicate exists, do not add a key
    6.) add iterator to the dictionary as the key
    7.) add the next word as a value
    8.) loop through every word in the file
    9.) make another list with every word in the file
    10.) compare lists and add the value as
    the word after iterator word for each word.

        PART B:
    4.) Print a word
    5.) look for words come next
    6.) pick one at random to replace the next word.
    7.) return the next jumbled version of the txt file.


    GOAL: Jumbled version of the file inserting
    random words that came after the original word
    """


def print_mimic(mimic_dict, start_word):
    """Given a previously created mimic_dict and start_word,
    prints 200 random words from mimic_dict as follows:
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process 200 times
    """
    # +++your code here+++
    pass


# Provided main(), calls mimic_dict() and print_mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
        sys.exit(1)

    d = create_mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
