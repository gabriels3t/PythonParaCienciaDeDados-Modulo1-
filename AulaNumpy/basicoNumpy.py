import numpy as np

dados = [ 
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]

#array do numpy
np.arange(10)

km = np.array([1000,2300,4500,1500])
print(km.dtype)
km = np.loadtxt(fname='data/carros-km.txt',dtype = int)
acessorios = np.array(dados)
#shape mostra dimensoes, exemplo linhas e colunas 
print(km.shape)
print(acessorios.shape)






