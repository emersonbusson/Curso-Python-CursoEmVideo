#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, caucule e mostre o comprimento da hipotenusa.

from math import sqrt
catep = float(input('Digite o comprimento do cateto oposto:'))
catead = float(input('Digite o comprimento do tato adjacente:'))
soma = catep **2 + catead **2
hipo = sqrt(soma)
print('Visto que o cateto Oposto é {}, e o cateto Adjacente é: {}, O valor da Hipotenusa é {:.2f}'.format(catep, catead,hipo))
