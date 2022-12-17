'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:'''
#   A vista dinheiro ou debito, 10% de desconto.
#   A vista no cartão: 5% de desconto.
# Em até 2x no cartão, preço normal.
# Em 3x ou mais no cartão, 20% de juros.

valor_produto = float(input('QUAL O VALOR DA COMPRA EM R$? '))
print('-=' * 30)

forma_pagamento = int(input('''          \33[31mDigite de 1 a 4, de acordo com a forma de pagamento desejada:\33[m
===================================================================================================================
                - [1] A vista dinheiro ou debito, 10% de desconto.
                - [2] A vista no cartão: 5% de desconto.
                - [3] Em até 2x no cartão, preço normal.
                - [4] Em 3x ou mais no cartão, 20% de juros.
                OPÇÃO: >>  '''))

print('-=' * 30)
if forma_pagamento == 1:
    print('Forma de pagamento escolhida: \33[32mA vista dinheiro ou debito, 10% de desconto.\33[m')
    print('\33[31m-=\33[m' * 30)
    print(f'O valor do produto é R$:{valor_produto}.')
    print('\33[32mCom 10% de desconto, fica R$:{:.2f}.\33[m'.format(valor_produto - (valor_produto * 10 /100)))

elif forma_pagamento == 2:
    print('Forma de pagamento escolhida: \33[32mA vista no cartão: 5% de desconto.\33[m')
    print('\33[31m-=\33[m' * 30)
    print(f'O valor do produto é R$:{valor_produto}.')
    print('\33[32mCom 05% de desconto, fica R$: {}'.format(valor_produto - (valor_produto *5 /100)))


elif forma_pagamento == 3:
    print('Forma de pagamento escolhida: \33[32mEm até 2x no cartão, preço normal.\33[m')
    print('\33[31m-=\33[m' * 30)
    print(f'\33[33mO valor do produto é R$:{valor_produto:.2f}, em até 2x no cartão, não tem desconto.\33[m')
    parcela = (valor_produto /2)
    print(f'\33[35mO valor parcelado em 2x é R$:{parcela:.2f}.\33[m')

elif forma_pagamento == 4:
    print('Forma de pagamento escolhida: \33[32mEm 3x ou mais no cartão, 20% de juros.\33[m')
    print(f'O valor do produto é R$:{valor_produto:.2f}.')
    total_parcelas = int(input('\33[31mDigite a Quantidade de parcelas: \33[m'))
    valor_com20juros = valor_produto + (valor_produto *20 /100)
    print(f'\33[35mQuantidade de parcelas x{total_parcelas}, valor das percelas \33[mR$:{valor_com20juros / total_parcelas:.2f}.\33[m')
    print('\33[7mCom 20% de juros, visto que está sendo parcelado em mais de 2x, o valor fica R$ {}\33[m'.format(valor_produto + (valor_produto *20 /100)))


else:
    print('ESCOLHA A OPÇÃO CORRETA...')