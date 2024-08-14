import pandas as pd
#Colunas ['TransactionID', 'Date', 'MobileModel', 'Brand', 'Price', 'UnitsSold','TotalRevenue', 'CustomerAge', 'CustomerGender', 'Location','PaymentMethod']

df = pd.read_csv("../../material/mobile_sales.csv")

print(df.head(n=10))#Traz as 5 primeiras linhas do arquivo, quado coloca n=10, vai aparecer o numero indicado de linhas
print(df.columns)
df_valores_nulos = df.isnull() #identifica valores nulos
print(df_valores_nulos.sum())
print(df.duplicated()) #identificar valores duplicados

#DETECTA OS TIPOS CORRETOS DE DADOS QUE TEM NAS COLUNAS
#OBJECT = STRING
print(df.dtypes)

#Traz os dados da coluna que você informa
print(df["Date"])

#formatar o tipo de informação da coluna
df["Date"] = pd.to_datetime(df["Date"], format="mixed")
print(df.dtypes)

#Crie uma nova coluna chamada 'Total Sales Value', que seja o produto de 'Price' e 'UnitsSold'.
df["Total Sales Value"] = df["Price"] * df["UnitsSold"]
print(df.columns)

#Crie uma coluna 'Profit Margin', assumindo que o custo de fabricação é 70% do preço ('Price'), a margem de lucro pode ser calculada como (Price * 0.30) * UnitsSold.
profit_per_product = 0.30
df["Profit Margin"] = (df["Price"] * profit_per_product) * df["UnitsSold"]
print(df["Profit Margin"])

#- Filtre as transações onde o 'Total Sales Value' é maior que 100,000 e a margem de lucro ('Profit Margin') é maior que 20,000.
filtered_df = df[(df["Total Sales Value"] > 1000_000) & (df["Profit Margin"] > 20_000)]
print(filtered_df.head())

#Salve o DataFrame resultante em um novo arquivo CSV chamado 'vendas_filtradas.csv'.
filtered_df.to_csv("./filtered_list.csv", index=False)

# Carregue este arquivo salvo e exiba as primeiras 5 linhas para verificar.



