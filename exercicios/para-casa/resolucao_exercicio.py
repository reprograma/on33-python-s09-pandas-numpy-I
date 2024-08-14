import pandas as pd
df = pd.read_csv("../../material/mais_ouvidas_2024.csv")

# Verificar se a base foi feita com sucesso:
#print(df.head())
#print(df.dtypes)

# Converter as bases numéricas para Float64:

numerical_columns = ["All Time Rank", "Track Score", "Spotify Streams", "Spotify Playlist Count", "Spotify Playlist Reach", "Spotify Popularity", "YouTube Views", "YouTube Likes", "TikTok Posts", "TikTok Likes", "TikTok Views", "YouTube Playlist Reach", "Apple Music Playlist Count", "AirPlay Spins", "SiriusXM Spins", "Deezer Playlist Count", "Deezer Playlist Reach", "Amazon Playlist Count", "Pandora Streams", "Pandora Track Stations", "Soundcloud Streams", "Shazam Counts", "TIDAL Popularity", "Explicit Track"]

# Função for in para a lista:

for col in numerical_columns:
    df[col] = df[col].replace(",", "", regex=True).astype("Float64")
    #print(df[col])

# Corrigir a coluna para datetime
df["Release Date"] = pd.to_datetime(df["Release Date"])
#print(df.dtypes)

# Nova coluna Streaming Popularity como média das colunas utilizando o mean(axis=1):
df['Streaming Popularity'] = df[['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts']].mean(axis=1)

# Criar a coluna 'Total Streams' com a soma utilizando o .sum(axis=1):
df['Total Streams'] = df[['Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', 'Soundcloud Streams']].sum(axis=1)

# Filtrar as faixas onde 'Spotify Popularity' > 80 e 'Total Streams' > 1 milhão:
faixas_filtradas = df[(df['Spotify Popularity'] > 80) & (df['Total Streams'] > 1_000_000)]

# Salvar base em um arquivo JSON
faixas_filtradas.to_json('faixas_filtradas.json', orient='records', lines=True)

# Para verificar se o arquivo foi salvo:
# Carregar novamente para garantir que os dados foram escritos corretamente
df_verificacao = pd.read_json('faixas_filtradas.json', orient='records', lines=True)
print(df_verificacao.head())
