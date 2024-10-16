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
        chars_to_use: list[str] = [self.chars]
        if self.use_uppercase:
            chars_to_use.append(ascii_uppercase)
        if self.use_digits:
            chars_to_use.append(digits)
        if self.use_punctuation:
            chars_to_use.append(punctuation)

        if self.allow_duplicates:
            return ''.join(sample(''.join(chars_to_use), self.n))

        result = []
        for _ in range(self.n):
            char = choice(''.join(chars_to_use))
            result.append(char)
        return ''.join(result)


if __name__ == '__main__':
    rg = RandomGenerator(10)
    print(rg.get_string())
    rg = RandomGenerator(10, use_uppercase=True)
    print(rg.get_string())
    rg = RandomGenerator(10, use_uppercase=True, use_digits=True)
    print(rg.get_string())
    rg = RandomGenerator(10, use_uppercase=True, use_punctuation=True)
    print(rg.get_string())
    rg = RandomGenerator(10, use_uppercase=True, allow_duplicates=True)
    print(rg.get_string())