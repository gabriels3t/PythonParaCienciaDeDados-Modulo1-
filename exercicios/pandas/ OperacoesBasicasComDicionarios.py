dados = {
    'Passat': {
        'ano': 2012,
        'km': 50000,
        'valor': 75000,
        'acessorios': ['Airbag', 'ABS']
    }, 
    'Crossfox': {
        'ano': 2015,
        'km': 35000,
        'valor': 25000
    }
}

print('acessorios' in dados['Crossfox'])
print('acessorios' in dados['Passat'])
print(dados['Crossfox']['valor'])
print(dados['Passat']['acessorios'][-1])