import numpy as np

anos = np.loadtxt('data/carros-anos.txt', dtype = int)
km = np.loadtxt('data/carros-km.txt')
valor = np.loadtxt('data/carros-valor.txt')
dataset = np.column_stack((anos, km, valor))
#print(dataset.shape)

print('=-'*30)
print(f'{"Media":^60}')
print('=-'*30)

#mean retorna a media dos elementos do array ao longo do eixo especifico
# axix = 0 media de cada coluna
# axis = 1 media em cada linha
print(np.mean(dataset, axis = 0))
print(np.mean(dataset[:,1]))
print(np.mean(dataset[:,2]))

print('=-'*30)
print(f'{"Desvio padrão":^60}')
print('=-'*30)
#std desvio padrao dos elementos do array ao longo do eixo especifico
print(np.std(dataset[:,2]))


print('=-'*30)
print(f'{"Sum":^60}')
print('=-'*30)
#sum soma dos elementos do array ao longo do eixo especifico

print(dataset.sum(axis = 0))
print(dataset[:,1].sum())
print(np.sum(dataset, axis = 0))
print(np.sum(dataset[:,1], axis = 0))