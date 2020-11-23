'''Entrada dos dados'''
Acessorios = [
    'Rodas de liga', 
    'Travas elétricas', 
    'Piloto automático',
    'Bancos de couro',
    'Ar condicionado'
]

'''
Manipulando os dados para a saida
'''
Acessorios.append('Airbag')
Acessorios.sort()
Acessorios.pop()
Acessorios.append('Vidros elétricos')
print(Acessorios)




'''
como deve ficar na saida


['Airbag',
 'Ar condicionado',
 'Bancos de couro',
 'Piloto automático',
 'Rodas de liga',
 'Vidros elétricos']
 '''