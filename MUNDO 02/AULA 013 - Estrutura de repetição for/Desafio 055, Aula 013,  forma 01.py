''' Desafio 055, forma 01, Faça um programa que leia o peso de cinco pessoas, no final, mostre qual foi o maior e o menor peso lidos.  '''

num = int(0)
list = []
for c in range(1,6):
    num = int(input('Digite o peso da {}º pessoa: '.format(c)))
    list = list + [num]


print('o maior peso é: {} KG'.format(max(list)))
print('o menor peso é: {} KG'.format(min(list)))
