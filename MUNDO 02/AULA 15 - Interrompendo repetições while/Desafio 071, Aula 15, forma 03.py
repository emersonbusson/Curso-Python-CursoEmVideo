''' Crie um programa que simule o funcionamento de um caixa eletrônico.
No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas
de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.'''
#forma comentario youtube.

valor = int(input('Quanto você quer sacar? R='))
lista1 = [valor // 50, (valor%50)//20, ((valor%50)%20)//10, ((valor%50)%20)%10]
lista2 = ['R$50','R$20','R$10','R$1']
for i in range(4):
    if (lista1[i] > 0):
        print('Total de {} cédulas de {}'.format(lista1[i], lista2[i]))
