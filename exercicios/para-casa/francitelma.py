#- Use o arquivo `mais_ouvidas_2024.csv` para análise. Lembre-se de garantir que o carregamento foi feito com sucesso.
import pandas as pd

df = pd.read_csv("../../material/mais_ouvidas_2024.csv")
print (df.head())

#- Indentifique as colunas que contêm números, como 'Spotify Streams', 'YouTube Views', etc., e converta essas colunas para o tipo numérico se estiverem em outro formato. (Use replace() e astype())

#print (df.columns) 
convertendo_colunas = ['Spotify Streams', 'Spotify Playlist Count', 'Spotify Playlist Reach','YouTube Views', 'YouTube Likes', 
'TikTok Posts', 'TikTok Likes', 'TikTok Views','YouTube Playlist Reach', 'AirPlay Spins', 
'SiriusXM Spins', 'Deezer Playlist Reach', 'Pandora Streams', 'Pandora Track Stations', 'Soundcloud Streams', 'Shazam Counts']
df[convertendo_colunas] = df[convertendo_colunas].replace({',': ''}, regex=True).astype(float)
print(df.dtypes)

# - Corrija a coluna 'Release Date' para o formato datetime.

df["Release Date"] = pd.to_datetime(df["Release Date"], format="mixed")
print(df["Release Date"])

# - Crie uma nova coluna chamada 'Streaming Popularity', que seja a média da popularidade nas plataformas 'Spotify Popularity', 'YouTube Views', 'TikTok Likes', e 'Shazam Counts'. 
# (lembrem-se que só é possível calcular médias e fazer operações matemáticas com tipos númericos)

df['Streaming Popularity'] = (df['Spotify Popularity'] + df['YouTube Views'] + df['TikTok Likes'] + df['Shazam Counts']) / 4
print(df["Streaming Popularity"].dtype)
print(df.head())
#print(df.columns)

# - Crie uma coluna 'Total Streams', somando os valores de 'Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', e 'Soundcloud Streams'.
df['Total Streams'] = (df['Spotify Streams'] + df['YouTube Views'] + df['TikTok Views'] + df['Pandora Streams'] + df['Soundcloud Streams'])
print(df.head())
#print(df.columns)

# - Filtre apenas as faixas onde a popularidade do Spotify ('Spotify Popularity') é maior que 80 e que tenham mais de 1 milhão de streams totais ('Total Streams').

filtradas = df[(df['Spotify Popularity'] > 80) & (df['Total Streams'] > 1_000_000)]
print(filtradas.head())

# - Salve o DataFrame resultante em um novo arquivo JSON chamado 'faixas_filtradas.json'.
filtradas.to_json("./faixas_filtradas.json", index= False)

# - Garanta que o arquivo foi salvo corretamente
df = pd.read_json("../para_casa/mais_ouvidas_2024.json")
print (df.head())
