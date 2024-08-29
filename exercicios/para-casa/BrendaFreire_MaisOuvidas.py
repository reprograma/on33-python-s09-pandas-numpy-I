import pandas as pd

# ['Track', 'Album Name', 'Artist', 'Release Date', 'ISRC', 'All Time Rank', 'Track Score', 'Spotify Streams','Spotify Playlist Count', 'Spotify Playlist Reach','Spotify Popularity', 'YouTube Views', 'YouTube Likes', 'TikTok Posts','TikTok Likes', 'TikTok Views', 'YouTube Playlist Reach','Apple Music Playlist Count', 'AirPlay Spins', 'SiriusXM Spins','Deezer Playlist Count', 'Deezer Playlist Reach','Amazon Playlist Count', 'Pandora Streams', 'Pandora Track Stations','Soundcloud Streams', 'Shazam Counts', 'TIDAL Popularity','Explicit Track']

# 1° passo: Use o arquivo `mais_ouvidas_2024.csv` para análise. Lembre-se de garantir que o carregamento foi feito com sucesso.
df = pd.read_csv(r"C:\Users\brend\Desktop\REPROGRAMA\semana11\on33-python-s09-pandas-numpy-I\exercicios\para-casa\mais_ouvidas_2024.csv")
print(df.head())

# 2° passo: Identifique as colunas que contêm números, e converta essas colunas para o tipo numérico se estiverem em outro formato. (Use replace() e astype())
print(df.columns)
df_valores_nulos = df.isnull()
print(df_valores_nulos.sum())
print(df.duplicated().sum())

colunas_convertidas = ['All Time Rank', 'Track Score', 'Spotify Streams','Spotify Playlist Count', 'Spotify Playlist Reach','Spotify Popularity', 'YouTube Views', 'YouTube Likes', 'TikTok Posts','TikTok Likes', 'TikTok Views', 'YouTube Playlist Reach','Apple Music Playlist Count', 'AirPlay Spins', 'SiriusXM Spins','Deezer Playlist Count', 'Deezer Playlist Reach','Amazon Playlist Count', 'Pandora Streams', 'Pandora Track Stations','Soundcloud Streams', 'Shazam Counts', 'TIDAL Popularity','Explicit Track']

for coluna in colunas_convertidas:
     if df[coluna].dtype == "object":
           df[coluna] = pd.to_numeric(df[coluna].str.replace(",", "."), errors="coerce")
        
print(df.dtypes)

# 3° passo: Corrija a coluna 'Release Date' para o formato datetime

df["Release Date"] = pd.to_datetime(df["Release Date"], format="mixed")
print(df["Release Date"])

# # 4° passo: Crie uma nova coluna chamada 'Streaming Popularity', que seja a média da popularidade nas plataformas 'Spotify Popularity', 'YouTube Views', 'TikTok Likes', e 'Shazam Counts'. (lembrem-se que só é possível calcular médias e fazer operações matemáticas com tipos númericos)

df[['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts']] = df[['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts']].apply(pd.to_numeric, errors='coerce')
df["Streaming Popularity"] = df[['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts']].mean(axis=1)
print(df["Streaming Popularity"])

# 5° passo: Crie uma coluna 'Total Streams', somando os valores de 'Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', e 'Soundcloud Streams

df["Total Streams"] = df[["Spotify Streams", "YouTube Views", "TikTok Views", "Pandora Streams", "Soundcloud Streams"]].sum(axis=1)
print(df["Total Streams"])

# 6° passo: Filtre apenas as faixas onde a popularidade do Spotify ('Spotify Popularity') é maior que 80 e que tenham mais de 1 milhão de streams totais ('Total Streams').

filtered_df = df[(df["Spotify Popularity"] > 80 & (df["Total Streams"] > 1000000))]
print(filtered_df.head())

# 7° passo: Salve o DataFrame resultante em um novo arquivo JSON chamado 'faixas_filtradas.json'
# 8° passo: Garanta que o arquivo foi salvo corretamente

filtered_df.to_json("./faixas_filtradas.json", index=False)
df = pd.read_json("./faixas_filtradas.json")
print(df.head())



