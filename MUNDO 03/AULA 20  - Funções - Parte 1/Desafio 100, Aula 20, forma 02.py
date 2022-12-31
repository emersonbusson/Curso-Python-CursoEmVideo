'''Desafio 100, Aula 20, forma 01, Faça um programa que tenha uma lista chamada números e duas funções chamadas:  sorteia() e somapar().
A primeira deve sortear 5 números e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior. '''
geral = 0


def sorteia (quant=5):
    global geral
    from random import randint
    numeros = list()
    while True:
        numeros.append(randint(0, 10))
        if len(numeros) == quant:
            break
    print(f'Sorteando {len(numeros)} valores da lista:', end=' ')
    for valor in numeros:
        print(f'{valor}', end=' ')
    geral = numeros

    print('PRONTO!')


def somapares():
    global geral     #recebe o valor gerado pela outra função.
    numeros = geral
    soma = 0
    for e in numeros:
        if e % 2 == 0:
            soma += e
    print(f'Somando os valores pares de {geral}, temos: {soma}.')


#programa principal
sorteia()
somapares()