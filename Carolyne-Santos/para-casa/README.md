# 📈📉📊🎲 Análise com Python - Pandas e Numpy I

## 📚 Descrição da Atividade

Exercicio para casa semana 11. Agora que já sabem como fazer o processo de ETL com pandas, é hora de brincar com a lista dos artistas mais ouvidos do SPOTIFY!

## 📋 Passo a Passo

## 🟦 Atividade 1 - Use o arquivo `mais_ouvidas_2024.csv` para análise. Lembre-se de garantir que o carregamento foi feito com sucesso:

 ### - Bibliotecas Utilizadas:

        # Biblioteca
        import pandas as pd

        # Carregando o arquivo 'vendas_filtradas', chamei de 'vendas'
        df = pd.read_csv("C:/Users/carol/OneDrive/Área de Trabalho/Reprograma/on33-python-s11-pandas-numpy-I/material/mais_ouvidas_2024.csv")

        # Visualizar df
        print(df.head())

## 🟦 Atividade 2 - Indentifique as colunas que contêm números, como 'Spotify Streams', 'YouTube Views', etc., e converta essas colunas para o tipo numérico se estiverem em outro formato. (Use replace() e astype()):

        # Visualizar Colunas
        print(df.columns)

        # Colunas
        # ['Track', 'Album Name', 'Artist', 'Release Date', 'ISRC',
        #       'All Time Rank', 'Track Score', 'Spotify Streams',
        #       'Spotify Playlist Count', 'Spotify Playlist Reach',
        #       'Spotify Popularity', 'YouTube Views', 'YouTube Likes', 'TikTok Posts',
        #       'TikTok Likes', 'TikTok Views', 'YouTube Playlist Reach',
        #       'Apple Music Playlist Count', 'AirPlay Spins', 'SiriusXM Spins',
        #       'Deezer Playlist Count', 'Deezer Playlist Reach',
        #       'Amazon Playlist Count', 'Pandora Streams', 'Pandora Track Stations',
        #       'Soundcloud Streams', 'Shazam Counts', 'TIDAL Popularity',
        #       'Explicit Track']

        # Visualizar typos
        print(df.dtypes)

        # Selecionar as colunas numéricas:
        colunas_numericas = ["All Time Rank", "Track Score", "Spotify Streams", "Spotify Playlist Count", 
                            "Spotify Playlist Reach", "Spotify Popularity", "YouTube Views", "YouTube Likes", 
                            "TikTok Posts", "TikTok Likes", "TikTok Views", "YouTube Playlist Reach",
                            "Apple Music Playlist Count", "AirPlay Spins", "SiriusXM Spins", "Deezer Playlist Count", 
                            "Deezer Playlist Reach", "Amazon Playlist Count", "Pandora Streams",
                                "Pandora Track Stations", "Soundcloud Streams", "Shazam Counts", 
                                "TIDAL Popularity", "Explicit Track"]

        # Converter as colunas numéricas para Float64
        for colunas in colunas_numericas:
            df[colunas] = df[colunas].replace(",", "", regex=True).astype("Float64")

## 🟦 Atividade 3 - Corrija a coluna 'Release Date' para o formato datetime.

        # Visualizar o formato dos dados da coluna 'Release Date'
        df["Release Date"] = pd.to_datetime(df["Release Date"], format="mixed")

        # Visualizar typos
        print(df.dtypes)

## 🟦 Atividade 4 - Crie uma nova coluna chamada 'Streaming Popularity', que seja a média da popularidade nas plataformas 'Spotify Popularity', 'YouTube Views', 'TikTok Likes', e 'Shazam Counts'. (lembrem-se que só é possível calcular médias e fazer operações matemáticas com tipos númericos):

        # Nova coluna 'Streaming Popularity' 
        df['Streaming Popularity'] = df[['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts']].mean(axis=1)

## 🟦 Atividade 5 - Crie uma coluna 'Total Streams', somando os valores de 'Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', e 'Soundcloud Streams':

        # Nova coluna 'Total Streams' 
        df['Total Streams'] = df[['Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', 'Soundcloud Streams']].sum(axis=1)

## 🟦 Atividade 6 - Filtre apenas as faixas onde a popularidade do Spotify ('Spotify Popularity') é maior que 80 e que tenham mais de 1 milhão de streams totais ('Total Streams'):

        # Faixas filtradas
        faixas_filtradas = df[(df['Spotify Popularity'] > 80) & (df['Total Streams'] > 1_000_000)]

## 🟦 Atividade 7 - Salve o DataFrame resultante em um novo arquivo JSON chamado 'faixas_filtradas.json':

        # Salvar df em formato json
        faixas_filtradas.to_json('faixas_filtradas.json', index=False)

## 🟦 Atividade 8 - Garanta que o arquivo foi salvo corretamente:

        # Carregando o arquivo 'faixas_filtradas.json', chamei de 'faixas'
        faixas = pd.read_json('C:/Users/carol/OneDrive/Área de Trabalho/Reprograma/on33-python-s11-pandas-numpy-I/Carolyne-Santos/para-casa/faixas_filtradas.json')

        # Visualizar
        print(faixas.head())
  
## 👩🏻‍🏫 Professora Manuelly Suzik.


 [![LinkdIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/manuellysuzik/)
</br>
 [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/manuellysuzik)</br>
