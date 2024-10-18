import requests  # импорт библиотеки requests

url = 'http://api.forismatic.com/api/1.0/' # создал и инициировал переменную url
payload = {                 # уточнённые настройки нашего запроса
    'method': 'getQuote',   # мы указываем, что метод - это getQuote или ПолучитьЦитату
    'format': 'json',       # мы указываем, что формат - это json
    'lang': 'ru'}           # мы указываем, что нам нужна цитата на русском языке
res = requests.get(url, params=payload) # создал переменную res и сохранил в неё результат работы функции requests.get
# res - это response - ответ

data = res.json() # создал переменную data и сохранил в неё результат работы функции res.json

print(data) # вывел data на экран
