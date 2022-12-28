# Desafio 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
# Utilizando o módulo math e chamando a função hypot.

import math
cateto_oposto = float(input('Digite o comprimento do cateto oposto:'))
cateto_adjacente = float(input('Digite o comprimento do tato adjacente:'))
print(f'O comprimento da hipotenusa é: {math.hypot(cateto_oposto, cateto_adjacente):.2f}')