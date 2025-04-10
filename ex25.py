def break_words(stuff):
    """This function will break up words for us."""             # documentation comments
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""                                      # documentation comments
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""           # documentation comments
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""            # documentation comments
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""# documentation comments
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""      # documentation comments
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""   # documentation comments
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)