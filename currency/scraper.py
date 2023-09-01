import re

import requests
from bs4 import BeautifulSoup


def current_currency_rate(currency: str):
    url = f"https://fa.navasan.net/dayRates.php?item={currency.lower()}"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    divs = soup.find('div', {'class': 'idesc lastrate pos'})

    if divs is None:
        divs = soup.find('div', {'class': 'idesc lastrate neg'})

        if divs is None:
            divs = soup.find('div', {'class': 'idesc lastrate'})

        if divs is not None:
            return re.sub(r'\s+', ' ', divs.text).strip()
        else:
            return "?"

    else:
        return re.sub(r'\s+', ' ', divs.text).strip()
