import pandas as pd

df = pd.read_csv("/Users/laristch/Desktop/reprograma/on33-python-s09-pandas-numpy-I/material/mais_ouvidas_2024.csv")

print(df.head())

# Identificar colunas que contêm números e converter para o tipo numérico
for coluna in df.columns:
    if df[coluna].dtype == 'object':
        try:
            df[coluna] = pd.to_numeric(df[coluna].str.replace(",", ""), errors='raise')
        except ValueError:
            # Se não for possível converter, ignorar essa coluna
            pass
print(df.dtypes)

# Corrigir a coluna 'Release Date' para o formato datetime
df['Release Date'] = pd.to_datetime(df['Release Date'], errors='coerce')
print(df.dtypes)

# Criar a coluna 'Streaming Popularity' (média das colunas de popularidade)
df['Streaming Popularity'] = df[['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts']].mean(axis=1)

# Criar a coluna 'Total Streams' (soma das colunas de streams)
df['Total Streams'] = df[['Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', 'Soundcloud Streams']].sum(axis=1)

# Filtrar as faixas conforme as condições
filtered_df = df[(df['Spotify Popularity'] > 80) & (df['Total Streams'] > 1000000)]

# Salvar o DataFrame resultante em um novo arquivo JSON
filtered_df.to_json('faixas_filtradas.json', index=False)

print(filtered_df.head())




