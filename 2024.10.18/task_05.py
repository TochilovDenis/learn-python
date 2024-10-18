import requests  # импорт библиотеки requests

def  get_list_of_available_countries() -> list[dict[str, str]]:
    url = 'https://date.nager.at/api/v3/AvailableCountries'
    res = requests.get(url).json()
    return res

def main() -> None:
    countries = get_list_of_available_countries()
    for country in countries:
        print(country['name'],  country['countryCode'])


if __name__ == '__main__':
    main()
