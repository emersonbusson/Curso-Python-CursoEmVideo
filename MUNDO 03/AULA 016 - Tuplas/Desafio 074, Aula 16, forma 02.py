'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

#forma guanabara.

from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram:', end= ' ')
for n in numeros:
    print(f'{n} ',end='')
print(f'\nO maior valor sorteado: {max(numeros)}.')
print(f'O menor valor sorteado: {min(numeros)}.')