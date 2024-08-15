import pandas as pd

['Track', 'Album Name', 'Artist', 'Release Date', 'ISRC','All Time Rank', 'Track Score', 'Spotify Streams','Spotify Playlist Count', 'Spotify Playlist Reach',
'Spotify Popularity', 'YouTube Views', 'YouTube Likes', 'TikTok Posts','TikTok Likes', 'TikTok Views', 'YouTube Playlist Reach','Apple Music Playlist Count', 
'AirPlay Spins', 'SiriusXM Spins','Deezer Playlist Count', 'Deezer Playlist Reach','Amazon Playlist Count', 'Pandora Streams', 'Pandora Track Stations',
'Soundcloud Streams', 'Shazam Counts', 'TIDAL Popularity', 'Explicit Track'] 

# Carregar o arquivo CSV em um DataFrame do Pandas
df = pd.read_csv(r"C:/Users/sanel/OneDrive/Área de Trabalho/git-on33/on33-python-s011-pandas-numpy/exercicios/para-casa/mais_ouvidas_2024.csv")

#print(df.head())
#print(df.columns)
#print(df.isnull())
#df_valores_nulos = df.isnull()
#print(df_valores_nulos.sum())
#print(df.dtypes)

colunas_conversao = ['Spotify Streams', 'Spotify Playlist Count', 'Spotify Playlist Reach','YouTube Views', 'YouTube Likes','TikTok Posts', 'TikTok Likes', 'TikTok Views' ,'YouTube Playlist Reach','AirPlay Spins', 'SiriusXM Spins','Deezer Playlist Reach','Pandora Streams','Soundcloud Streams','Shazam Counts']
df[colunas_conversao] = df[colunas_conversao].replace({',':''}, regex=True).astype(float)
#print(df["Release Date"])
#df["Release Date"] = pd.to_datetime(df["Release Date"], format="mixed")
#print(df.dtypes)
#print(df["Release Date"])

#df["Streaming Popularity"] = df[["Spotify Popularity","YouTube Views","TikTok Likes", "Shazam Counts"]].mean(axis=1)

#print(df["Streaming Popularity"])

df["Total Streams"] = df['Spotify Streams'] + df['YouTube Views'] + df['TikTok Views'] + df['Pandora Streams'] + df['Soundcloud Streams']

#print(df["Total Streams"])

filtered_df = df[(df["Spotify Popularity"]> 80_00) & (df["Total Streams"] > 1_000_000)]

print(filtered_df.head())

filtered_df.to_json("./exercicios\para-casa/faixasfiltradas.json", index=False)


