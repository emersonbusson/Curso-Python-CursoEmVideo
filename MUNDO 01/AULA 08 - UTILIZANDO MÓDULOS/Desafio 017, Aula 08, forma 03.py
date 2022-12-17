'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, caulcule e mostre o comprimento da hipotenusa'''


import math
co = float(input('Digite o cateto oposto:'))
ca = float(input('Digite o cateto adjacente:'))
hi = math.hypot(co,ca)
print('visto que o cateto oposto é: {}, e o cateto adjacete é: {}, então a hipotenusa é: {:.2f}'.format(co,ca,hi))