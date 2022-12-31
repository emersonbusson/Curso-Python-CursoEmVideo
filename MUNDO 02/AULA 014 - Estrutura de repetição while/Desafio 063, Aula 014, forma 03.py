''' Desafio 063, Aula 014, forma 03, Escrava um programa que
leia um número n inteiro qualquer e mostre na tela os n primeiros
elementos de uma sequência de fibonacci.'''
# EX: 0 > 1 > 1 > 2 > 3 > 5 > 8
# DE UM USUARIO DO YOUTUBE .

Nant = 1
Fibonacci = 0

n = int(input('Digite um número:(Este vai ser o nº de elementos da sequência) '))

while n != 0:
    print('{}'.format(Fibonacci), end=' → ')
    Fibonacci = Fibonacci + Nant
    Nant = Fibonacci - Nant
    n -= 1
print('FIM')
