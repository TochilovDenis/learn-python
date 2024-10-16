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
    def __init__(self, n, use_uppercase = False, use_digits = False, use_punctuation = False,
                 allow_duplicates = False):
        self.n: int = n
        self.use_uppercase: bool = use_uppercase
        self.use_digits: bool = use_digits
        self.use_punctuation: bool = use_punctuation
        self.allow_duplicates: bool = allow_duplicates
        self.chars = ascii_lowercase


    def get_string(self) -> str:
        if self.use_uppercase:
            self.chars += ascii_uppercase
        if self.use_digits:
            self.chars += digits
        if self.use_punctuation:
            self.chars += punctuation

        if self.allow_duplicates:
            return ''.join(sample(self.chars, self.n))

        result = []
        for _ in range(self.n):
            char = choice(''.join(self.chars))
            result.append(char)

        return ''.join(result)

    def get_lowercase(self) -> str:
        return self.get_string()

    def get_uppercase(self) -> str:
        return self.get_string()

    def get_digits(self) -> str:
        return self.get_string()

    def get_punctuation(self) -> str:
        return self.get_string()


if __name__ == '__main__':
    generator = RandomGenerator(10)
    print(generator.get_string())
    generator = RandomGenerator(10, use_uppercase=True)
    print(generator.get_lowercase())
    generator = RandomGenerator(10, use_uppercase=True, use_digits=True)
    print(generator.get_uppercase())
    generator = RandomGenerator(10, use_uppercase=True, use_punctuation=True)
    print(generator.get_digits())
    generator = RandomGenerator(10, use_uppercase=True, use_digits=True, use_punctuation=True, allow_duplicates=True)
    print(generator.get_punctuation())