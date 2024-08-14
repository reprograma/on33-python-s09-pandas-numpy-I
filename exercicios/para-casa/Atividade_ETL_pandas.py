import pandas as pd

# Carregar o DataFrame
df = pd.read_csv("C:/Users/flavi_000/OneDrive/Flavienne/Cursos/Reprograma/S11 - 10.08/on33-python-s09-pandas-numpy-I/material/mais_ouvidas_2024.csv")

# Verificar os tipos de dados
print(df.dtypes)

# Converter colunas numéricas e datas
numeric_cols = df.select_dtypes(include=['object']).columns
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col].str.replace(',', ''), errors='coerce')

df['Data de lançamento'] = pd.to_datetime(df['Data de lançamento'], errors='coerce')

# Criar novas colunas
df['Popularidade do Streaming'] = df[['Popularidade do Spotify', 'Visualizações do YouTube', 'Curtidas do TikTok', 'Contagens do Shazam']].mean(axis=1)
df['Total de Transmissões'] = df[['Transmissões do Spotify', 'Visualizações do YouTube', 'Visualizações do TikTok', 'Transmissões do Pandora', 'Transmissões do Soundcloud']].sum(axis=1)

# Filtrar e salvar os dados
filtered_df = df[(df['Popularidade do Spotify'] > 80) & (df['Total de Transmissões'] > 1000000)]
filtered_df.to_json("./filtered_list.json", orient='records', index=False)
filtered_df.to_csv("./filtered_list.csv", index=False)

# Carregar os dados salvos e verificar
df_json = pd.read_json("./filtered_list.json")
print(df_json.head())
print(df_json.dtypes)

df_csv = pd.read_csv("./filtered_list.csv")
print(df_csv.head())
print(df_csv.dtypes)