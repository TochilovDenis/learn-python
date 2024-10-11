def text_split_by_separators(texts: list[str], separators: list[str]) -> list[str]:
    """
    Разделяет входную строку по указанным разделителям.
    :param texts: Входная строка для разделения.
    :param separators: Список разделителей для использования.
    :return list[str]: Список строк, полученных после разделения.
    """
    result: list[str] = ['']
    waiting_for_separator = True
    for symbol in texts:
        if waiting_for_separator:
            if symbol in separators:
                waiting_for_separator = False
        else:
            if not symbol in separators and symbol != ' ':
                result.append('')
                waiting_for_separator = True

        result[-1] += symbol

    return result


if __name__ == '__main__':
    initial_list_str: list[str] = ['Дем', 'онстра', 'ция!']
    seps: list[str] = ['.', ',', '?', '!']
    print(text_split_by_separators(initial_list_str, seps))