''' Crie um programa que simule o funcionamento de um caixa eletrônico.
No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas
de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.'''
#forma guanabara.
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$: '))
total = valor
ced = 50
cont = 0
while True:
    if total >= ced:
        total = total - ced
        cont = cont + 1
    else:
        if cont > 0:
            print('O total de {} cédulas de R$ {}.'.format(cont, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cont = 0
        if total == 0:
            print('{:=^30}'.format(' Saque Finalizado '))
            break


