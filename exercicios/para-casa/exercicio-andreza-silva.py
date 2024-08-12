import pandas as pd

'''['Track', 'Album Name', 'Artist', 'Release Date', 'ISRC',
       'All Time Rank', 'Track Score', 'Spotify Streams',
       'Spotify Playlist Count', 'Spotify Playlist Reach',
       'Spotify Popularity', 'YouTube Views', 'YouTube Likes', 'TikTok Posts',
       'TikTok Likes', 'TikTok Views', 'YouTube Playlist Reach',
       'Apple Music Playlist Count', 'AirPlay Spins', 'SiriusXM Spins',
       'Deezer Playlist Count', 'Deezer Playlist Reach',
       'Amazon Playlist Count', 'Pandora Streams', 'Pandora Track Stations',
       'Soundcloud Streams', 'Shazam Counts', 'TIDAL Popularity',
       'Explicit Track'],'''


df = pd.read_csv("C:/Users/andre/OneDrive/Área de Trabalho/REPROGRAMA/SEMANA 11/on33-python-s09-pandas-numpy-I/material/mais_ouvidas_2024.csv")

#print(df)

#print(df.head())
#print(df.columns)

#print(df.dtypes)

df['All Time Rank'] = df['All Time Rank'].replace({',': ''}, regex=True).astype(int) #Converte a coluna 'Spotify Streams' para tipo numérico, removendo separadores de milhar e convertendo com astype
#print(df)
df['Spotify Streams'] = df['Spotify Streams'].replace({',': ''}, regex=True).astype(float)
df['Spotify Playlist Count'] = df['Spotify Playlist Count'].replace({',': ''}, regex=True).astype(float)
df['Spotify Playlist Reach'] = df['Spotify Playlist Reach'].replace({',': ''}, regex=True).astype(float)
df['YouTube Views'] = df['YouTube Views'].replace({',': ''}, regex=True).astype(float)
df['YouTube Likes'] = df['YouTube Likes'].replace({',': ''}, regex=True).astype(float)
df['TikTok Posts'] = df['TikTok Posts'].replace({',': ''}, regex=True).astype(float)
df['TikTok Likes'] = df['TikTok Likes'].replace({',': ''}, regex=True).astype(float)
df['TikTok Views'] = df['TikTok Views'].replace({',': ''}, regex=True).astype(float)
df['YouTube Playlist Reach'] = df['YouTube Playlist Reach'].replace({',': ''}, regex=True).astype(float)
df['AirPlay Spins'] = df['AirPlay Spins'].replace({',': ''}, regex=True).astype(float)
df['SiriusXM Spins'] = df['SiriusXM Spins'].replace({',': ''}, regex=True).astype(float)
df['Deezer Playlist Reach'] = df['Deezer Playlist Reach'].replace({',': ''}, regex=True).astype(float)
df['Pandora Streams'] = df['Pandora Streams'].replace({',': ''}, regex=True).astype(float)
df['Pandora Track Stations'] = df['Pandora Track Stations'].replace({',': ''}, regex=True).astype(float)
df['Soundcloud Streams'] = df['Soundcloud Streams'].replace({',': ''}, regex=True).astype(float)
df['Shazam Counts'] = df['Shazam Counts'].replace({',': ''}, regex=True).astype(float)
df['Release Date'] = pd.to_datetime(df['Release Date'], format="mixed")
print(df.dtypes)



df["Streaming Popularity"] = (df["Spotify Popularity"] + df["YouTube Views"] + df["TikTok Likes"] + df["Shazam Counts"]) / 4

print(df["Streaming Popularity"])

df["Total Streams"] = df["Spotify Streams"] + df["YouTube Views"] + df["TikTok Views"] + df["Pandora Streams"] + df["Soundcloud Streams"]

print(df["Total Streams"])

print(df)

filtered_df = df [(df["Spotify Popularity"] > 80) & (df["Total Streams"] > 1000000)]
print(filtered_df)

filtered_df.to_json("./filtered_list.json", index=False) 