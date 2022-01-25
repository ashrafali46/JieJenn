import json
from datetime import datetime
import requests


class CurrencyConverter:
    base_url = 'http://api.currencylayer.com/live'

    def __init__(self, API_KEY):
        self.API_KEY = API_KEY

    def requestCurrency(self):
        params = {'access_key': self.API_KEY}
        response = requests.get(CurrencyConverter.base_url, params=params)
        response_json = json.loads(response.content)

        if response.status_code != 200:
            print('Failed to import currency exchange rates.')
            print(response.reason)
            return None
        elif not response_json['success']:
            print('Failed to import currency exchange rates.')
            print(response_json['error']['info'])
            return None
        else:
            timestamp = datetime.fromtimestamp(response_json['timestamp']).strftime('%d-%m-%Y')
            base_currency = response_json['source']
            quotes = response_json['quotes']
            return {
                'base': base_currency,
                'timestamp': timestamp,
                'quotes': quotes
            }


if __name__ == '__main__':
    c1 = CurrencyConverter('3ece61d3ec6d85eeb638aa8576a81836')
    print(c1.requestCurrency())