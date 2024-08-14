# ------------------------------------------------PASSO 1------------------------------------------------
# Use o arquivo `mais_ouvidas_2024.csv` para análise. Lembre-se de garantir que o carregamento foi feito com sucesso.
#--------------------------------------------------------------------------------------------------------
 
import pandas as pd

df_mais_ouvidas = pd.read_csv('../../material/mais_ouvidas_2024.csv')

print(df_mais_ouvidas.head())

# ------------------------------------------------PASSO 2------------------------------------------------
# Identifique as colunas que contêm números, como 'Spotify Streams', 'YouTube Views', etc., e converta essas colunas para o tipo numérico se estiverem em outro formato. (Use replace() e astype())
#--------------------------------------------------------------------------------------------------------

# print(df_mais_ouvidas.columns) # lista as colunas da tabela
# print(df_mais_ouvidas.dtypes) # retorna os tipos de cada coluna da tabela
print(df_mais_ouvidas.info()) # traz informações de colunas (qtde de linhas - nulos - tipos)
print(df_mais_ouvidas.isnull().sum()) #traz a qtde de valores nulos em cada coluna da tabela
# colunas com tipagem incorreta: 'Spotify Streams', 'Spotify Playlist Count', 'Spotify Playlist Reach', 'YouTube Views', 'YouTube Likes', 'TikTok Posts','TikTok Likes', 'TikTok Views', 'YouTube Playlist Reach','AirPlay Spins', 'SiriusXM Spins', 'Deezer Playlist Reach', 'Pandora Streams', 'Pandora Track Stations', 'Soundcloud Streams', 'Shazam Counts'],

colunas_tipagem = ['Spotify Streams', 'Spotify Playlist Count', 'Spotify Playlist Reach', 'YouTube Views', 'YouTube Likes', 'TikTok Posts','TikTok Likes', 'TikTok Views', 'YouTube Playlist Reach','AirPlay Spins', 'SiriusXM Spins', 'Deezer Playlist Reach', 'Pandora Streams', 'Pandora Track Stations', 'Soundcloud Streams', 'Shazam Counts']
df_mais_ouvidas[colunas_tipagem] = df_mais_ouvidas[colunas_tipagem].apply(lambda x: x.str.replace(',', '').astype('float'))
print(df_mais_ouvidas[colunas_tipagem])

# ------------------------------------------------PASSO 3------------------------------------------------
# Corrija a coluna 'Release Date' para o formato datetime.
#--------------------------------------------------------------------------------------------------------

# print(df_mais_ouvidas.dtypes)
df_mais_ouvidas['Release Date'] = pd.to_datetime(df_mais_ouvidas['Release Date'], format='mixed')
print(df_mais_ouvidas.dtypes)
print (df_mais_ouvidas['Release Date'])

# ------------------------------------------------PASSO 4------------------------------------------------
# Crie uma nova coluna chamada 'Streaming Popularity', que seja a média da popularidade nas plataformas 'Spotify Popularity', 'YouTube Views', 'TikTok Likes', e 'Shazam Counts'. (lembrem-se que só é possível calcular médias e fazer operações matemáticas com tipos númericos)
#--------------------------------------------------------------------------------------------------------

colunas_popularidade = ['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts']
df_mais_ouvidas['Streaming Popularity'] = df_mais_ouvidas[colunas_popularidade].median(axis=1)
print(df_mais_ouvidas['Streaming Popularity'])

# ------------------------------------------------PASSO 5------------------------------------------------
# Crie uma coluna 'Total Streams', somando os valores de 'Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', e 'Soundcloud Streams'.
#--------------------------------------------------------------------------------------------------------

colunas_total = ['Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', 'Soundcloud Streams']
df_mais_ouvidas['Total Streams'] = df_mais_ouvidas[colunas_total].sum(axis=1)
print(df_mais_ouvidas['Total Streams'])
print(df_mais_ouvidas.isnull().sum())
# ------------------------------------------------PASSO 6------------------------------------------------
# Filtre apenas as faixas onde a popularidade do Spotify ('Spotify Popularity') é maior que 80 e que tenham mais de 1 milhão de streams totais ('Total Streams').
#--------------------------------------------------------------------------------------------------------

filter_popularity = df_mais_ouvidas[(df_mais_ouvidas['Spotify Popularity'] > 80) & (df_mais_ouvidas['Total Streams'] > 1_000_000)]
print(filter_popularity)

# ------------------------------------------------PASSO 7------------------------------------------------
# Salve o DataFrame resultante em um novo arquivo JSON chamado 'faixas_filtradas.json'.
# Garanta que o arquivo foi salvo corretamente
#--------------------------------------------------------------------------------------------------------

filter_popularity.to_json('./filtered_mais_ouvidas.json', index=False)
