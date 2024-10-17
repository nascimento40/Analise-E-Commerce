import pandas as pd
import os

def carregar_limpar_dados(pasta_arquivos):
    arquivos_csv = [os.path.join(pasta_arquivos, f) for f in os.listdir(pasta_arquivos) if f.endswith('.csv')]
    
    dados_lista = [pd.read_csv(arquivo) for arquivo in arquivos_csv]
    dados_combinados = pd.concat(dados_lista, ignore_index=True)
    
    dados_combinados.dropna(inplace=True)
    dados_combinados['hora_evento'] = pd.to_datetime(dados_combinados['event_time'])
    dados_combinados['dia_da_semana'] = dados_combinados['hora_evento'].dt.day_name()
    dados_combinados['hora'] = dados_combinados['hora_evento'].dt.hour
    
    return dados_combinados

pasta_arquivos = 'dados/'

dados_limpos = carregar_limpar_dados(pasta_arquivos)

dados_limpos.to_csv('dados/ecommerce_data_limpos.csv', index=False)

print("Os dados foram carregados e limpos com sucesso.")
print(f"Número de linhas após a limpeza: {len(dados_limpos)}")
print("Os dados limpos foram salvos no arquivo: dados/ecommerce_data_limpos.csv")
