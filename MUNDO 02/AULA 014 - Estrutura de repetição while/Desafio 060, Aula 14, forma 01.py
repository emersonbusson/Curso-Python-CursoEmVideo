#Desafio 060 - Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Utilizando o módulo math
import math
numero = int(input('Digite um número para calcular seu factorial: '))

resultado = math.factorial(numero)

print('O fatorial de {} é {}.'.format(numero, resultado))
