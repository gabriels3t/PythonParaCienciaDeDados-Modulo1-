import numpy as np


#listas em python
'''
km = [44410., 5712., 37123., 0., 25757.]
anos = [2003, 1991, 1990, 2019, 2006]
'''
#idade = 2019 - anos # Acontece um erro
#utilizando o numpy
km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])
idade = 2019 - anos
km_media = km/idade
#print(km_media)

'''
---------------------------------
    ARRAYS COM DUAS DIMENSOES
---------------------------------
'''
dados = np.array([km,anos])
#print(dados.shape)
print(dados[0])
print(dados[1])
km_media = dados[0] / (2019 - dados[1])
print(km_media)