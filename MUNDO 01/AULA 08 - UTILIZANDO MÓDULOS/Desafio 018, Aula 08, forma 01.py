#Desafio 018 - Faça um programa que leia um angulo qualquer e mostre na tela os valores do seno, cosseno e tangente.

import math

angulo = float(input('Digite um angulo qualquer: '))
angulo_radiano = math.radians(angulo)
seno = math.sin(angulo_radiano)
cosseno = math.cos(angulo_radiano)
tangente = math.tan(angulo_radiano)


print('O Ângulo de: {:.1f}° , tem o SENO de: {:.2f}'.format(angulo, seno))
print('O Ângulo de: {:.1f}° , tem o COSSENO de: {:.2f}'.format(angulo,cosseno))
print('O Ângulo de: {:.1f}° , tem a TANGENTE de: {:.2f}'.format(angulo,tangente))