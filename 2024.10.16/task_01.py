"""
Задача 2024.10.16.01
Написать функцию для генерации строки из n строчных латинских букв
"""
from random import choices
from string import ascii_lowercase


def generate_random_str(n: int) -> str:
    # chars = ascii_lowercase
    # result = []
    # for _ in range(n):
    #     char = choice(chars)
    #     result.append(char)
    # return ''.join(result)
    # return ''.join(choice(ascii_lowercase) for _ in range(n))
    return ''.join(choices(population=ascii_lowercase, k=n))


if __name__ == '__main__':
    print(generate_random_str(10))