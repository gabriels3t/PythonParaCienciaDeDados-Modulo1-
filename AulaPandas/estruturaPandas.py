import pandas as pd

carros = ['Jetta Variant', 'Passat', 'Crossfox']


'''
-------------------------------------
        SERIES()
-------------------------------------
'''
# Series são arrays unidimensionais rotulados capazes de armazenar qualquer tipo de dado. os rotulos das linhas são chamadas de index .
#  A forma basica de criação de uma series é :
#pd.Series(dados, index = index)
# dados pode ser um dicionario, lista ,array numpy ou constante

'''
-------------------------------------
        DATAFRAMES()
-------------------------------------
'''

#DataFrame é uma estrutura de dados tubular bidimensional com rotulos nas linhas e colunas ,
# os DataFrames são capazes de armazenar qualquer tipo de dados O DATAFRAME É UMA DAS FUNÇÕES MAIS IMPORTANDE DO PANDAS
#pd.DataFrame(dados, index = index, columns = columns)
#dados pode ser um dicionario, lista ,array numpy ,Series ou dataFrame


pd.Series(carros)
'''
Criando um DataFrame a partir de uma lista de dicionarios

'''
dados = [
    {'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003, 'Quilometragem': 44410.0, 'Zero_km': False, 'Valor': 88078.64},
    {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991, 'Quilometragem': 5712.0, 'Zero_km': False, 'Valor': 106161.94},
    {'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990, 'Quilometragem': 37123.0, 'Zero_km': False, 'Valor': 72832.16}
]
#dataset = pd.DataFrame(dados)
#print(dataset)
# para mudar a ordem
#dataset[['Ano','Nome']]

dados = {
    'Nome': ['Jetta Variant', 'Passat', 'Crossfox'], 
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8'],
    'Ano': [2003, 1991, 1990],
    'Quilometragem': [44410.0, 5712.0, 37123.0],
    'Zero_km': [False, False, False],
    'Valor': [88078.64, 106161.94, 72832.16]
}
#dataset = pd.DataFrame(dados)
#print(dataset)

'''
    Utilizando dados externos
'''
dataset = pd.read_csv('data/db.csv', sep=';', index_col =  0)

'''
-------------------------------------
    SELEÇÕES COM DATAFRAME
-------------------------------------
'''
'''
    head() mostra as 5 primeiras registros
'''
#print(dataset.head())

'''
    Selecionar colunas
'''
#print(dataset['Valor'])
'''
    retornar 1 dataframe
'''
#print(dataset[['Valor']])
'''
    seleção de linhas
'''
# mesmo jeito de tuplas e lista
#print(dataset[0:3])
'''
 .loc seleciona um grupo de linhas e colunas segundo os rotulos ou uma matriz booleana
 OBS RETORMA APENAS UMA LINHA
'''

#print(dataset.loc['Passat'])
'''
 para retornar um dataframe e mais de um valor
'''
#print(dataset.loc[['Passat','DS5']])
'''
 Selecionando variaves 
'''
#print(dataset.loc[['Passat','DS5'],['Motor','Valor']])
'''
 mostrar todas as linhas 
'''

#print(dataset.loc[:,['Motor','Valor']])
'''
    Utilizando o iloc
    Seleção com base em indices , se baseia na posição das informações
'''

#print(dataset.iloc[[1]])
#print(dataset.iloc[1:4])
'''
linhas e colunas específicas 
'''
#print(dataset.iloc[1:4,[0,5,2]])
'''
    todas as linhas
'''
#print(dataset.iloc[:,[0,5,2]])

'''
-------------------------------------
   QUERIES COM DATAFRAME
-------------------------------------
'''
'''
caso seja apenas uma query sem espaços, .nome
'''
#print(dataset.Motor)
select = dataset.Motor == 'Motor Diesel' #retorna booleano
#print(dataset[select])# retorna apenas os trues 


'''
Mais de uma query
'''
#print(dataset[(dataset.Motor == 'Motor Diesel') & (dataset.Zero_km == True)]) #Retorna as informações do select 

'''
    Utilizando o metodo Query
'''
#print(dataset.query('Motor == "Motor Diesel" and Zero_km == True'))

'''
-------------------------------------
   ITERANDO COM DATAFRAMES
-------------------------------------
'''
print(dataset)
for index , row in dataset.iterrows():
    
    if(2019 - row['Ano'] != 0):
        dataset.loc[index, 'Km_media'] = row['Quilometragem']/(2019 - row['Ano'])
    else:
        dataset.loc[index,'Km_media'] = 0


#print(dataset)


'''
-------------------------------------
    TRATAMENTO DE DADOS
-------------------------------------
'''
'''
    Utilizando a função isna retorna uma Series booleana , quando o valor for nulo vai retornar True
'''
#print(dataset.Quilometragem.isna())
#print(dataset[dataset.Quilometragem.isna()])
'''
    preencher valores nulos
    dataset.fillna(0) Alteração apenas na visualização
    fillna(0,inplace=True ) inplace altera no dataset 
'''
#dataset.fillna(0, inplace=True)
dataset.fillna(0,inplace=True)
print(dataset.query('Zero_km == True'))

dataset = pd.read_csv('data/db.csv', sep=';') 
'''
deletar na
'''
dataset.dropna(subset = ['Quilometragem'],inplace=True)
print(dataset)