#Desafio 011 - Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e quantidade de tinta necessária para pinta-ló, sabendo que cada litro de tinta pinta uma área de 2m2.

largura_parede = float(input('Digite a largura da parede em metros: '))
altura_parede = float(input('Digite a altura da parede em metros: '))
area_parede = largura_parede * altura_parede
print('A sua parede tem a dimensão de {} X {} e a sua área é de: {}m²'.format(largura_parede,altura_parede,altura_parede))
print('Você vai precisar de {} litros de tinta para pintar essa parede!'.format(altura_parede / 2))
