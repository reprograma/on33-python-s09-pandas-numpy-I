import pandas as pd # import o panda como um pd(apelido para o panda)

# A prof pediu para colocar os elementos que sairam pelo df.columns (o nome das colunas)
#'TransactionID', 'Date', 'MobileModel', 'Brand', 'Price', 'UnitsSold','TotalRevenue', 'CustomerAge', 'CustomerGender', 'Location','PaymentMethod'


df = pd.read_csv("C:/Users/andre/OneDrive/Área de Trabalho/REPROGRAMA/SEMANA 11/on33-python-s09-pandas-numpy-I/material/mobile_sales.csv")

# print(df.head()) # o head retorna o df = seria tipo um banco de dados, o head mostra as primeiras 5 linhas

print(df.head(n=10)) # dessa forma vai me mostrar as 10 primeiras linhas, logo n retorna as linhas que solicitei (se n for maior que o número de linhas existentes ele mostra só as linhas existentes, não dá erro)

print(df.columns) # mostra quantas colunas tem no csv e mostra as colunas = o index(os nomes)

# df_valores_nulos =df.isnull() # retorna False se os valores não forem nulos e True se tiver valor nulo na tabela (nulo é espaço vazio)
# print(df_valores_nulos.sum())
print(df.duplicated().sum()) #retorna as duplicadas, usando o Sum mostra o total de duplicadas

print(df.dtypes) # retorna o tipo de dados de cada coluna / object = string

# item = df['Date']
# print(item) # ou print(df['Date']) imprime a coluna Date

#Para converter dados
# o pd.to_datetime - transformamos a coluna date em datetime
df['Date'] = pd.to_datetime(df['Date'], format="mixed") # o mixed mantem o formato e serve para ???

print(df.dtypes)

df["Total Sales Value"] = df["Price"] * df["UnitsSold"] # Cria uma nova coluna com o título Total Sales Value através do produto de Price x UnitsSold 
print(df["Total Sales Value"]) # print a nova coluna

print(df.columns)

df["Profit Margin"] = (df["Price"] * 0.30) * df["UnitsSold"] 
print(df["Profit Margin"]) # print a nova coluna

print(df.columns)

df["Profit Margin 2"] = df["Total Sales Value"] * 0.30 
print(df["Profit Margin 2"]) # print a nova coluna

filtered_df = df [(df["Total Sales Value"] > 100_000) & (df["Profit Margin 2"] > 20_000)]
print(filtered_df)

filtered_df2 = df [(df["PaymentMethod"] == "Online")]
print(filtered_df2)

filtered_df.to_csv("./filtered_list.csv", index=False) # Transforma o arquivo filtrado em csv e index = False não coloca os index