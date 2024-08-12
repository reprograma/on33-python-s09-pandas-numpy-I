import pandas as pd

df = pd.read_csv("../../material/mobile_sales.csv")

#print(df.head(n=10))
#print(df.columns)
#df_valores_nulos = df.isnull()
#print(df_valores_nulos.sum())
#print(df.duplicated())
#print(df.dtypes)

#df["Date"] = pd.to_datetime(df["Date"], format="mixed")
#print(df.dtypes)

#df = df["Total Sales Value"]
#print(df["Total Sales Value"])

df["Total Sales Value"] = df["Price"] * df["UnitsSold"] # Cria uma nova coluna com o título Total Sales Value através do produto de Price x UnitsSold 
print(df["Total Sales Value"]) # print a nova coluna
print(df.columns)

df['Profit Margin'] = (df['Price'] * 0.30) * df['UnitsSold']
print(df["Profit Margin"])
print(df.columns)

filtered_df = df[(df["Total Sales Value"] > 100_000) & (df["Profit Margin"] > 20_000)]
print(filtered_df)

filtered_df.to_csv("./teste_lady.csv", index=False) 