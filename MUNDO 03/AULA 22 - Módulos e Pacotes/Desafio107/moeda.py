'''Modulo Moeda, Desafio 107.'''

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

