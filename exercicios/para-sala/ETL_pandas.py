import pandas as pd

df = pd.read_csv("C:/Users/Colaborador/Reprograma/on33-python-s09-pandas-numpy-I/material/mobile_sales.csv")

#print(df.head(n=10))
#print(df.columns)
#df_valores_nulos = df.isnull()
#print(df_valores_nulos.sum())
#print(df.isnull())
#df_valores_nulos = df.isnull()
#print(df_valores_nulos.sum())
#print(df.duplicated().sum())
#print(df.dtypes)

df["Date"] = pd.to_datetime(df["Date"], format="mixed")

#print(df.dtypes)
#print(df["Date"])

df["Total Sales Value"] = df["Price"] *df["UnitsSold"]
#print (df.columns)

df["Profit Margin"] = (df["Price"] * 0.30) * df["UnitsSold"] 

filtered_df = df [(df["Total Sales Value"] > 100_000) & (df["Profit Margin"] > 20_000)]
                 
print(filtered_df)

filtered_df.to_csv("./filtered_list.csv", index=False)