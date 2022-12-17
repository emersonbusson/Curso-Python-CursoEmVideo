''' Crie um programa que simule o funcionamento de um caixa eletrônico.
No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas
de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.'''
#forma comentario youtube.

valor = int(input('Informe o valor a ser sacado: '))
print('-=' *30)
nota50 = valor //50
print(f'Notas de R$50 = \33[31m{nota50}\33[m.')
valor %= 50
print(f'\33[35mSacando resto: R$ \33[33m{valor}\33[m.')
print('-=' *30)
nota20 = valor //20
print(f'Notas de R$20 = \33[31m{nota20}\33[m.')
valor %= 20
print(f'\33[35mSacando resto: R$ \33[33m{valor}\33[m.')
print('-=' *30)
nota10 = valor //10
print(f'Notas de R$10 = \33[31m{nota10}\33[m.')
valor %= 10
print(f'\33[35mSacando resto: R$ \33[33m{valor}\33[m.')
print('-=' *30)
nota1 = valor // 1
print(f'Notas de R$1 = \33[31m{nota1}\33[m.')
valor %= 1
print(f'\33[34mResto: R$ \33[33m{valor}\33[m.')
print('-=' *30)
print(f'Notas de R$50 = \33[31m{nota50}\33[m.')
print(f'Notas de R$20 = \33[31m{nota20}\33[m.')
print(f'Notas de R$10 = \33[31m{nota10}\33[m.')
print(f'Notas de R$1 = \33[31m{nota1}\33[m.')
print(f'Valor de saque solicitado zerado: \33[33m{valor}\33[m.')