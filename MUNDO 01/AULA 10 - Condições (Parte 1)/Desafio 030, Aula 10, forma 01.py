'''Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.'''
import time



print('____' *20)
numero = int(input('Digite um número inteiro e te direis se ele é par ou ímpar:'))
print('____' *20)
time.sleep(2)
print('Processando...')

print('____'*20)

if (numero%2) == 0:
    print('O número: {}, é PAR.'.format(numero))
else:
    print('O número: {}, é ÍMPAR.'.format(numero))
