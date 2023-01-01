# Desafio 033 - Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.
# Utilizando if

valor1 = float(input('Digite o primeiro valor:'))
valor2 = float(input('Digite o segundo valor:'))
valor3 = float(input('Digite o terceiro valor:'))

menor = valor1

if valor2 < valor1 and valor2 < valor3:
    menor = valor2
if valor3 < valor1 and valor3 < valor2:
    menor = valor3

maior = valor1

if valor2 > valor1 and valor2 > valor3:
    maior = valor2
if valor3 > valor1 and valor3 > valor2:
    maior = valor3

print('O Menor Valor é {}.'.format(menor))
print('O Maior Valor é {}'.format(maior))
