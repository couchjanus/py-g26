import re
import requests
import json

# Python-скрипт, который реализует логику конкретных запросов курсов валют.
# Используемый API - PrivatBank API.
# URL: https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5.

URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

def load_exchange():
   return json.loads(requests.get(URL).text)

def get_exchange(key):
    for item in load_exchange():
        if key == item['ccy']:
            return item
    return False

def get_exchanges(ccy_pattern):
    result = []
    ccy_pattern = re.escape(ccy_pattern) + '.*'
    for exc in load_exchange():
        if re.match(ccy_pattern, exc['ccy'], re.IGNORECASE) is not None:
            result.append(exc)
    return result

e_now = get_exchange('USD')
print(e_now)
