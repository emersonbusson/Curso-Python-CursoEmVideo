'''Faça um programa que leia um número qualquer e mostre o seu fatorial'''
import math
n = int(input('Digite um número para calcular seu factorial: '))

resultado = math.factorial(n)

print('O fatorial de {} é {}.'.format(n, resultado))
