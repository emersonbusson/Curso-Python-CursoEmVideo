# Desafio 030 - Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
import time


numero = int(input('Digite um número inteiro e te direis se ele é par ou ímpar: '))
time.sleep(0.5)
print('Processando...')

if (numero%2) == 0:
    print('O número: {}, é PAR.'.format(numero))
else:
    print('O número: {}, é ÍMPAR.'.format(numero))
