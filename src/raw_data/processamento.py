import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

path_landing = os.getenv('PATH_LANDING')
path_landing_arquivo = os.getenv('PATH_LANDING_ARQUIVO')
path_raw_arquivo = os.getenv('PATH_RAW_ARQUIVO')
current_datetime = datetime.now().strftime('%Y_%m_%d')

fila_processamento = []
data_processamento = []

def processa_raw():
    for i in os.listdir(path_landing_arquivo):
        arquivo = (i.split('.')[0].split('__'))
        arquivo_tempo =  datetime.strptime(arquivo[1], '%Y_%m_%d').strftime('%Y_%m_%d')
        if arquivo_tempo == current_datetime:
            fila_processamento.append(i)
            data_processamento.append(arquivo_tempo)
        else:
            print(f'Arquivo não atualizado {arquivo}')
    print(fila_processamento)

    json_processado = f'{path_landing_arquivo}\{fila_processamento[0]}'
    print(f'Arquivo a ser processado é o {json_processado}')

    df = pd.read_json(json_processado)
    df['data_atualizacao'] = data_processamento[0]

    colunas_json= ['id','name','brewery_type','address_1','address_2','address_3', 
                                    'city','state_province', 'postal_code', 'country', 'longitude', 
                                    'latitude', 'phone', 'website_url', 'state', 'street']
    #print(df.isnull().any())
    #print(df['state_province'].unique())
    #print(df['state'].unique())
    #print(df['country'].unique())
    #print(df[df['country'] == 'Ireland']['state_province'])
    if os.listdir(path_raw_arquivo):
        dfpq = pd.read_parquet(path_raw_arquivo)
        df_nao_alterado = dfpq.merge(df, 
                                on=['id','name','brewery_type','address_1','address_2','address_3', 
                                    'city','state_province', 'postal_code', 'country', 'longitude', 
                                    'latitude', 'phone', 'website_url', 'state', 'street']
                                    , how = "outer", indicator=True)
        df_novos_dados = df_nao_alterado[df_nao_alterado['_merge'] == 'right_only']
        df_novos_dados= df_novos_dados[colunas_json]
        df_dados_atuais = df_nao_alterado[df_nao_alterado['_merge'] != 'right_only']
        df_dados_atuais = df_dados_atuais[colunas_json]
        df_final = pd.concat([df_dados_atuais,df_novos_dados], ignore_index=True)
        df_final.to_parquet(path_raw_arquivo, index=False, partition_cols=['state'])
        print(df_novos_dados.count().sum(), 'linhas atualizadas')

    else:
        
        df.to_parquet(path_raw_arquivo, index=False, partition_cols=['state'])
        print(df.count().sum(),' linhas criadas')

processa_raw()