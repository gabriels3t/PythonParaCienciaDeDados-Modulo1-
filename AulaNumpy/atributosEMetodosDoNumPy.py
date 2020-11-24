import numpy as np

km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])
dados = np.array([km,anos])
contador = np.arange(10)
'''
print(dados.shape)
#ndim mosta as dimensoes
print(dados.ndim)
#size numero total dos elementos 
print(dados.size)
#dtype tipo dentro do array 
print(dados.dtype)
# T Retorna o array transposto, converte linha em coluna e vice versa
print(dados.T)'''

'''
---------------------------------
        MÉTODOS
----------------------------------

'''
'''
#tolist retorna o array como uma lista python
print(dados.tolist())
#reshape retorna um array que contem os mesmos dados com uma nova forma 
print(contador.reshape((5,2), order='C')) # formatacao linguaguem C
print(contador.reshape((5,2), order='F')) # formatacao  linguagem Fortran 
'''
#resize alterar a forma  e o tamanho do array (utilizar o refcheck)
dados_new = dados.copy()
dados_new.resize((3,5),refcheck=False)
dados_new[2] = dados_new[0]/(2019 - dados_new[1])
print(dados_new)

