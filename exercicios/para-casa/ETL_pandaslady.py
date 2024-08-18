#- Use o arquivo `mais_ouvidas_2024.csv` para análise. Lembre-se de garantir que o carregamento foi feito com sucesso.
import pandas as pd
# Carregar o documento CSV
df = pd.read_csv(r"C:\Users\lady_\OneDrive\Documentos\Reprograma-2024\reprograma\on33-python-s11-pandas-numpy-I\exercicios\para-casa\mais_ouvidas_2024.csv") 

<<<<<<< HEAD
df.head()
# print(df.dtypes) 
=======
#print(df.head())

>>>>>>> 51289e8 (salvando sugestão sugeridas pela professoura)

# - Indentifique as colunas que contêm números, como 'Spotify Streams', 'YouTube Views', etc., e converta essas colunas para o tipo numérico se estiverem em outro formato. 
# (Use replace() e astype())

<<<<<<< HEAD
# print(df.head()) #verificar as primeiras linhas para garantir que o carregamento foi feito 
# print(df.dtypes)
for coluna in df.columns:
    if df[coluna].dtype == 'object':
        df[coluna] = pd.to_numeric(df[coluna].replace({',': '', '-': ''}, regex=True), errors='coerce')
print(df.dtypes)

# - Corrija a coluna 'Release Date' para o formato datetime.
# Converter a coluna 'Release Date' para o formato datetime
df['Release Date'] = pd.to_datetime(df['Release Date'], format='mixed')
print(df.dtypes)
# - Crie uma nova coluna chamada 'Streaming Popularity', que seja a média da popularidade nas plataformas
# 'Spotify Popularity', 'YouTube Views', 'TikTok Likes', e 'Shazam Counts'. 
# (lembrem-se que só é possível calcular médias e fazer operações matemáticas com tipos númericos)
# Criar a coluna 'Streaming Popularity'
df['Streaming Popularity'] = df[['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts']].mean(axis=1)
# a coluna 'Streaming Popularity' mostra a média das quatro colunas de popularidade para cada linha.
print(df[['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts', 'Streaming Popularity']].head())

#- Crie uma coluna 'Total Streams', somando os valores de 'Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', e 'Soundcloud Streams'.
#Some as colunas relacionadas às visualizações e streams

# Criar a coluna 'Total Streams'
df['Total Streams'] = df[['Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', 'Soundcloud Streams']].sum(axis=1)
print(df.head())
#- Filtre apenas as faixas onde a popularidade do Spotify ('Spotify Popularity') é maior que 80 e que tenham mais de 1 milhão de streams totais ('Total Streams')

# Filtrar as faixas 
df_filtrado = df[(df['Spotify Popularity'] > 80) & (df['Total Streams'] > 1_000_000)]
print(df_filtrado.head())
#- Salve o DataFrame resultante em um novo arquivo JSON chamado 'faixas_filtradas.json'.
# Salvar o DataFrame filtrado em um novo arquivo JSON
df_filtrado.to_json('faixas_filtradas.json', orient='records', lines=True)

# Carregar e verificar o arquivo JSON salvo
df_verificado = pd.read_json('faixas_filtradas.json', orient='records', lines=True)
print(df_verificado.head())

=======


### 1 -print(df.columns) # vê todas minhas colunas 
# print(df.dtypes) # tipos de colunas, parte mas trabalhosa 


#jeito certo de fazer a conversão do tipo da coluna sem mudar toda ela.
to_parse = [
    "All Time Rank",
    "Spotify Streams", 
    "Spotify Playlist Count",
    "Spotify Playlist Reach",
    "YouTube Views",
    "YouTube Likes",
    "TikTok Posts",
    "TikTok Likes",
    "TikTok Views",
    "YouTube Playlist Reach",
    "Deezer Playlist Reach",
    "Pandora Streams",
    "Pandora Track Stations",
    "Soundcloud Streams",
    "Shazam Counts",
]
for column in to_parse:
    df[column] = df[column].str.replace(",", "").astype(float) # spor que precisamos do número sem a virgula porque assim astype vai identificar como valor possível ser convertido
print(df.dtypes)    




#jeito errado pois converte toodos os objetos para float 
# print(df.head()) #verificar as primeiras linhas para garantir que o carregamento foi feito 
# print(df.dtypes)
# for coluna in df.columns:
#     if df[coluna].dtype == 'object':
#         df[coluna] = pd.to_numeric(df[coluna].replace({',': '', '-': ''}, regex=True), errors='coerce')
# print(df.dtypes)




# # - Corrija a coluna 'Release Date' para o formato datetime.
df['Release Date'] = pd.to_datetime(df['Release Date'], format='%m/%d/%Y') #verificar documentação do pandas - esse e maos rapido na hora de processa porque não precisa procurar data com formato diferente
print(df.dtypes)
# df['Release Date'] = pd.to_datetime(df['Release Date'], format='mixed') # misturado .format='mixed' e utilizado para que o datetime consiga indetificar diversos formato diferente de data numa mesma coluna



# # - Crie uma nova coluna chamada 'Streaming Popularity', que seja a média da popularidade nas plataformas
# # 'Spotify Popularity', 'YouTube Views', 'TikTok Likes', e 'Shazam Counts'. 
# # (lembrem-se que só é possível calcular médias e fazer operações matemáticas com tipos númericos)

df['Streaming Popularity'] = df[['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts']].mean(axis=1) #o mean fumciona para série ,dataframe, coluna que no caso sao dataframe de uma dimensão só 
# # a coluna 'Streaming Popularity' mostra a média das quatro colunas de popularidade para cada linha.
print(df[['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts', 'Streaming Popularity']].head())



# #- Crie uma coluna 'Total Streams', somando os valores de 'Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', e 'Soundcloud Streams'.
# #Some as colunas relacionadas às visualizações e streams

# Criar a coluna 'Total Streams'
df['Total Streams'] = df[['Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', 'Soundcloud Streams']].sum(axis=1)
print(df['Total Streams'])



# #- Filtre apenas as faixas onde a popularidade do Spotify ('Spotify Popularity') é maior que 80 e que tenham mais de 1 milhão de streams totais ('Total Streams')
# # Filtrar as faixas 
df_filtrado = df[(df['Spotify Popularity'] > 80) & (df['Total Streams'] > 1_000_000)]
print(df['Spotify Popularity'])

# #- Salve o DataFrame resultante em um novo arquivo JSON chamado 'faixas_filtradas.json'.
# # Salvar o DataFrame filtrado em um novo arquivo JSON#
df_filtrado.to_json('faixas_filtradas.json', orient='records', lines=True)
#Quando você usa orient='records', cada linha do DataFrame é representada como um objeto JSON separado, com as colunas do DataFrame como chaves e os valores da linha como valores do objeto.
#Com lines=True, cada objeto JSON correspondente a uma linha do DataFrame será gravado em uma linha individual no arqui


# # Carregar e verificar o arquivo JSON salvo
df_verificado = pd.read_json('faixas_filtradas.json', orient='records', lines=True)
print(df_verificado.head())

####################################
# for valor in df.columns:
#     print(df[valor].head(2))  # para vê todas as colunas e trazer o tipo , com 2 linha para cada 
#####################################

>>>>>>> 51289e8 (salvando sugestão sugeridas pela professoura)
