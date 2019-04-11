# hangman.py

import random
import sys


def get_secret_word(word_file="/usr/share/dict/words"):
    with open(word_file) as f:
        good_words = []
        for i in f:
            i = i.strip()
            if len(i) <= 6:     # No short words
                continue
            if not i.isalpha():  # No punctuation
                continue
            if i[0].isupper():  # No proper nouns
                continue
            good_words.append(i)
    return random.choice(good_words)


def mask_word(word, guesses):
    ret = []
    for i in word:
        if i in guesses:
            ret.append(i)
        else:
            ret.append('*')
    return ''.join(ret)


def status(secret_word, guesses, turns):
    return """
    Secret word : {}
    Guessed letters : {}
    turns : {}
    """.format(mask_word(secret_word, guesses),
               ' '.join(sorted(guesses)),
               turns)


def guess_word(secret_word, guesses, letter, turns):
    if letter not in guesses:
        guesses.append(letter)
    else:
        return turns
    if letter not in secret_word:
        return turns - 1
    else:
        return turns


def winning_statement(mask, secret_word, turns):
    if "*" not in mask:
        print("\n\U0001F44d\U0001f44D You did it")
        return True
    if turns == 0:
        print("sorry!! The secret word was {}".format(secret_word))
        return True



#def losing_statement(secret_word, turns):


def main():
    print("Welcome to Hangman game!")
    secret_word = get_secret_word(word_file="/usr/share/dict/words")
    guesses = []
    print(mask_word(secret_word, guesses))
    turns = 10
    while True:
        mask = mask_word(secret_word, guesses)
        letter = input("Enter a letter: ")
        turns = guess_word(secret_word, guesses, letter, turns)
        print(status(secret_word, guesses, turns))
        if winning_statement(mask, secret_word, turns):
            break


if __name__ == '__main__':
    main()
