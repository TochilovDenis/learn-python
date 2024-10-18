import requests  # импорт библиотеки requests

def  get_list_of_available_countries() -> list[dict[str, str]]:
    url = 'https://date.nager.at/api/v3/AvailableCountries'
    res = requests.get(url).json()
    return res

def main() -> None:
    countries = get_list_of_available_countries()
    result: dict = {}
    for country in countries:
        result[country['name']] = country['countryCode']

    if 'Russia' in result:
        print(f'Страна Russia, код [{result["Russia"]}]')
    else:
        print(f"Страна Russia не найдена")

if __name__ == '__main__':
    main()
