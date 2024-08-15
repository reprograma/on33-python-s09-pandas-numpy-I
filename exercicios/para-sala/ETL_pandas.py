import pandas as pd
#Index(['TransactionID', 'Date', 'MobileModel', 'Brand', 'Price', 'UnitsSold',
#       'TotalRevenue', 'CustomerAge', 'CustomerGender', 'Location',
#       'PaymentMethod']

#Extração de dados(extract):
df = pd.read_csv("material/mobile_sales.csv") 
#df = dataframe, é um dado tabular, contém colunas, linhas e índices. 
#É necessário que qualquer arquivo torne-se um
#dataframe para que possamos usar neles funções.

print(df.head(n = 5))
# #imprime as cinco primeiras linhas de uma tabela cvs. 
# # Pode se colocar imputs nele por ex.: df.head(n=5) ou df.head(5) para exibir as
# #cinco primeiras linhas. Se deixar em branco ele exibe, por padrão, cinco linhas.

print(df.columns) #o mesmo raciocínio da função a cima, mas ele exibe uma lista
# #com nome de todas as colunas existentes no arquivo.

# #Tratamento de dados(transform):
print(df.isnull()) #função que retorna uma expressão boleana 
# #'True' se a célula tem algum valor nulo, ou 'False' para as
# #que foram preenchidas.

df_valores_nulos = df.isnull() #Guardamos todos os valores nulos numa variável
# print(df_valores_nulos.sum()) #outra forma de ver valores nulos em números, somados. 

print(df.duplicated()) #Retorna boleanos 'True' se encontram linhas duplicadas 
# #e 'False' caso contrário.

print(df.dtypes) #função que me ajuda a saber (neste caso, exibe) os tipos de dados dentro de um dataframe. 
# #Retorna o tipo de dado contido em cada coluna. OBS: object=string.

# #formato != tipo
# #formato é como ele está escrito

df["Date"] = pd.to_datetime(df["Date"], format = "mixed") #Função do pandas, para converter tipos de dados.
# print(df.dtypes) # Mostrar uma coluna inteira
# print(df["Date"])

df["Total Sales Value"] = df["Price"] * df["UnitsSold"] #Operação matemática que multiplica os valores de uma
#dada coluna pela outra ao mesmo tempo que cria outra.
# print(df["Total Sales Value"])

#Exercício:
#Crie uma coluna 'Profit Margin', assumindo que o custo de fabricação é 70% do preço ('Price'), 
#a margem de lucro pode ser calculada como (Price * 0.30) * UnitsSold.
df["Desconto"] = df["Price"] * 0.30
# print(df["Desconto"])

df["Profit Margin"] = df["Desconto"] * df["UnitsSold"] #Operação matemática que multiplica os valores de uma
#dada coluna pela outra ao mesmo tempo que cria outra.
# print(df["Profit Margin"])
# print(df.columns)

#Filtragem
filtered_df = df [(df["Total Sales Value"] > 100_000) & (df["Profit Margin"] > 20_000)]
print(filtered_df)

#carregamento:
filtered_df.to_csv("/Users/minavelicastelo/Library/Mobile Documents/com~apple~CloudDocs/Reprograma/on33-python-s09-pandas-numpy-I/exercicios/para-sala/filterd_list.csv", index=False)# a operação boleana 'index=False' 
#significa que o pandas não manda o index para o arquivo novo criado.
