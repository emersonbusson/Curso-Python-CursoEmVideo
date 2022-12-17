''' Crie um programa que simule o funcionamento de um caixa eletrônico.
No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas
de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.'''
#forma comentario youtube.


valor_saque = int(input('Digite o valor do saque R$:  '))
print('='*40)
for nota in [50, 20, 10, 1]:
    quantidade_notas = valor_saque // nota
    valor_saque = valor_saque % nota
    if quantidade_notas > 0:
        print(f'Sacado:\33[31m {quantidade_notas}\33[m Cédulas de R$ {nota}.')
