import pandas as pd

df = pd.read_csv("./mais_ouvidas_2024.csv")

#Colunas ['Track', 'Album Name', 'Artist', 'Release Date', 'ISRC','All Time Rank', 'Track Score', 'Spotify Streams','Spotify Playlist Count', 'Spotify Playlist Reach',
#      'Spotify Popularity', 'YouTube Views', 'YouTube Likes', 'TikTok Posts','TikTok Likes', 'TikTok Views', 'YouTube Playlist Reach',
#       'Apple Music Playlist Count', 'AirPlay Spins', 'SiriusXM Spins','Deezer Playlist Count', 'Deezer Playlist Reach',
#      'Amazon Playlist Count', 'Pandora Streams', 'Pandora Track Stations','Soundcloud Streams', 'Shazam Counts', 'TIDAL Popularity',   'Explicit Track']

#print(df.head(n=10))

#Converter os dados das colunas para numéricos

Columns = ['Track', 'Album Name', 'Artist', 'ISRC','All Time Rank', 'Track Score', 'Spotify Streams','Spotify Playlist Count', 'Spotify Playlist Reach','Spotify Popularity', 
'YouTube Views', 'YouTube Likes', 'TikTok Posts','TikTok Likes', 'TikTok Views', 'YouTube Playlist Reach','Apple Music Playlist Count', 'AirPlay Spins', 'SiriusXM Spins',
'Deezer Playlist Count', 'Deezer Playlist Reach','Amazon Playlist Count','Pandora Streams', 'Pandora Track Stations','Soundcloud Streams', 'Shazam Counts', 'TIDAL Popularity','Explicit Track']

for col in Columns:
    if df[col].dtype == 'object':
        df[col] = df[col].str.replace(',', '', regex=False)
    df[col] = pd.to_numeric(df[col], errors='coerce')

#Substitui por zero as linhas que tem o NaN
df = df.fillna(0)

#Corrija a coluna 'Release Date' para o formato datetime.
df["Release Date"] = pd.to_datetime(df["Release Date"], errors='coerce', format="mixed")

#print(df.dtypes)


#- Crie uma nova coluna chamada 'Streaming Popularity', que seja a média da popularidade nas plataformas 'Spotify Popularity', 'YouTube Views', 'TikTok Likes', e 'Shazam Counts'.
df["Streaming_Popularity"] = df[['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts']].mean(axis=1)
#print(df)

#Crie uma coluna 'Total Streams', somando os valores de 'Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', e 'Soundcloud Streams'.
df["Total_Streams"] = df[['Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', 'Soundcloud Streams']].sum(axis=1)
#print(df)

#- Filtre apenas as faixas onde a popularidade do Spotify ('Spotify Popularity') é maior que 80 e que tenham mais de 1 milhão de streams totais ('Total Streams').
filtered_df = df[(df["Spotify Popularity"] > 80) & (df["Total_Streams"] > 1000000)]
print(filtered_df.head())

#Salve o DataFrame resultante em um novo arquivo JSON chamado 'faixas_filtradas.json'.
filtered_df.to_csv("./faixas_filtradas.json", index=False)

#Slvando em CSV
filtered_df.to_csv("./faixas_filtradas.csv", index=False)
