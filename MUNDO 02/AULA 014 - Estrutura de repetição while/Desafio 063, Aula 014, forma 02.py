''' Desafio 063, Aula 014, forma 02, Escrava um programa que
leia um número n inteiro qualquer e mostre na tela os n primeiros
elementos de uma sequência de fibonacci.'''
# EX: 0 > 1 > 1 > 2 > 3 > 5 > 8
# Froam Guanabara.
print('--' *30)
print('Sequência de fibonacci'.upper())
print('--' *30)
n = int(input('Quantos termos você quer mostrar?: '))
print('--' *30)
t1 = 0
t2 = 1
print('\33[31m{} \n{}\33[m'.format(t1, t2))
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('\33[35m{} X {} = \33[31m{}\33[m'.format(t2, t1, t3))
    t1 = t2
    t2 = t3
    cont += 1
print('--' *30)
print('\33[33mFoi mostrado a quantidade de \33[31m{}\33[33m termos\33[m'.format(cont - 1))
