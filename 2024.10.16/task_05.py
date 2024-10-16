"""
Задача 2024.10.16.05

Переделайте функцию в класс RandomGenerator, в конструктор он принимает то же, что и функция в 4-й задаче.

Объект генерирует строку в методе get_string().

Также у него должен быть метод генерирующий строку только строчных букв, только заглавных букв,
только цифр и только символов.
"""
from random import choice, sample
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

class RandomGenerator:
    def __init__(self, n = 10, use_uppercase = False, use_digits = False, use_punctuation = False):
        self.n: int = n
        self.use_uppercase: bool = use_uppercase
        self.use_digits: bool = use_digits
        self.use_punctuation: bool = use_punctuation
        self.chars = ascii_lowercase

    def get_string(self) -> str:
        return ''.join(sample(self.chars, self.n))

    def get_lowercase(self) -> str:
        return ''.join(sample(ascii_lowercase, self.n))

    def get_uppercase(self) -> str:
        return ''.join(sample(ascii_uppercase, self.n))

    def get_digits(self) -> str:
        return ''.join(sample(digits, self.n))

    def get_punctuation(self) -> str:
        return ''.join(sample(punctuation, self.n))

if __name__ == '__main__':
    generator = RandomGenerator(10, use_uppercase=True, use_digits=True, use_punctuation=True)
    print(generator.get_string())
    print(generator.get_lowercase())
    print(generator.get_uppercase())
    print(generator.get_digits())
    print(generator.get_punctuation())