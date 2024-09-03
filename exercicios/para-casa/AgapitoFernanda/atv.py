import pandas as pd

df = pd.read_csv('../../../material/mais_ouvidas_2024.csv')
 
#print(df.head())
#print(df.columns)
#print(df.dtypes)

#- Corrija a coluna 'Spotify Streams' para que tenha apenas valores numéricos.
#df ['Spotify Streams'] = df['Spotify Streams'].str.replace(',', '').fillna('0').astype(int)
#print(df['Spotify Streams'])

#- Corrija a coluna 'Release Date' para o formato datetime.
print(df.dtypes['Release Date'])
df['Release Date'] = pd.to_datetime(df['Release Date'], format='mixed')
print(df.dtypes['Release Date'])

#- Converta as colunas 'YouTube Views', 'TikTok Views', 'Pandora Streams', 'Spotify Streams', 'TikTok Likes', 'Shazam Counts', 'Soundcloud Streams' para o tipo inteiro.
print(df.dtypes)

col_convert =  ['YouTube Views', 'TikTok Views', 'Pandora Streams','TikTok Likes', 'Shazam Counts', 'Soundcloud Streams', 'Spotify Streams']

#original_dtypes = df[col_convert].dtypes
#print(original_dtypes)
#print()

for col in col_convert:
    df[col] = df[col].str.replace(',', '')  # Remove as vírgulas
    df[col] = df[col].fillna('0')           # Substitui NaN por '0'
    df[col] = df[col].astype(float)           # Converte para int
    
tipos = df[col_convert].dtypes
#print(tipos)

#- Crie uma nova coluna chamada 'Streaming Popularity', que seja a média da popularidade nas plataformas 'Spotify Popularity', 'YouTube Views', 'TikTok Likes', e 'Shazam Counts'. (lembrem-se que só é possível calcular médias e fazer operações matemáticas com tipos númericos)

#df['Streaming Popularity'] = (df['Spotify Popularity'] + df['YouTube Views'] + df['TikTok Likes'] + df['Shazam Counts']) /4
df['Streaming Popularity'] = df[['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts']].mean(axis=1)
#print(df['Streaming Popularity'])

#- Crie uma coluna 'Total Streams', somando os valores de 'Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', e 'Soundcloud Streams'.

df['Total Streams'] = df[['Spotify Streams','YouTube Views','TikTok Views','Pandora Streams','Soundcloud Streams']].sum(axis=1)
print(df['Total Streams'])

#- Filtre apenas as faixas onde a popularidade do Spotify ('Spotify Popularity') é maior que 80 e que tenham mais de 1 milhão de streams totais ('Total Streams').

filtered_df = df[(df['Spotify Popularity'] > 80) & (df['Total Streams'] > 1_000_000)]
#print (filtered_df)

#- Salve o DataFrame resultante em um novo arquivo JSON chamado 'faixas_filtradas.json'.
filtered_df.to_json('./faixas_filtradas2.json', index=False)



