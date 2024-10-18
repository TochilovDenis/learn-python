import requests  # импорт библиотеки requests

url = 'https://date.nager.at/api/v3/AvailableCountries' # создал и инициировал переменную url
payload = {
    'countryCode': '',
    'name': ''
}
res = requests.get(url, params=payload)
data = res.text

print(data)
