import pandas as pd

#['Track', 'Album Name', 'Artist', 'Release Date', 'ISRC','All Time Rank', 'Track Score', 'Spotify Streams','Spotify Playlist Count', 'Spotify Playlist Reach','Spotify Popularity', 'YouTube Views', 'YouTube Likes', 'TikTok Posts','TikTok Likes', 'TikTok Views', 'YouTube Playlist Reach','Apple Music Playlist Count', 'AirPlay Spins', 'SiriusXM Spins','Deezer Playlist Count', 'Deezer Playlist Reach','Amazon Playlist Count', 'Pandora Streams', 'Pandora Track Stations','Soundcloud Streams', 'Shazam Counts', 'TIDAL Popularity','Explicit Track']

df_musicas = pd.read_csv ('../../material/mais_ouvidas_2024.csv')

print(df_musicas.head()) # mostra a "cabeça" do dataframe
print(df_musicas.columns) # mostra todas as colunas 

# 2 - Indentifique as colunas que contêm números, como 'Spotify Streams', 'YouTube Views', etc., e converta essas colunas para o tipo numérico se estiverem em outro formato. (Use replace() e astype())

colunas = ['Track', 'Album Name', 'Artist', 'Release Date', 'ISRC','All Time Rank', 'Track Score', 'Spotify Streams','Spotify Playlist Count', 'Spotify Playlist Reach','Spotify Popularity', 'YouTube Views', 'YouTube Likes', 'TikTok Posts','TikTok Likes', 'TikTok Views', 'YouTube Playlist Reach','Apple Music Playlist Count', 'AirPlay Spins', 'SiriusXM Spins','Deezer Playlist Count', 'Deezer Playlist Reach','Amazon Playlist Count', 'Pandora Streams', 'Pandora Track Stations','Soundcloud Streams', 'Shazam Counts', 'TIDAL Popularity','Explicit Track']
nulos = df_musicas.isnull() # retorna os valores nulos
print(nulos.sum()) # soma esses valores nulos
print(df_musicas.dtypes)

for col in colunas: 
    if df_musicas[col].dtypes == 'object':
        df_musicas[col] = df_musicas[col].str.replace(',' , '').astype(float, errors='ignore')

# 3 - Corrija a coluna 'Release Date' para o formato datetime.

df_musicas['Release Date'] = pd.to_datetime(df_musicas['Release Date'], format= 'mixed')
print(df_musicas.dtypes)

# 4 - Crie uma nova coluna chamada 'Streaming Popularity', que seja a média da popularidade nas plataformas 'Spotify Popularity', 'YouTube Views', 'TikTok Likes', e 'Shazam Counts'. (lembrem-se que só é possível calcular médias e fazer operações matemáticas com tipos númericos)

df_musicas ['Streaming Popularity'] = df_musicas[['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts']].median(axis=1)
print(df_musicas['Streaming Popularity'])

# 5 - Crie uma coluna 'Total Streams', somando os valores de 'Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', e 'Soundcloud Streams'.

df_musicas ['Total Streams'] = df_musicas[['Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams','Soundcloud Streams']].sum(axis=1)
print(df_musicas['Total Streams'])

# 6 - Filtre apenas as faixas onde a popularidade do Spotify ('Spotify Popularity') é maior que 80 e que tenham mais de 1 milhão de streams totais ('Total Streams').

filtrar = df_musicas[(df_musicas['Spotify Popularity'] > 80) & (df_musicas['Total Streams'] > 1_000_000)]
print(filtrar.head())

# 7 - Salve o DataFrame resultante em um novo arquivo JSON chamado 'faixas_filtradas.json'. - Garanta que o arquivo foi salvo corretamente

filtrar.to_json('./faixas_filtradas.json', index= False)