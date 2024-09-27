import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv("C:/Users/Colaborador/Reprograma/on33-python-s09-pandas-numpy-I/material/mais_ouvidas_2024.csv")

# Exibir as primeiras linhas para garantir que foi carregado corretamente
print(df.head())

colunas_numericas = ['Spotify Streams', 'YouTube Views', 'TikTok Views', 
                     'Pandora Streams', 'Soundcloud Streams', 'Spotify Popularity', 
                     'TikTok Likes', 'Shazam Counts']

# converter para numérico
df[colunas_numericas] = df[colunas_numericas].replace(',', '', regex=True).astype(float)

# Verificar se as colunas foram convertidas corretamente
print(df[colunas_numericas].dtypes)

df['Release Date'] = pd.to_datetime(df['Release Date'], errors='coerce')

print(df['Release Date'].head())

df['Streaming Popularity'] = df[['Spotify Popularity', 'YouTube Views', 
                                  'TikTok Likes', 'Shazam Counts']].mean(axis=1)

# cálculo da média
print(df[['Spotify Popularity', 'Streaming Popularity']].head())

df['Total Streams'] = df[['Spotify Streams', 'YouTube Views', 'TikTok Views', 
                          'Pandora Streams', 'Soundcloud Streams']].sum(axis=1)

# cálculo da soma
print(df[['Total Streams']].head())

faixas_filtradas = df[(df['Spotify Popularity'] > 80) & (df['Total Streams'] > 1_000_000)]

# faixas filtradas
print(faixas_filtradas.head())

