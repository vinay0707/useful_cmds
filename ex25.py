def break_words(stuff):
    words = stuff.split(' ')
    return words


def sort_words(words):
    return sorted(words)


def print_first_word( words ):
    word = words.pop(0)
    return word


def print_last_word(words):
    word = words.pop(-1)
    return word


sentence = "All good things come to those who wait."
words = break_words(sentence)
print words


print sort_words(words)
print print_first_word(words)
print print_last_word(words)