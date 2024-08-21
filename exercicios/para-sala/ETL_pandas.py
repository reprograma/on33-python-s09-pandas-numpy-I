import pandas as pd 

##['TransactionID', 'Date', 'MobileModel', 'Brand', 'Price', 'UnitsSold','TotalRevenue', 'CustomerAge', 'CustomerGender', 'Location','PaymentMethod']

df = pd.read_csv(
    "C:/Users/thai/Downloads/reprograma/on33-python-s09-pandas-numpy-I/material/mobile_sales.csv"
)

print(df.head(n=10))#Traz as 10 primeiras linhas do arquivo
print(df.columns)
df_valores_nulos = df.isnull() #identifica valores nulos
print(df_valores_nulos.sum())
print(df.duplicated()) #identificar valores duplicados

df['Date'] = pd.to_datetime(df['Date'], format="mixed")

df["Total Sales Value"] = df["Price"] * df["UnitsSold"] # Cria uma nova coluna com o título Total Sales Value através do produto de Price x UnitsSold 
print(df["Total Sales Value"]) # print a nova coluna
print(df.columns)
df["Profit Margin"] = (df["Price"] * 0.30) * df["UnitsSold"] 
print(df["Profit Margin"]) # print a nova coluna
print(df.columns)

#Filtragem
filtered_df = df [(df["Total Sales Value"] > 100_000) & (df["Profit Margin"] > 20_000)]
print(filtered_df)
