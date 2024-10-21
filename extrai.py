 
def main():
    from  utils.extrai_api import dados_json_api
    import os
    from dotenv import load_dotenv
    #carrega dados env. 
    load_dotenv()
    api_brew = os.getenv('API_BREW')
    dados_json_api(api_brew)
 
main()
