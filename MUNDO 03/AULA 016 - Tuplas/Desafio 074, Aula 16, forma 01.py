'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

import random

valores = (random.randint(0,10),random.randint(0,10),random.randint(0,10), random.randint(0,10),random.randint(0,10))
print(f'Os valores sorteados foram: {valores}')
print(f'O maior valor sorteado é: {max(valores)}')
print(f'O menor valor sorteado é:  {min(valores)}')