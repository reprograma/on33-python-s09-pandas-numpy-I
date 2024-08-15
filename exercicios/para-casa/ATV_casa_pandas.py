import pandas as pd

#ler o arquivo csv
df = pd.read_csv("material/mais_ouvidas_2024.csv") 

#Fazer replace das colunas que tem strings para números.
for column in df.columns:
    if df[column].dtype == "object":
        df[column] = df[column].str.replace(",", "").astype(float, errors='ignore')

#Corrija a coluna 'Release Date' para o formato datetime.
df["Release Date"] = pd.to_datetime(df["Release Date"], format = "mixed") 

#Crie uma nova coluna chamada 'Streaming Popularity', 
# que seja a média da popularidade nas plataformas 'Spotify Popularity', 
# 'YouTube Views', 'TikTok Likes', e 'Shazam Counts'.
df["Streaming Popularity"] = df["Spotify Popularity"] + df["YouTube Views"] + df["TikTok Likes"] + df["Shazam Counts"] / 4

#crie uma coluna 'Total Streams', somando os valores de 'Spotify Streams', 
# 'YouTube Views', 'TikTok Views', 'Pandora Streams', e 'Soundcloud Streams'.
df["Total Streams"] =  df["Spotify Streams"] + df["YouTube Views"] + df["TikTok Views"] + df["Pandora Streams"] + df["Soundcloud Streams"]

#Filtre apenas as faixas onde a popularidade do Spotify ('Spotify Popularity') 
# é maior que 80 e que tenham mais de 1 milhão de streams totais ('Total Streams').
filtered_df = df [(df["Spotify Popularity"] > 80) & (df["Total Streams"] > 1000000)]

#Salvar um novo arquivo com os resultados filtrados
filtered_df.to_csv("/Users/minavelicastelo/Library/Mobile Documents/com~apple~CloudDocs/Reprograma/on33-python-s09-pandas-numpy-I/exercicios/para-casa/faixas_filtradas.json", index=False)
