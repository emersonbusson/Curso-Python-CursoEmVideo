'''Faça um programa que leia 5 valores númericos e guardeos dentro de uma lista.
No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista'''
#Forma Guanabara.
listanum = []
maior = 0
menor = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('=-' *30)
print(f'Você digitou os valores: {listanum}.')
print('=-' *30)
print(f'O maior valor digitado foi: {maior}, na posição: ',end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print() # quebra a linha do "( end=' ')"
print(f'O menor valor digitiado foi: {menor}. na posição: ',end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...',end='')
print()
