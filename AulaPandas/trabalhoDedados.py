import pandas as pd
'''
pd.set_option('display.max_rows',1000) # mostrar o maximo de linhas
pd.set_option('display.max_columns',1000) # mostrar o maximo de colunas
'''
dataset = pd.read_csv('data/db.csv', sep=';')
print(dataset)
'''
# object = string
print(dataset[['Quilometragem','Valor']].describe()) #Describe Mosta dados estatisticos basicos
'''
print(dataset.info())