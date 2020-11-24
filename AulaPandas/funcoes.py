'''
----------------------------------------------
                BUILT-IN FUNCTIONS
----------------------------------------------
'''
dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
sum(dados.values())
'''
----------------------------------------------
            CRIANDO A PROPRIA FUNÇÃO
----------------------------------------------
'''
def media():
    valor =(1+2+3)/3
    print(valor)


def media(num_1, num_2, num_3):
    valor =(num_1 + num_2 + num_3)/3
    print(valor)


def media(lista):
    valor = sum(lista)/len(lista)
    return valor

resultado = media([1,2,3,4,5,6,7,8,])

def media(lista):
    valor = sum(lista)/len(lista)
    return (valor,len(lista))

resultado, n = media([1,2,3,4,5,6,7,8,])
print(resultado)
print(n)