import pandas as pd

# ['TransactionID', 'Date', 'MobileModel', 'Brand', 'Price', 'UnitsSold', 'TotalRevenue', 'CustomerAge', 'CustomerGender', 'Location', 'PaymentMethod']

df = pd.read_csv("../../material/mobile_sales.csv")

# Mostrar as 10 primeiras linhas ao invés do padrão 5
# print(df.head(n=10))

# print(df.head())
# print(df.columns)
df_valores_nulos = df.isnull()
# print(df_valores_nulos.sum())
# Verificar dados duplicados
#print(df.duplicated().sum())
df.drop_duplicates()

df["Date"] = pd.to_datetime(df["Date"], format="mixed")
#print(df.dtypes)
#print(df["Date"])

df["Total Sales Value"] = df["Price"] * df["UnitsSold"]
# print(df.columns)
# print(df["Total Sales Value"])

profit_per_product = 0.30
df["Profit Margin"] = (df["Price"] * profit_per_product ) * df["UnitsSold"]

filtered_df = df[(df["Total Sales Value"] > 100_000) & (df["Profit Margin"] > 20_000)]

print(filtered_df.head())

filtered_df.to_csv("./filtered_list.csv", index=False)
