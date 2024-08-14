import pandas as pd

['TransactionID', 'Date', 'MobileModel', 'Brand', 'Price', 'UnitsSold','TotalRevenue', 'CustomerAge', 'CustomerGender', 'Location','PaymentMethod']

df = pd.read_csv("../../material/mobile_sales.csv")

print(df.head())
print(df.columns)
df_valores_nulos = df.isnull()
print(df_valores_nulos.sum())
print(df.duplicated().sum)
print(df.dtypes)

df["Date"] = pd.to_datetime(df["Date"], format= 'mixed')
print(df.dtypes)

print(df["Date"]) # mostra os dados da coluna selecionada
print('Date')

df["Total Sales Value"] = df["Price"] * df["UnitsSold"] # Cria uma nova coluna com o título Total Sales Value através do produto de Price x UnitsSold 

print(df["Total Sales Value"]) # print a nova coluna

print(df.columns)

profit_per_product = 0.30

df['Profit Margin'] = (df['Price']*profit_per_product)* df['UnitsSold']
print(df['Profit Margin'])

filtered_df = df[(df["Total Sales Value"] > 100_000) & (df["Profit Margin"] > 20_000)]

print(filtered_df.head())

filtered_df.to_csv("./filtered_list.csv", index=False)