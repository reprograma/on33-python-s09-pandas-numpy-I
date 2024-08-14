import pandas as pd

# Carregando o arquivo csv
df = pd.read_csv('C:/Users/bruno/Desktop/REPROG/on33-python-s09-pandas-numpy-I/material/mais_ouvidas_2024.csv')

# Verificando as primeiras linhas para garantir que o carregamento
print(df.head())
print(df.columns)

# verificando valores nulos e duplicados
print("Valores nulos por coluna:")
print(df.isnull().sum())
print("Duplicados:")
print(df.duplicated().sum())

# Identificando e convertendo colunas numéricas
num_cols = ['Spotify Streams', 'YouTube Views', 'TikTok Likes', 'Shazam Counts', 
            'Spotify Popularity', 'Pandora Streams', 'Soundcloud Streams']

for col in num_cols:
    if df[col].dtype == 'object':
        df[col] = pd.to_numeric(df[col].str.replace('[\$,]', '', regex=True), errors='coerce')

# Corrigindo a coluna 'Release Date' para o formato datetime
df['Release Date'] = pd.to_datetime(df['Release Date'], errors='coerce')

# Criando a coluna 'Streaming Popularity' como a média das plataformas
df['Streaming Popularity'] = df[['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts']].mean(axis=1)

# Criando a coluna 'Total Streams' somando os valores das diferentes plataformas
df['Total Streams'] = df[['Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', 'Soundcloud Streams']].sum(axis=1)

# Filtrando faixas com alta popularidade
filtered_df = df[(df['Spotify Popularity'] > 80) & (df['Total Streams'] > 1_000_000)]

# Salvando o DataFrame resultante em um novo arquivo JSON :) quase lá...
filtered_df.to_json('faixas_filtradas.json', orient='records', lines=True)

# Verificando se o arquivo JSON foi salvo corretamente '-'
import os
if os.path.exists('faixas_filtradas.json'):
    print("Arquivo 'faixas_filtradas.json' foi salvo com sucesso!")
else:
    print("Erro ao salvar o arquivo 'faixas_filtradas.json'.")