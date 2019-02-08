# hangman.py

import random

def get_secret_word(word_file="/usr/share/dict/words"):
    with open(word_file) as f:
        words = [x.strip() for x in f if len(x.strip()) >= 6]
    
    return random.choice(words)
        
