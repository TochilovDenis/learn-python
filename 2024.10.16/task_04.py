"""
Задача 2024.10.16.04

Добавьте в генератор опцию, которая будет контролировать разрешены ли в строке повторяющиеся символы.
И если не разрешены, то нельзя допускать повторяющихся символов в строке.
"""

from random import choice, sample
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def generate_random_str(n: int, use_uppercase: bool = False, use_digits = False, use_punctuation = False, allow_duplicates = False) -> str:
    chars: str = ascii_lowercase
    result: list = []

    for _ in range(n):
        char = choice(chars)
        result.append(char)

    if use_uppercase:
        chars += ascii_uppercase
    if use_digits:
        chars += digits
    if use_punctuation:
        chars += punctuation

    if allow_duplicates:
        return ''.join(sample(chars, n))

    return ''.join(result)


if __name__ == '__main__':
    print(generate_random_str(10, use_uppercase=True))
    print(generate_random_str(10, use_uppercase=True, use_digits=True))
    print(generate_random_str(10, use_uppercase=True, use_punctuation=True))
    print(generate_random_str(10, use_uppercase=True, allow_duplicates=True))