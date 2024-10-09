def text_split(s: str, separator: str) -> list[str]:
    return s.split(separator)


if __name__ == '__main__':
    print(text_split("Hello Dex", '\n'))

