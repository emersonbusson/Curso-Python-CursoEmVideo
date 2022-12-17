'''Desafio 100, Aula 20, forma 01, Faça um programa que tenha uma lista chamada números e duas funções chamadas:  sorteia() e somapar().
A primeira deve sortear 5 números e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior. '''
# forma guanabara.
from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')


def somarpar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}. ')


numeros = list()
sorteia(numeros)
somarpar(numeros)
