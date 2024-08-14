import pandas as pd

df = pd.read_csv("../../material/mais_ouvidas_2024.csv")

print(df.head())
print(df.dtypes)


#Aqui criamos uma variável que armazena em uma lista (nome_colunas) as colunas existentes em um csv, sem a necessidade de copiar e colar os valores 
nome_colunas = df.columns.tolist()


#Para converter as colunas numéricas em formato de números não usei replace e astype. Usei direto o to_numeric e usei o replace para retirar as vírgulas em um for para fazer uma série de transformações. (1) analisa se a coluna é do tipo ocject, se sim (2) aplica o to_numeric, checando se aquele valor pode ser transformado em float ou int. Contudo, como haviam vírgulas em alguns números essa função não completava, por isso, apliquei o str.replace para trocar todas as vírgulas que ele encontrasse por vazio (""). Os erros foram ignorados, mas os espaços vazios foram substituídos por NaN. Preferi não filtrar com o fillna porque mudava o tipo da coluna como um todo para object quando havia um espaço vazio. 
for coluna in nome_colunas:
    if df[coluna].dtype == "object":
        df[coluna] = pd.to_numeric(df[coluna].str.replace(",", ""), errors = "ignore")


#Convertendo a coluna Release Date para Datetime
df["Release Date"] = pd.to_datetime(df["Release Date"], errors = "ignore")


#Criando a coluna Streaming Popularity e calculando a média dos valores. A determinação do axis nesse caso é importante porque por padrão ele vem como None, e faz uma agregação em ambos os eixos, ou seja, exibiria o resultado geral em todas as linhas e como uma soma total da coluna. Determinando axis=1, estamos indicando que a operação vai ser realizada ao longo das linhas, individualmente.
df["Streaming Popularity"] = df[["Spotify Popularity", "YouTube Views", "TikTok Likes", "Shazam Counts"]].mean(axis=1)


#Criando a coluna Total Streams, com a mesma lógica utilizada acima.
df["Total Streams"] = df[["Spotify Streams", "YouTube Views", "TikTok Views", "Pandora Streams", "Soundcloud Streams"]].sum(axis=1)


#Prints de consulta criados para verificar os tipos das colunas após as conversões solicitadas.
print (df.dtypes)
print(df.head(20))


#Filtro aplicado para filtrar as faixas conforme solicitado no exercício. Adicionalmente foi criado um arquivo csv também
filtered_df = df[(df["Spotify Popularity"] > 80) & (df["Total Streams"] > 1000000)]
filtered_df.to_json("./filtered_list.json", index=False)
filtered_df.to_csv("./filtered_list.csv", index=False)


#Código para consultar o json criado
df = pd.read_json("./filtered_list.json")
print(df.head())
print(df.dtypes)


#Código para consultar o csv criado adicionalmente
df = pd.read_csv("./filtered_list.csv")
print(df.head())
print(df.dtypes)