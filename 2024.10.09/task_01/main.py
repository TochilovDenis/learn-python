INITIAL_STR: str = "Строка1; Строка2. Строка3."
SEPARATORS: list =  [';', '.']

def text_split(s: str, separators: str) -> list[str]:
    for separator in separators:
        return s.split(separator)


if __name__ == '__main__':
    print(text_split(INITIAL_STR, SEPARATORS))

