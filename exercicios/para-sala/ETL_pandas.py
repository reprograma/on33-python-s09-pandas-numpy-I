import pandas as pd #nickname de pd, para não ter que digitar o nome Pandas ao longo do código.
#['TransactionID', 'Date', 'MobileModel', 'Brand', 'Price', 'UnitsSold','TotalRevenue', 'CustomerAge', 'CustomerGender', 'Location','PaymentMethod']
df = pd.read_csv(r"C:\Users\flavi_000\OneDrive\Flavienne\Cursos\Reprograma\S11 - 10.08\on33-python-s09-pandas-numpy-I\exercicios\para-sala\ETL_pandas.py")
print(df.head()) # head seleciona o número de linhas, padrão são 5, caso queira visualizar outros n=x
print(df.columns) #expõem as colunas do dataframe no terminal
df_valores_nulos = df.isnull() #permite identificar quais células contêm dados faltantes, vazios, nulos.
print(df_valores_nulos.sum())
print(df.duplicated().sum()) #conta o número de linhas duplicadas em um DataFrame Pandas.
print(df.dtypes) #entender seus dados em Pandas. Ele fornece uma visão rápida dos tipos de dados presentes em cada coluna do seu DataFrame
                 # objest neste caso é string, float, inteiro; ele aplica nas informações das colunas, o cabeçalho é só um direcionamento p a análise.
                 #o número na float que pode aparecer no int é o intervalo que cabe pontos
df["Date"] = pd.to_datetime(df["Date"], format="mixed") #terá seu valor(formato) substiuito pelo pandas na nomenclatura

print(df["Date"]) # serve para exibir a coluna especificada por "Date" dentro de um DataFrame chamado 
#pode trocar o mixed para:"%Y//%m/%d"

df["Total Sales Value"] = df["Price"] * df["UnitsSold"]
print(df.columns)

#- Crie uma coluna 'Profit Margin', assumindo que o custo de fabricação é 70% do preço ('Price'), a margem de lucro pode ser calculada como (Price * 0.30) * UnitsSold.
df ["Profit Margin"] = (df["Price"] * 0.30) * df['UnitsSold'] 
print(df.columns)
print(df["Profit Margin"])

filtered_df = df[(df["Total Sales Value"]>100_000) & (df["Profit Margin"] >20_000)]
print(filtered_df.head())

filtered_df.to_csv("./filtered_list.csv", index=False) #salvar em um arquivo csv, o pandas 