# hangman.py

import random

def get_secret_word(word_file="/usr/share/dict/words"):
    with open(word_file) as f:
        good_words = []
        for i in f:
            i = i.strip()
            if len(i) <= 6:     # No short words
                continue
            if not i.isalpha(): # No punctuation
                continue
            if i[0].isupper():  # No proper nouns
                continue
            good_words.append(i)
    return random.choice(good_words)
def get_guess_word(s):
    n = len(s)
    l = "*"*n
    return l

def get_tries_left(n=10):
    for i in range(10,-1,-1):
        if i == 0:
            print("Zero chances left, Exit!!")
        elif i > 0:
            i = i - 1
            print("%l chances left")

def get_wrong_guess_word(n=10, word1, word2):
    for i in range(10):
        if word1 != word2:
            print("%i guess so far")
        else:
            break

