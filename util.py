import random
import os
import assets

def get_random_word() -> str:
    return random.choice(assets.WORDS)

def get_initial_placeholder(word: str) -> list[str]:
    return ['_'] * len(word)

def get_initial_attempts() -> int:
    return len(assets.IMAGES)

def print_placeholder(word: str) -> None:
    for char in word:
        print(char, end=' ')

def print_image(attempts: int) -> None:
    print(assets.IMAGES[attempts-1])

def get_user_input() -> str:
    msg = 'Choose a letter: '
    return input(msg).upper()

def clear() -> None:
    os.system('clear')
    os.system('cls')

def user_has_won(word: str) -> bool:
    return "_" not in word

def user_has_lost(attempts: int) -> bool:
    return attempts == 0

def print_message_win() -> None:
    print('Ganaste!!')

def print_message_lose() -> None:
    print('Perdiste :(')