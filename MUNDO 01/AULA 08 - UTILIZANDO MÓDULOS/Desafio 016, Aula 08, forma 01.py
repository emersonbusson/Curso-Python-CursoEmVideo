#Desafio 016 - forma 01 - Crie um programa que leia um número real qualquer e mostre na tela sua porção inteira.
from math import trunc
numero_real = float(input('Digite um número real:'))
numero_inteiro = trunc(numero_real)
print('O número real digitado: {}, tem a parte inteira: {}'.format(numero_real, numero_inteiro))