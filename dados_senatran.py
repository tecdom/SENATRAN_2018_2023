# %% importando libs
import pandas as pd
import numpy as np
import os 
import urllib3
from bs4 import BeautifulSoup

# %% fazendo o download do arquivo
url = 'http://dados.transportes.gov.br/dataset/42e2320b-ea67-4fdc-896f-71363e043fc6/resource/6b54cd7b-0693-4b2f-b4ae-d3ce90c299bc/download/renaest_dabertos_20230713.zip'
conexao =  urllib3.PoolManager()
retorno = conexao.request('GET',url)
pagina = BeautifulSoup(retorno.data,"html.parser")

# %% Abrindo arquivo de dados
df=pd.read_csv('./renaest_dabertos_20230613/Acidentes_DadosAbertos_20230613.csv')
df.head()
