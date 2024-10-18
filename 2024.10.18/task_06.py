# Импортируем библиотеку requests для выполнения HTTP-запросов
import requests

# Определяем список стран, которые нам интересны
COUNTRY: list[str] = ['Russia', 'Andorra']

# Функция для получения списка всех доступных стран
def get_list_of_available_countries() -> list[dict[str, str]]:
    url = 'https://date.nager.at/api/v3/AvailableCountries' # URL API для получения списка доступных стран
    res = requests.get(url).json()  # Выполняем GET-запрос к API и получаем JSON-ответ

    return res  # Возвращаем список словарей с информацией о странах


# Функция для создания словаря с нужными странами
def get_dict_of_available_countries(countries: list[dict[str, str]]) -> dict[str, str]:
    result: dict[str, str] = dict()  # Создаем пустой словарь для хранения результата
    # Проходим по каждой стране в списке
    for country in countries:
        # Проверяем, является ли текущая страна одной из тех, что нам нужны
        if country['name'] in COUNTRY:
            result[country['name']] = country['countryCode']  # Добавляем страну в словарь с ее кодом

    return result  # Возвращаем созданный словарь


def main() -> None:
    countries = get_list_of_available_countries()
    dict_countries = get_dict_of_available_countries(countries)

    # Выводим весь полученный словарь
    print(dict_countries)

    # Проходим по каждой стране в нашем словаре и выводим ее имя и код
    for country, code in dict_countries.items():
        print(f"{country}: {code}")


if __name__ == '__main__':
    main()