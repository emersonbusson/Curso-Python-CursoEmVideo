# Desafio 055 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

# Utilizando o método max e min e listas.
peso = 0
lista_pesos = []
for cont in range(1,6):
    peso = int(input(f'Digite o peso da {cont}º pessoa: '))
    lista_pesos = lista_pesos + [peso]

print(f'O maior peso é: {max(lista_pesos)} Kg')
print(f'O menor peso é: {min(lista_pesos)} Kg')
