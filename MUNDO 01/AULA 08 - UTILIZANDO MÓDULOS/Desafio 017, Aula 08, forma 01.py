# Desafio 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

# Forma utilizando o módulos math e chamando somente a função da raiz quadrada sqrt().

from math import sqrt
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do tato adjacente: '))
soma_catetos = cateto_oposto **2 + cateto_adjacente **2
hipotenusa = sqrt(soma_catetos)
print('O valor da Hipotenusa é: {:.2f}'.format(hipotenusa))
