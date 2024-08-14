import pandas as pd
import os

# Carregando o arquivo CSV
df = pd.read_csv('C:/Users/bruno/Desktop/REPROG/on33-python-s09-pandas-numpy-I/material/mais_ouvidas_2024.csv')

# Verificando as primeiras linhas para garantir o carregamento
print(df.head())
print(df.columns)

# Verificando valores nulos e duplicados
print("Valores nulos por coluna:")
print(df.isnull().sum())
print("Duplicados:")
print(df.duplicated().sum())

# Identificando e convertendo colunas numéricas usando pd.to_numeric
num_cols = ['Spotify Streams', 'YouTube Views', 'TikTok Likes', 'Shazam Counts', 
            'Spotify Popularity', 'Pandora Streams', 'Soundcloud Streams' , 'Tiktok Views']

for col in num_cols:
    if col in df.columns:
        # Convertendo colunas para numérico, forçando a remoção de caracteres não numéricos
        df[col] = pd.to_numeric(df[col].str.replace(',', '').str.replace('', ''), errors='coerce')

# Corrigindo a coluna 'Release Date' para o formato datetime
df['Release Date'] = pd.to_datetime(df['Release Date'], errors='coerce')

# Verificando se todas as colunas estão corretas
print("Tipos de dados das colunas:")
print(df.dtypes)

# Verificando se todas as colunas envolvidas na soma são numéricas
sum_cols = ['Spotify Streams', 'YouTube Views', 'TikTok Likes', 'Pandora Streams', 'Soundcloud Streams']
for col in sum_cols:
    if col not in df.columns:
        print(f"Coluna {col} não encontrada no DataFrame.")

# Criando a coluna com a média das plataformas
df['Streaming Popularity'] = df[['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts']].mean(axis=1)

# Criando a coluna 'Total Streams' somando os valores das diferentes plataformas
df['Total Streams'] = df[sum_cols].sum(axis=1)

# Filtrando faixas com alta popularidade
filtered_df = df[(df['Spotify Popularity'] > 80) & (df['Total Streams'] > 1_000_000)]

# Salvando o DataFrame resultante em um novo arquivo JSON
filtered_df.to_json('faixas_filtradas.json', orient='records', lines=True)

# Verificando se o arquivo JSON foi salvo corretamente
if os.path.exists('faixas_filtradas.json'):
    print("Arquivo 'faixas_filtradas.json' foi salvo com sucesso!")
else:
    print("Erro ao salvar o arquivo 'faixas_filtradas.json'.")
