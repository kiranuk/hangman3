# test_hangman.py

import hangman

# 1. Secret word should have atleast 6 letters
# 2. Secret word should have no punctuation
# 3. Secret word should not be a proper noun

def test_secret_word_6_letters():
    assert all(hangman.get_secret_word("./test_data/1.words") == "policeman" for _ in range(100))

def test_secret_word_no_punctuation():
    assert all(hangman.get_secret_word("./test_data/2.words") == "fireman" for _ in range(100))

def test_secret_word_no_proper_nouns():
    assert all(hangman.get_secret_word("./test_data/3.words") == "policeman" for _ in range(100))

def test_guess_word():
    assert (hangman.guess_word("elephant") == "********")

def test_tries_left():
    assert (hangman.tries_left(10) == "9 tries left" for _ in range(10))

def test_wrong_guess_word():
    assert (hangman.wrong_guess_word(s) == "Guess so far q,w,e,r" for _ in range(10))


