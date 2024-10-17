import pandas as pd
import plotly.express as px

dados = pd.read_csv('dados/ecommerce_data_limpos.csv')

print(dados.head())

print("Tipos de eventos únicos no dataset:", dados['event_type'].unique())

def criar_painel_interativo(dados):
    compras = dados[dados['event_type'] == 'purchase']

    if compras.empty:
        print("Nenhum evento de compra encontrado nos dados.")
        return

    compras_por_data = compras.groupby('hora_evento').size().reset_index(name='contagem_compras')

    fig = px.line(compras_por_data, x='hora_evento', y='contagem_compras', title='Compras ao Longo do Tempo')
    fig.show()

criar_painel_interativo(dados)
