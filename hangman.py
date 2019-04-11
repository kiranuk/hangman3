# hangman.py
"import random to get random word from word file"
import random



def get_secret_word(word_file="/usr/share/dict/words"):
    "Take words randomly"
    with open(word_file) as file1:
        good_words = []
        for i in file1:
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
    "Mask the word with * char"
    ret = []
    for i in word:
        if i in guesses:
            ret.append(i)
        else:
            ret.append('*')
    return ''.join(ret)


def status(secret_word, guesses, turns):
    "Prints the current status"
    return """
    Secret word : {}
    Guessed letters : {}
    turns : {}
    """.format(mask_word(secret_word, guesses),
               ' '.join(sorted(guesses)),
               turns)


def guess_word(secret_word, guesses, letter, turns):
    "Returns the remaining turns"
    if letter not in guesses:
        guesses.append(letter)
    else:
        return turns
    if letter not in secret_word:
        return turns - 1
    else:
        return turns


def final_status(mask, secret_word, turns):
    "To give final status lie win/lose statement"
    if "*" not in mask:
        print("\n\U0001F44d\U0001f44D You did it")
        return True
    if turns == 0:
        print("sorry!! The secret word was {}".format(secret_word))
        return True






def main():
    print("Welcome to Hangman game!")
    secret_word = get_secret_word(word_file="/usr/share/dict/words")
    guesses = []
    print(mask_word(secret_word, guesses))
    print(secret_word)
    turns = 10
    while True:
        mask = mask_word(secret_word, guesses)
        if final_status(mask, secret_word, turns):
            break
        letter = input("Enter a letter: ")
        turns = guess_word(secret_word, guesses, letter, turns)
        print(status(secret_word, guesses, turns))


if __name__ == '__main__':
    main()
