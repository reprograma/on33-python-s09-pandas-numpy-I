import pandas as pd
#'TransactionID', 'Date', 'MobileModel', 'Brand', 'Price', 'UnitsSold','TotalRevenue', 'CustomerAge', 'CustomerGender', 'Location','PaymentMethod'
df = pd.read_csv("../../material/mobile_sales.csv")
#print(df.head())
#print(df.columns)
#df_valores_nulos=df.isnull()
#print (df_valores_nulos.sum())
#print (df.duplicated().sum())
#df.drop_duplicates
#print(df.dtypes)
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
#print (df['Date'])
#print(df.dtypes)

df['Total sales value'] = df['Price'] * df['UnitsSold']
print(df.columns)

df['Profit Margin'] = (df['Price']*0.30)* df['UnitsSold']
print(df['Profit Margin'])

filtered_df = df [(df["Total sales value"] > 100_000) & (df["Profit Margin"] > 20_000)]


print(filtered_df.head())

filtered_df.to_csv('./filtered_list.csv', index=False)