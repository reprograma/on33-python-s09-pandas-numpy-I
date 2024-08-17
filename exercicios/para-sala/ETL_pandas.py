import pandas as pd

#['TransactionID', 'Date', 'MobileModel', 'Brand', 'Price', 'UnitsSold','TotalRevenue', 'CustomerAge', 'CustomerGender', 'Location','PaymentMethod']

df = pd.read_csv("C:/Users/Usuario/OneDrive/Área de Trabalho/On33-Python/FORK/on33-python-s09-pandas-numpy-I/material/mobile_sales.csv")

#transformando os dados#

# print(df.head())
# print (df.columns)
# df_valores_nulos = df.isnull()
# print(df_valores_nulos.sum())
#print(df.duplicated(). sum())
#print(df.dtypes)
df['Dade'] = pd.to_datetime((df['Date']), format="mixed")
#print(df.dtypes)

df["Total Sales Value"] = df['Price'] * df['UnitsSold']
# print(df["Total Sales Value"])
profit_per_product = 0.30
df["Profit Margin"] = (df["Price"]  * profit_per_product ) * df["UnitsSold"] 

filtered_df = df[(df['Total Sales Value'] > 100_000) & (df['Profit Margin'] > 20_000)]
print(filtered_df)

filtered_df.to_csv("./filtered_list.csv", index=False)
