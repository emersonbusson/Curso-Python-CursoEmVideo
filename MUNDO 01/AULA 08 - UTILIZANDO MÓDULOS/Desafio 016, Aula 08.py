# Crie um programa que leia um número real qualquer e mostre na tela sua porção inteira.

#Forma 01

from math import  trunc
num = float(input('Digite um número:'))
result = trunc(num)
print('O número: {}, tem a parte inteira: {}.'.format(num, trunc(result)))

