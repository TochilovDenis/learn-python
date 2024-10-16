"""
Задача 2024.10.16.05

Переделайте функцию в класс RandomGenerator, в конструктор он принимает то же, что и функция в 4-й задаче.

Объект генерирует строку в методе get_string().

Также у него должен быть метод генерирующий строку только строчных букв, только заглавных букв,
только цифр и только символов.
"""
from random import choices, sample
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, punctuation

class RandomGenerator:
    def __init__(self, n = 10):
        self.n: int = n
        self.chars = ascii_letters

    def get_string(self) -> str:
        return ''.join(choices(population=self.chars, k=self.n))

    def get_lowercase(self) -> str:
        return ''.join(sample(population=ascii_lowercase, k=self.n))

    def get_uppercase(self) -> str:
        return ''.join(sample(population=ascii_uppercase, k=self.n))

    def get_digits(self) -> str:
        return ''.join(sample(population=digits, k=self.n))

    def get_punctuation(self) -> str:
        return ''.join(sample(population=punctuation, k=self.n))

if __name__ == '__main__':
    generator = RandomGenerator()
    print(generator.get_string())
    print(generator.get_lowercase())
    print(generator.get_uppercase())
    print(generator.get_digits())
    print(generator.get_punctuation())