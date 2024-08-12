#Exercicio Semana 11 [Pandas]

import pandas as pd

#Use o arquivo `mais_ouvidas_2024.csv` para análise. Lembre-se de garantir que o carregamento foi feito com sucesso.

df = pd.read_csv("../../material/mais_ouvidas_2024.csv")
#print(df.head())
#print(df.columns)

#Indentifique as colunas que contêm números, como 'Spotify Streams', 'YouTube Views', etc., e converta essas colunas para o tipo numérico se estiverem em outro formato. (Use replace() e astype())

print(df.dtypes)#Verificando os tipos de dado

#Corrigindo os tipos de dados  - errors='coerce' para corrir erros de '.' e ',' na separaçao entre outros erros de digitaçao

df['All Time Rank'] = pd.to_numeric(df['All Time Rank'], errors='coerce')
df['Spotify Streams'] = pd.to_numeric(df['Spotify Streams'], errors='coerce')
df['Spotify Playlist Count'] = pd.to_numeric(df['Spotify Playlist Count'], errors='coerce')
df['Spotify Playlist Reach'] = pd.to_numeric(df['Spotify Playlist Reach'], errors='coerce')
df['YouTube Views'] = pd.to_numeric(df['YouTube Views'], errors='coerce')
df['YouTube Likes'] = pd.to_numeric(df['YouTube Likes'], errors='coerce')
df['TikTok Posts'] = pd.to_numeric(df['TikTok Posts'], errors='coerce')
df['TikTok Likes'] = pd.to_numeric(df['TikTok Likes'], errors='coerce')
df['TikTok Views'] = pd.to_numeric(df['TikTok Views'], errors='coerce')
df['YouTube Playlist Reach'] = pd.to_numeric(df['YouTube Playlist Reach'], errors='coerce')
df['AirPlay Spins'] = pd.to_numeric(df['AirPlay Spins'], errors='coerce')
df['SiriusXM Spins'] = pd.to_numeric(df['SiriusXM Spins'], errors='coerce')
df['Deezer Playlist Reach'] = pd.to_numeric(df['Deezer Playlist Reach'], errors='coerce')
df['Pandora Streams'] = pd.to_numeric(df['Pandora Streams'], errors='coerce')
df['Soundcloud Streams'] = pd.to_numeric(df['Soundcloud Streams'], errors='coerce')
df['Shazam Counts'] = pd.to_numeric(df['Shazam Counts'], errors='coerce')

#Corrija a coluna 'Release Date' para o formato datetime.

df['Release Date'] = pd.to_datetime(df['Release Date'], errors='coerce')

#print(df.dtypes)#Conferindo a mudança de tipo de dado

#Crie uma nova coluna chamada 'Streaming Popularity', que seja a média da popularidade nas plataformas 'Spotify Popularity', 'YouTube Views', 'TikTok Likes', e 'Shazam Counts'. (lembrem-se que só é possível calcular médias e fazer operações matemáticas com tipos númericos)

df['Streaming Popularity'] = (df['Spotify Popularity'] + df['YouTube Views'] + df['TikTok Likes'] + df['Shazam Counts']) / 4
#print(df.head())
#print(df.columns)

#Crie uma coluna 'Total Streams', somando os valores de 'Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', e 'Soundcloud Streams'.

df['Total Streams'] = (df['Spotify Streams'] + df['YouTube Views'] + df['TikTok Views'] + df['Pandora Streams'] + df['Soundcloud Streams'])
#print(df.head())
#print(df.columns)

#Filtre apenas as faixas onde a popularidade do Spotify ('Spotify Popularity') é maior que 80 e que tenham mais de 1 milhão de streams totais ('Total Streams').

filtered_df = df[(df['Spotify Popularity'] > 80) & (df['Total Streams'] > 1_000_000)]
print(filtered_df)

#Salve o DataFrame resultante em um novo arquivo JSON chamado 'faixas_filtradas.json'.

df.to_json('./faixas_filtradas.json', orient='records', lines=True)
