import requests
import os
from dotenv import load_dotenv
import json
from datetime import datetime

load_dotenv()

api_brew = os.getenv('API_BREW')
path_bronze = os.getenv('PATH_BRONZE')
path_bronze_arquivo = os.getenv('PATH_BRONZE_ARQUIVO')
session = requests.Session()
current_datetime = datetime.now().strftime('%Y_%m_%d')

def dados_json_api(url):
    response = requests.get(api_brew)
    if response.status_code == 200:
        raw = session.get(url, timeout=10).json()
        if raw:
            with open(os.path.join(path_bronze_arquivo, f'brewery_raw__{current_datetime}.json'), 'w') as f:
                json.dump(raw, f)
            print('Arquivo criado com sucesso')
        else:
            print('A API não retornou dados, arquivo não criado')
    else:
        raise Exception(f"Erro ao acessar a API: {response.status_code}")
     
    return raw


