from bs4 import BeautifulSoup
import requests


class TextCollor:
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[1;31m'
    ENDC = '\033[0m'


currencys = [
    ['EUR', 'Euro'],
    ['USD', 'US Dollar'],
    ['JPY', 'Japanischer Yen'],
    ['AUD', 'Australischer Dollar'],
    ['GBP', 'Britischer Pfund']
]

conversion_values = [
    # Euro
    ['EUR/USD', 1.131],
    ['EUR/JPY', 127.998],
    ['EUR/AUD', 1.600],
    ['EUR/GBP', 0.850],
    # USD
    ['USD/EUR', 0.884],
    ['USD/JPY', 113.340],
    ['USD/AUD', 1.417],
    ['USD/GBP', 0.753],
    # Japanese Yen
    ['JPY/EUR', 0.885],
    ['JPY/USD', 113.340],
    ['JPY/AUD', 1.417],
    ['JPY/GBP', 0.753],
    # Australischer Dollar
    ['AUD/EUR', 0.885],
    ['AUD/USD', 113.340],
    ['AUD/JPY', 1.417],
    ['AUD/GBP', 0.753],
    # Britisch Pound
    ['JPY/EUR', 0.885],
    ['JPY/USD', 113.340],
    ['JPY/AUD', 1.417],
    ['JPY/GBP', 0.753],
]
print(currencys[4][0])
print(f'{TextCollor.YELLOW}Willkommen zum Währungsrechner!{TextCollor.ENDC}')

print(f'Verfügbare {TextCollor.GREEN}Währungen{TextCollor.ENDC}: '
      f'{currencys[0][1]} [{TextCollor.GREEN}{currencys[0][0]}{TextCollor.ENDC}],'
      f'{currencys[1][1]} [{TextCollor.GREEN}{currencys[1][0]}{TextCollor.ENDC}],'
      f'{currencys[2][1]} [{TextCollor.GREEN}{currencys[2][0]}{TextCollor.ENDC}],'
      f'{currencys[3][1]} [{TextCollor.GREEN}{currencys[3][0]}{TextCollor.ENDC}],'
      f'{currencys[4][1]} [{TextCollor.GREEN}{currencys[4][0]}{TextCollor.ENDC}]'
      )

from_currency = str.upper(input('Bitte gib die Währung ein, von der du umrechnen möchtest: '))
to_currency = str.upper(input('Bitte gib die Währung ein, in die du umrechnen möchtest: '))

merged_currencys_user_input = f'{from_currency}/{to_currency}'

j = 0
while j < len(conversion_values):
    if conversion_values[j][0] == merged_currencys_user_input:
        print(f'Der Umrechnungskurs für {TextCollor.GREEN}{conversion_values[j][0]}{TextCollor.ENDC} '
              f'beträgt: {TextCollor.GREEN}{conversion_values[j][1]}{TextCollor.ENDC}')
        value = input('Gib bitte den Betrag ein, den du umrechnen möchtest: ')
        result = f'Das Ergebnis beträgt: {TextCollor.GREEN}{int(value) * conversion_values[j][1]}{TextCollor.ENDC}' \
                 f' {TextCollor.GREEN}{to_currency}{TextCollor.ENDC}'
        print(result)
        break
    j += 1
