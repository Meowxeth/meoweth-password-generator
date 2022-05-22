import enum
from random import randint

# default :
# 14 letter long password is going to be generated

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special_characters = ['!', '@', '#', "$", '&', '?', '%']


def pick_lowercase_letters(amount):
    return [alphabet[randint(0, 25)] for i in range(amount)]


def pick_uppercase_letters(amount):
    return [alphabet[randint(0, 25)].upper() for i in range(amount)]


def pick_special_characters(amount):
    return [special_characters[randint(0, 6)] for i in range(amount)]


def pick_numbers(amount):
    return [str(randint(0, 9)) for i in range(amount)]

# total amount / 2 = length of generated password


def generate(lowercase_amount=8, uppercase_amount=8, special_char_amount=5, number_amount=5):
    scrambled = []
    unscrambled = (pick_lowercase_letters(lowercase_amount) +
                   pick_uppercase_letters(uppercase_amount) +
                   pick_special_characters(special_char_amount) +
                   pick_numbers(number_amount))
    for i in enumerate(unscrambled):
        picked_index = randint(0, len(unscrambled) - 1)
        scrambled.append(unscrambled[picked_index])
        # the line below removes the picked letter from the unscrambled list.
        unscrambled.pop(picked_index)
    return ''.join(scrambled)


print(generate())
