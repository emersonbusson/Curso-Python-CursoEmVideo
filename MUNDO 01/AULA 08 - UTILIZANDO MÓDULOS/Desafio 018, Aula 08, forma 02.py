#Desafio 018 - Faça um programa que leia um angulo qualquer e mostre na tela os valores do seno, cosseno e tangente.

from math import radians, sin, cos, tan

angulo = float(input('Digite o Ângulo Desejado: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O Ângulo de: {angulo:.2f}, tem o SENO de: {seno:.2f}')
print(f'O Ângulo de: {angulo:.2f}, tem o COSSENO de: {cosseno:.2f}')
print(f'O Ângulo de: {angulo:.2f}, tem a TANGENTE de: {tangente:.2f}')
