# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua aréa e quantidade de tinta nescessária para pinta-ló
# sabendo que cada litro de tinta pinta uma aréa de 2m2.

larg = float(input('Digite a largura da parede:'))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}X{} e Sua aréa pe de {}m²'.format(larg,alt,area))
print('Você vai precisar de {} litros de tinta para pintar essa parede!'.format(area / 2))
