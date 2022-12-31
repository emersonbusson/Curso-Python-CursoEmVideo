'''Desafio 055, forma 02, Faça um programa que leia o peso de cinco pessoas, no final, mostre qual foi o maior e o menor peso lidos.'''
maior = 0
menor = 0


for c in  range(1,6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('maior peso é: {}'.format(maior))
print('menor peso é: {}'.format(menor))