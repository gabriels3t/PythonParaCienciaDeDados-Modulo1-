nomes_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5'])
#print(nomes_carros)


'''
------------------------------
        SELEÇÃO EM TUPLAS
------------------------------
'''

#print(nomes_carros[1:-1])

#nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5', ('Fusca', 'Gol', 'C4'))
#print(nomes_carros[-1][1])

'''
------------------------------
        ITERANDO EM TUPLAS
------------------------------
'''
carro_1, carro_2, carro_3, carro_4 = nomes_carros
#print(carro_1)
#print(carro_2)
#print(carro_3)
#print(carro_4)

_, a, _, b = nomes_carros
#print(a)
#print(b)

_ , c, *_ = nomes_carros
#print(c)
'''
------------------------------
        Função zip
------------------------------
'''
carros = ['Jetta Variant', 'Passat', 'Crossfox', 'DS5']

valores = [88078.64, 106161.94, 72832.16, 124549.07]
#print(list(zip(carros,valores)))

for carro, valor in zip(carros, valores):
    if valor > 100000:
        print(carro, valor)

