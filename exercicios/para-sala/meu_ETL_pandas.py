import pandas as pd


#Index(['TransactionID', 'Date', 'MobileModel', 'Brand', 'Price', 'UnitsSold', 'TotalRevenue', 'CustomerAge', 'CustomerGender', 'Location', 'PaymentMethod'],dtype='object')


df = pd.read_csv("../../material/mobile_sales.csv")
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
print(df.head())
print(df.head(n=10))
print(df.columns)

df_valores_nulos = df.isnull()
print(df_valores_nulos.sum())

print(df.isnull().sum())
print(df.duplicated().sum())

df["Total Sales Value"] = df["Price"] * df["UnitsSold"] # 
print(df["Total Sales Value"]) 

#df["Profit Margin"] = (df["Price"] * 0.30) *  df ["UnitsSold"] 
# ^ o valor extraido do total de tudo com a multiplicação por ultimo ou jeito mais legivel onde a multiplicação por 0.30 fica dentro do price 


print(df["Profit Margin"])

filtered_df = df[(df["Total Sales Value"] > 100_000) & (df["Profit Margin"] > 20_000)]


print(filtered_df.head())


filtered_df.to_csv("./lista_filtrada.csv" , index=False)


