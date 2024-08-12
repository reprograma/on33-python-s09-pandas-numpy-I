import pandas as pd

df = pd.read_csv("C:/git-on33/on33-python-s09-pandas-numpy-I/material/mais_ouvidas_2024.csv")

#print(df.head())
# print(df.columns)
# df_valores_nulos = df.isnull())
# print(df_valores_nulos.sum())
# print(df.duplicated().sum())
#print(df.dtypes)
possible_num_cols = [col for col in df.columns if df[col].dtype == 'object'] #  Identificar colunas que podem conter números e que são do tipo 'object'
num_cols = [col for col in possible_num_cols if 'Streams' in col or 'Views' in col or 'Count' in col or 'Likes' in col or 'Spins' in col or 'Reach' in col or 'Rank' in col or 'Stations' in col] # filtrar ainda mais as colunas que têm nomes que indicam que provavelmente contêm números
#print(num_cols)
for col in num_cols:
 df[col] = df[col].replace(',', '', regex=True) # Remover caracteres indesejados (exemplo: vírgulas, espaços)
df[col] = df[col].astype(float)
for col in num_cols:
    df[col] = df[col].fillna(0).astype(int) # tratar valores em branco
#print(df.dtypes)
#df["Release Date"] = pd.to_datetime(df["Release Date"], format="mixed" )
#df["Spotify Popularity"] = df["Spotify Popularity"].fillna(0).astype(int)
#columns_media = ['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts']
#df['Streaming Popularity'] = df[columns_media].mean(axis=1) #calcular média

#print(df['Streaming Popularity'].head())
columns_soma = ['Spotify Popularity', 'YouTube Views', 'TikTok Views', 'Pandora Streams', 'Soundcloud Streams']
df['Total Streams'] = df[columns_soma].sum(axis=1)
df['Total Streams'] = df['Total Streams'].fillna(0).astype(int)
#print(df['Total Streams'].head())
#print(df.dtypes)

# Filtre apenas as faixas onde a popularidade do Spotify ('Spotify Popularity') é maior que 80 e que tenham mais de 1 milhão de streams totais ('Total Streams').
filtered_df = df[(df["Spotify Popularity"] > 80 ) & (df["Total Streams"] > 1_000_000)]
print(filtered_df.head())

filtered_df.to_json("./faixas_filtradas.json", index=False)

