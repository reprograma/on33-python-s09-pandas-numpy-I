import pandas as pd  

df = pd.read_csv("Anália/mais_ouvidas_2024.csv")

print(df.head())
print(df.dtypes)

convertendo_colunas = ['Spotify Streams', 'Spotify Playlist Count', 'Spotify Playlist Reach','YouTube Views', 'YouTube Likes', 
'TikTok Posts', 'TikTok Likes', 'TikTok Views','YouTube Playlist Reach', 'AirPlay Spins', 
'SiriusXM Spins', 'Deezer Playlist Reach', 'Pandora Streams', 'Pandora Track Stations', 'Soundcloud Streams', 'Shazam Counts']
df[convertendo_colunas] = df[convertendo_colunas].replace({',': ''}, regex=True).astype(float)

print(df.dtypes)

df['Release Date'] = pd.to_datetime(df['Release Date'])

df['Streaming Popularity'] = df[['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts']].mean(axis=1)
df['Total Streams'] = df['Spotify Streams'] + df['YouTube Views'] + df['TikTok Views'] + df['Pandora Streams'] + df['Soundcloud Streams']

filtro = (df['Spotify Popularity'] > 80) & (df['Total Streams'] > 1_000_000)
faixas_filtradas = df[filtro]

print(faixas_filtradas)

faixas_filtradas.to_json('faixas_filtradas.json')

