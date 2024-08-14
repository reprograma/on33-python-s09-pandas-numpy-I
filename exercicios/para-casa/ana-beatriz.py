import pandas as pd

df = pd.read_csv("../../material/mais_ouvidas_2024.csv")

#print(df.head())#Traz as 10 primeiras linhas do arquivo
#print(df.columns)
#df_valores_nulos = df.isnull() #identifica valores nulos
#print(df_valores_nulos.sum())
#print(df.duplicated())

df.fillna(0, inplace=True)
df_valores_nulos_apos = df.isnull()
#print(df_valores_nulos_apos.sum())

#print(df.dtypes)

nome_colunas = df.columns

for coluna in nome_colunas:
    if df[coluna].dtype == "object":  
        df[coluna] = df[coluna].str.replace(",", "")
        df[coluna] = pd.to_numeric(df[coluna], errors='ignore')


#print(df.dtypes)

df['Release Date'] = pd.to_datetime(df['Release Date'])
#print(df.dtypes)
#print(df.head())

df['Streaming Popularity'] = (df['Spotify Popularity'] + df['YouTube Views'] + df['TikTok Likes'] + df['Shazam Counts']) / 4
#print(df['Streaming Popularity'])
#print(df.columns)

df['Total Streams'] = (df['Spotify Streams'] + df['YouTube Views'] + df['TikTok Views'] + df['Pandora Streams'] + df['Soundcloud Streams'])
#print(df['Total Streams'])
#print(df.columns)

filtered_df = df[(df['Spotify Popularity'] > 80) & (df['Total Streams'] > 1000000 )]
#print(filtered_df.head())
#print(filtered_df['Spotify Popularity'].head())

filtered_df.to_json('faixas_filtradas.json')
