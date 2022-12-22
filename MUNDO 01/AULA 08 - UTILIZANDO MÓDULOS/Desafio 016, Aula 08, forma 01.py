# Desafio 16 ~ Crie um programa que leia um número real qualquer e mostre na tela sua porção inteira.

from math import  trunc
num = float(input('Digite um número:'))
result = trunc(num)
print('O número real: {}, tem a parte inteira: {}.'.format(num, trunc(result)))