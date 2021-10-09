from operator import itemgetter

from util import (clear, get_init_config, get_user_input, print_image,
                  print_placeholder, user_has_lost, user_has_won)


def play():
    attempts, word, diplay_word = itemgetter(
        'attempts', 'word', 'display_word')(get_init_config())

    while not user_has_lost(attempts):
        clear()
        print_image(attempts)
        print_placeholder(diplay_word)
        user_letter: str = get_user_input()
        found: bool = False
        for i, letter in enumerate(word):
            if letter == user_letter:
                diplay_word[i] = letter
                found = True

        if not found:
            attempts -= 1

        if user_has_won(diplay_word):
            clear()
            print('Ganaste!!')
            return

    clear()
    print('Perdiste :(')
