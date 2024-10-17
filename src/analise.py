import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv('dados/ecommerce_data_limpos.csv')

def analisar_padroes_compra(dados):
    compras = dados[dados['event_type'] == 'purchase']
    plt.figure(figsize=(10, 6))
    sns.countplot(x='dia_da_semana', data=compras, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    plt.title('Compras por Dia da Semana')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.countplot(x='hora', data=compras)
    plt.title('Compras por Hora do Dia')
    plt.show()

def plotar_heatmap_tempo(dados):
    compras = dados[dados['event_type'] == 'purchase']
    heatmap_dados = compras.pivot_table(index='dia_da_semana', columns='hora', aggfunc='size', fill_value=0)
    heatmap_dados = heatmap_dados.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    plt.figure(figsize=(12, 6))
    sns.heatmap(heatmap_dados, cmap='Blues')
    plt.title('Heatmap de Compras: Dias da Semana vs Horas do Dia')
    plt.show()

analisar_padroes_compra(dados)
plotar_heatmap_tempo(dados)
