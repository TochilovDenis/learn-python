"""
Задача 2024.10.16.03

Написать функцию для генерации строки из n строчных и заглавных латинских букв, а также числе и символов

Заглавные должны добавляться в строку только если параметр use_uppercase в функции равен True.
А если параметр use_uppercase не указан при использовании функции, то генерируем строку только из строчных букв.

По тому же сценарию добавляем контроль использования цифр и символов
"""

from random import choice
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def generate_random_str(n: int, use_uppercase: bool = False, use_digits = False, use_punctuation = False) -> str:
    chars: str = ascii_lowercase
    if use_uppercase:
        chars += ascii_uppercase
    if use_digits:
        chars += digits
    if use_punctuation:
        chars += punctuation

    return ''.join(choice(chars) for _ in range(n))

if __name__ == '__main__':
    print(generate_random_str(10, use_uppercase=True))
    print(generate_random_str(10, use_uppercase=True, use_digits=True))
    print(generate_random_str(10, use_uppercase=True, use_punctuation=True))