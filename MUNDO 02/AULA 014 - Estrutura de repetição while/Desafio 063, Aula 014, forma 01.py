''' Desafio 063, Aula 014, forma 01, Escrava um programa que
leia um número n inteiro qualquer e mostre na tela os n primeiros
elementos de uma sequência de fibonacci.'''
# EX: 0 > 1 > 1 > 2 > 3 > 5 > 8
print('-=' *20)
print('Sequencia de Fibonacci')
print('-=' *20)
n = int(input('Quantos termos você quer mostrar? '))
anterior = 0
proximo = 0
c = 0
while c != n:
    print('{} > '.format(proximo),end='')
    proximo = proximo + anterior
    anterior = proximo - anterior
    c = c + 1
    if proximo == 0:
        proximo = proximo + 1
print('Fim')