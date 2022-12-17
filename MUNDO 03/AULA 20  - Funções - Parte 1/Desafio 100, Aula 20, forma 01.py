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


def somapares_impares(impares=False, pares=False):
    global geral     #recebe o valor gerado pela outra função.
    numeros = geral
    soma = 0
    desisão = str(input('[i] SOMA IMPARES E [P] PARA SOMA PARES: ')).strip().upper()[0]
    while desisão not in 'IP':
        desisão = str(input('[i] SOMA IMPARES E [P] PARA SOMA PARES: ')).strip().upper()[0]
    if desisão == 'I':
        impares = True
    if desisão == 'P':
        pares = True
    if impares == True:
        print(f'\33[33mValores impares: \33[m', end='')
        for e in numeros:
            if e % 2 == 1:
                soma += e
                print(f'\33[31m{e}\33[m', end=' ')
        print()
        print(f'Somando os valores impares de {geral}, temos: {soma}.')
    if pares == True:
        print(f'\33[35mValores pares: \33[m',end='')
        for e in numeros:
            if e % 2 == 0:
                soma += e
                print(f'\33[31m{e}\33[m',end=' ')
        print()
        print(f'Somando os valores pares de {geral}, temos: {soma}.')

#programa principal
sorteia()
somapares_impares()