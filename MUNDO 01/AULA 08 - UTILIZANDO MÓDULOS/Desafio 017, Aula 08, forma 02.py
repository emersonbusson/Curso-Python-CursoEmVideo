# Desafio 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
# Sem a utilização de módulos.

cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do tato adjacente: '))
hipotenusa = (cateto_oposto **2 + cateto_adjacente **2) **(1/2)
print(f'A hipotenusa vai medir: {hipotenusa:.2f}')