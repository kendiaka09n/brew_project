import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

path_raw_arquivo = os.getenv('PATH_RAW_ARQUIVO')
path_curated_arquivo = os.getenv('PATH_CURATED_ARQUIVO')
current_datetime = datetime.now().strftime('%Y_%m_%d')

fonte = os.listdir(path_raw_arquivo)
dfpq = pd.read_parquet(path_raw_arquivo)
print(dfpq[dfpq['id']=='fb94830f-6196-4f59-9189-c9060b778085'].head(5))