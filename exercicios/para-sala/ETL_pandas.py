import pandas as pd

#['TransactionID', 'Date', 'MobileModel', 'Brand', 'Price', 'UnitsSold','TotalRevenue', 'CustomerAge', 'CustomerGender', 'Location','PaymentMethod']
# Substitua 'caminho/para/seu/arquivo.csv' pelo caminho real do seu arquivo CSV
#caminho_arquivo = 'C:/Users/sanel/OneDrive/Área de Trabalho/git-on33/on33-python-s011-pandas-numpy/material/mobile_sales.csv'

# Carregar o arquivo CSV em um DataFrame do Pandas
df = pd.read_csv(r"C:/Users/sanel/OneDrive/Área de Trabalho/git-on33/on33-python-s011-pandas-numpy/material/mobile_sales.csv")


# Exibir as primeiras linhas do DataFrame para verificar o carregamento
#print(df.head(n=10))
#print(df.columns)
#print(df.isnull())
#df_valores_nulos = df.isnull()
#print(df_valores_nulos.sum())
#print(df.duplicated().sum())
#print(df.dtypes)
#print(df["Date"])
df["Date"] = pd.to_datetime(df["Date"], format="mixed")
#print(df.dtypes)
#print(df["Date"])

df["Total Sales Value"] = df["Price"] * df["UnitsSold"]
#print(df["Total Sales Value"])
#print(df.columns)
profit_per_product = 0.30

df["Profit Margin"] = df["Price"] * df["UnitsSold"] * 0.30

filtered_df = df[(df["Total Sales Value"]>100_00) & (df["Profit Margin"] > 20_00)]

print(filtered_df.head())

filtered_df.to_csv("./exercicios\para-sala/filtered_list.csv", index=False)


