"""
Задача 2024.10.16.01
Написать функцию для генерации строки из n строчных латинских букв
"""
from random import choice
from string import ascii_lowercase


def generate_random_str(n: int) -> str:
    return ''.join(choice(ascii_lowercase) for _ in range(n))

if __name__ == '__main__':
    print(generate_random_str(10))