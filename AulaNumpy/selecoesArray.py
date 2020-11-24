import numpy as np

km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])
dados = np.array([km,anos])

contador = np.arange(10)
item = 10
index = item - 1

#print(contador[index])
#print(contador[-1])
'''
print(dados[1][2])
# OU
print(dados[1,2])
'''
#print(contador[1:4])
'''
#com passo
print(contador[1:8:2])
print(contador[1::2])
'''

#print(dados[:,1:3])
print(dados[:,1:3][0])
print(dados[:,1:3][1])
print('km Medio '+str(dados[:,1:3][0]/(2019 - dados[:,1:3][1])))
print(contador > 5)
print(contador[contador >5 ])

print(dados[:,dados[1] > 2000][0])
km_medio = dados[:,dados[1] > 2000][0]/(2019 - dados[:,dados[1] > 2000])
print(f'Km medio dos carros Lançados depois de 2000 {km_medio}')