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
    while(n >= 0):
        if n == 0:
            l = print("too bad try next time!!")
        else:
            l = print("chances left {}".format(n))
            n 1= n - 1
        return l

def get_wrong_guess_word():
    guess_word = []
    letter = get_ask_to_type()
    if letter not in get_secret_word():
        print('\nGuess so far {}'.format(letter))
        m.append(letter)
    return m

def get_ask_to_type():
    w = []
    s = input("Enter a letter: ")
    check1 = s.isalpha()
    check2 = s.islower()
    if (check1 == True and check2 == True):
        for i in get_secret_word():
            if s == i:
                w.append(s)
                print(w)
                continue
            else:
                continue
if '__name__' == '__main__':
    main()

print("Welcome to hangman game")
while True:
    play_game = input('ready to play? y or n')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        l = get_secret_word(word_file="/usr/share/dict/words")
        l1 = get_guess_word(l)
        print(l1)
        l2 = get_ask_to_type()
        get_wrong_guess_word()
        get_tries_left(n=10)
    




 
