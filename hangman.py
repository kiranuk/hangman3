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

def mask_word(word, guesses):
    ret = []
    for i in word:
        if i in guesses:
            ret.append(i)
        else:
            ret.append('*')
    return ' '.join(ret)

def status(word, guesses, turns):
    return """Secret word : {}
    Guessed letters : {}
    turns : {}
    """.format(mask_word(word, guesses),
            ' '.join(sorted(guesses)),
            turns)

def guess_word(word, guesses, letter, turns):
    if letter not in word:
        guesses.append(letter)
        return turns - 1, False
    else:
        return turns, False

def main():
    print("Welcome to Hangman game!")
    word = get_secret_word(word_file="/usr/share/dict/words")
    guesses = []
    global turns
    while True:
        mask = mask_word(word, guesses)
        print(mask)
        letter = input("Enter a letter: ")
        turns, success = guess_word(word, guesses, letter, turns)
        print(status(word, guesses, turns))
        if turns == 0:
            print(f"sorry!! The secret word was {word}")
            break
        if success:
            print("You did it!!")
            break

if __name__ == '__main__':
    main()
