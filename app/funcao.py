import requests
url = 'https://api.openbrewerydb.org/v1/breweries'


def check_status():
    raw = requests.get(url)
    return raw.status_code