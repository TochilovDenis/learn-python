def text_split_by_separators(texts: str, separators: list[str]) -> list[str]:
    """
    Разделяет входную строку по указанным разделителям.
    :param texts: Входная строка для разделения.
    :param separators: Список разделителей для использования.
    :return list[str]: Список строк, полученных после разделения.
    """
    result: list[str] = [''] # Инициализируем список результатов с пустым элементом
    waiting_for_separator = True # Флаг для отслеживания ожидания разделителя
    for symbol in texts: # Проходим по каждому символу во входной строке
        if waiting_for_separator: # Если мы ожидаем разделитель
            if symbol in separators: # Если текущий символ является разделителем, устанавливаем флаг False
                waiting_for_separator = False
        else:
            if not symbol in separators and symbol != ' ': # Если текущий символ не является разделителем и не пробелом
                result.append('')  # Добавляем новый пустой элемент в список результатов
                waiting_for_separator = True  # Устанавливаем флаг True, чтобы начать ожидание следующего разделителя

        result[-1] += symbol # Добавляем текущий символ к последнему элементу списка результатов

    return result # Возвращаем список результатов после обработки всей строки


if __name__ == '__main__':
    # Инициализируем входную строку
    initial_str: str = "Строка1; Строка2. Строка3."
    # Определяем список разделителей
    seps: list[str] = [';', '.']
    # Вызываем функцию с параметрами и выводим результат
    print(text_split_by_separators(initial_str, seps))