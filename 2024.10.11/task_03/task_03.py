from random import randint, seed

def text_random_split(text: str) -> list[str]:
    result: list[str] = []
    left = 0
    right = 1

    while right > left != len(text):
        right = randint(left + 1, len(text))
        result.append(text[left: right])
        left = right
        right += 1

    return result


if __name__ == '__main__':
    seed()
    texts: str = "Что?.. Да! Вышел корень из тумана; Вынул ножик из кармана. Раз, два, всё?.. "
    print(texts, '\nДлина текста:', len(texts))
    results = text_random_split(texts)
    print(results)