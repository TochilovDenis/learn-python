import requests  # импорт библиотеки requests

url = 'http://api.forismatic.com/api/1.0/' # создал и инициировал переменную url
payload = {                 # уточнённые настройки нашего запроса
    'method': 'getQuote',   # мы указываем, что метод - это getQuote или ПолучитьЦитату
    'format': 'text',       # мы указываем, что формат - это text
    'lang': 'en'            # мы указываем, что нам нужна цитата на русском языке
}
res = requests.get(url, params=payload) # создал переменную res и сохранил в неё результат работы функции requests.get
# res - это response - ответ

data = res.text  # создал переменную data и сохранил в неё результат работы функции res.text

print(data)