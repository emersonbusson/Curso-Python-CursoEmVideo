# Desafio 055 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
# Forma 2, utilizando o bloco if.

maior_peso = 0
menor_peso = 0

for cont in  range(1,6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(cont)))
    if cont == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso: #Poderia ser elif aqui
            maior_peso = peso
        if peso < menor_peso: #Poderia ser elif aqui também
            menor_peso = peso


print('O maior peso é: {}'.format(maior_peso))
print('O menor peso é: {}'.format(menor_peso))