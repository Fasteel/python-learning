# no link

import random


def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


running = True
min_input = 0
max_input = 100
random_number = random.randint(min_input, max_input)

while running:
    user_input = input('Entrez un nombre')

    if not is_int(user_input):
        print('You should enter int value')
        continue

    user_input = int(user_input)

    if user_input > max_input or user_input < min_input:
        print('Value should be between ' + str(min_input) + ' and ' + str(max_input))

    elif user_input == random_number:
        print('You win !')
        running = False

    elif user_input > random_number:
        print('It\'s lower')

    else:
        print('It\'s greater')
