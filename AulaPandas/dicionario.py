carros = ['Jetta Variant', 'Passat', 'Crossfox']
valores = [88078.64, 106161.94, 72832.16]

#print(carros.index('Passat'))
#print(valores[carros.index('Passat')])

#dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
#print(dados)
dados = dict(zip(carros,valores))
print(dados)
