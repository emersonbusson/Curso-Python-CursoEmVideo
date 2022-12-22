# Desafio 017 ~ Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, caucule e mostre o comprimento da hipotenusa.

from math import sqrt
cate_op = float(input('Digite o comprimento do cateto oposto:'))
cate_ad = float(input('Digite o comprimento do tato adjacente:'))
soma = cate_op **2 + cate_ad **2
hipo = sqrt(soma)
print('Visto que o Cateto Oposto é: {}, e o Cateto Adjacente é: {}, O valor da Hipotenusa é: {:.2f}'.format(cate_op, cate_ad,hipo))
