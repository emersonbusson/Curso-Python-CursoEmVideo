#Desafio 109, forma 01
'''Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro
a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
desenvolvida no Desafio 108. '''


def metade(valor=0,moeda=False):
    if moeda == True:
        resultado = valor / 2
        p = f'R${resultado:5.2f}'
        p = p.replace('.', ',')
        return p
    else:
        resultado = valor / 2
        return resultado


def dobro(valor=0,moeda=False):
    if moeda == True:
        resultado = valor * 2
        p = f'R${resultado:5.2f}'
        p = p.replace('.', ',')
        return p
    else:
        resultado = valor * 2
        return resultado


def aumentar(valor=0, porcento=10, moeda=False):
    if moeda == True:
        temp = valor * porcento
        valor += temp / 100
        p = f'R${valor:5.2f}'
        p = p.replace('.',',')
        return p
    else:
        temp = valor * porcento
        valor += temp / 100
        return valor


def dininuir(valor=0, porcento=10, moeda=False):
    if moeda == True:
        temp = valor * porcento
        valor -= temp / 100
        p = f'R${valor:5.2f}'
        p = p.replace('.', ',')
        return p
    else:
        temp = valor * porcento
        valor -= temp / 100
        return valor



def moeda(p):
    p = f'R${p:5.2f}'
    p = p.replace('.', ',')
    return p
