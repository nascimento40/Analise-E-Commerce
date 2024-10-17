# Análise de Vendas e Marketing em E-commerce

Este projeto analisa o comportamento de compra dos clientes em uma loja de cosméticos usando dados de eventos de e-commerce (cliques, carrinhos e compras). O objetivo é identificar padrões de compra e fornecer insights que podem ser usados para otimizar campanhas de marketing.

## Passo a Passo para Rodar o Projeto

1. **Baixe o Dataset**
   - Baixe os dados do [Kaggle](https://www.kaggle.com/datasets/mkechinov/ecommerce-events-history-in-cosmetics-shop).
   - Coloque o arquivo de dados dentro da pasta `dados/`. Caso queira substituir os já existentes.

2. **Instale as Dependências**
    pip install pandas matplotlib seaborn plotly

3. **Carregar e Limpar os Dados**
   - Execute o script `limpeza_dados.py` para carregar e limpar os dados:
     ```bash
     python src/limpeza_dados.py
     ```
   - Isso processa os dados, removendo valores nulos e criando colunas para dias da semana e horas dos eventos.

4. **Análise de Padrões de Compra**
   - Execute o script `analise.py` para gerar gráficos que mostram os padrões de compras por dia da semana e hora do dia:
     ```bash
     python src/analise.py
     ```
   - Esse script também gera um heatmap que mostra o volume de compras por dias da semana e horas do dia.

5. **Criar Painel Interativo**
   - Execute o script `painel_interativo.py` para gerar gráficos interativos de cliques e compras ao longo do tempo:
     ```bash
     python src/painel_interativo.py
     ```
   - Os gráficos serão exibidos no navegador, permitindo interatividade para explorar os dados de cliques e compras.

6. **Outros Arquivos**
   - `notebooks/analise.ipynb`: Caso queira explorar ou testar os dados interativamente, você pode usar o Jupyter Notebook.

## Estrutura de Arquivos

- `dados/`: Coloque o arquivo CSV dos dados nesta pasta.
- `src/`: Contém os scripts para limpeza, análise e criação do painel interativo.
- `notebooks/`: Contém um notebook Jupyter para análises adicionais, caso deseje usar.
- `requisitos.txt`: Arquivo contendo as dependências necessárias.
- `README.txt`: Este arquivo de instruções.

## Objetivo

O objetivo deste projeto é fornecer insights sobre o comportamento dos clientes para otimizar campanhas de marketing, como focar nos dias e horários de maior volume de compras.
