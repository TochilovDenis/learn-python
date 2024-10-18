import requests  # импорт библиотеки requests

def  get_list_of_available_countries() -> list[dict[str, str]]:
    url = 'https://date.nager.at/api/v3/AvailableCountries'
    res = requests.get(url).json()
    return res

def main() -> None:
    countries = get_list_of_available_countries()
    for country in countries:
        if country['name'] == 'Russia':
            print(f"Страна Russia, код [{country['countryCode']}]")
            return

    print('Страна Russia не найдена')


if __name__ == '__main__':
    main()

