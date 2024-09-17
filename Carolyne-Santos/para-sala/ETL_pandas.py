#Biblioteca
import pandas as pd

#Baixando o arquivo
df = pd.read_csv("C:/Users/carol/OneDrive/Área de Trabalho/Reprograma/on33-python-s11-pandas-numpy-I/Carolyne-Santos/para-sala/filtered_list.csv")

#Colunas
#['TransactionID', 'Date', 'MobileModel', 'Brand', 'Price', 'UnitsSold',
#       'TotalRevenue', 'CustomerAge', 'CustomerGender', 'Location',
#       'PaymentMethod', 'Total Sales Value', 'Profit Margin']

#Visualizar
print(df.head())
print(df.columns)
df_valores_nulos = df.isnull()
print(df_valores_nulos.sum())
print(df.duplicated().sum())
print(df.dtypes)

#Visualizar o formato dos dados da coluna 'Date'
df["Date"] = pd.to_datetime(df["Date"], format="mixed")
print(df.dtypes)

#Criar uma nova coluna calculada 'Total de Vendas'
df["Total Sales Value"] = df["Price"] * df["UnitsSold"]
print(df.columns)

#Criar uma nova coluna calculada 'margem de lucro'
profit_per_product = 0.30
df["Profit Margin"] = (df["Price"] * profit_per_product) * df["UnitsSold"]

#Filtrando o df = 'total de vendas' acima de  100.000 e 'margem de lucro' acima de  20.000
# o (_) esta sendo usado entre os numeros pois assim ele identifica se os dados estiverem com (,) ou (.)
filtered_df = df[(df["Total Sales Value"] > 100_000) & (df["Profit Margin"] > 20_000)]
print(filtered_df.head())

#Salvar em csv nosso df filtrado como 'vendas_filtradas'
filtered_df.to_csv("C:/Users/carol/OneDrive/Área de Trabalho/Reprograma/on33-python-s11-pandas-numpy-I/Carolyne-Santos/para-sala/vendas_filtradas.csv", index=False)