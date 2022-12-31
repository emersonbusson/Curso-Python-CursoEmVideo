'''Faça um programa que leia 5 valores númericos e guardeos dentro de uma lista.
No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista'''
from time import sleep
valores_5 = list()
for num in range(0,5):
    valores_5.append(int(input(f'Digite {num +1}º valor: ')))
print('Todos os valores foram lidos, aguarde...')
sleep(1)
print('==' *30)
print(f'O maior valor é: \33[31m{max(valores_5)}\33[m e está no indice: \33[33m{valores_5.index(max(valores_5))}\33[m')
print(f'O menor valor é: \33[31m{min(valores_5)}\33[m e está no indice: \33[33m{valores_5.index(min(valores_5))}\33[m')




