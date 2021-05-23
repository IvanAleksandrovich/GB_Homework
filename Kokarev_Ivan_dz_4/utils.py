import requests
from datetime import datetime

user_input = input('Введите код валюты: ').upper()


def currency_rates():
    url = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    url_text = url.text.split('><')
    date_server = url.headers['Date']
    date = datetime.strptime(date_server, '%a, %d %B %Y %H:%M:%S %Z')
    for el in url_text:
        if el == f'CharCode>{user_input}</CharCode':
            idx = url_text.index(el)
            currency_val = float(url_text[idx + 3][6:-7].replace(',', '.'))
            return currency_val, date.date()


result = currency_rates()
print(f'1 {user_input} = {result[0]} руб. на {result[1]}')
