carros = ['Jetta Variant', 'Passat', 'Crossfox']
valores = [88078.64, 106161.94, 72832.16]

print(carros.index('Passat'))
print(valores[carros.index('Passat')])

#dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
#print(dados)
dados = dict(zip(carros,valores))
print(dados)

#consultar valor de uma chave
print(dados['Passat'])

#Vefificar se existe chave
print('Passat' in dados)

#tamanho do dicionario
print(len(dados))

#adicionar no dicionario
dados['DS5'] = 124549.07

#deletar 
del dados['DS5']

'''
-------------------------------------------
        MÉTODOS DE DICIONÁRIOS
-------------------------------------------
'''


'''
-------------------------------------------
        update()
-------------------------------------------
'''
dados.update({'DS5':124549.07})


dados.update({'DS5':124552.77,'Fusca':150000})
print(dados)

'''
-------------------------------------------
        copy()
-------------------------------------------
'''
dadoscopy = dados.copy()
del dadoscopy['Fusca']
print(dadoscopy)
'''
-------------------------------------------
        pop(key,caso nao encontre colocar a mensagem com '')
-------------------------------------------
'''

dadoscopy.pop('Passat','chave  não encontrada')
print(dadoscopy)
'''
-------------------------------------------
        clear()
-------------------------------------------
'''
dadoscopy.clear()
print(dadoscopy)


'''
-------------------------------------------
      ITERANDO EM DICIONÁRIOS
-------------------------------------------
'''
dados = {'Crossfox': 72832.16, 'DS5': 124549.07,  'Fusca': 150000,  'Jetta Variant': 88078.64,  'Passat': 106161.95}

'''
-------------------------------------------
      keys()
-------------------------------------------
'''
for key in dados.keys():
    print(dados[key])
    

'''
-------------------------------------------
        valeus()
-------------------------------------------
'''
print(dados.values())

'''
-------------------------------------------
        items()
-------------------------------------------
'''
dados.items()