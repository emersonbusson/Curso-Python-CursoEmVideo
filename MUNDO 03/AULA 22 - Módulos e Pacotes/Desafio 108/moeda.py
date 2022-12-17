#desafio 108
'''Adapte o código do desafio 107, criando uma função adicional chamada moeda()
que consiga mostrar os valores como um valor monetário formatado.'''

def metade(valor=0):
    resultado = valor / 2
    return resultado

def dobro(valor=0):
    resultado = valor * 2
    return resultado

def aumentar(valor=0, porcento=10):
    temp = valor * porcento
    valor += temp / 100
    return valor

def dininuir(valor=0, porcento=10):
    temp = valor * porcento
    valor -= temp / 100
    return valor


# def moeda(p):
#     return f'R${p:5.2f}'

def moeda(p):
    p = f'R${p:5.2f}'
    p = p.replace('.',',')
    return p

# #forma guanabara.
# def moeda(preço=0, moeda='R$'):
#     return f'{moeda}{preço:>8.2f}'.replace('.',',')