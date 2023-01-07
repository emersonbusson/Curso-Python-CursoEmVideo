# Desafio 044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

valor_produto = float(input('Qual o valor da compra em R$: '))

print()
print(f"{' Digite de 1 a 4, de acordo com a forma de pagamento desejada ':=^70}")
print()

forma_pagamento = int(input('''
- [1] A vista dinheiro ou debito, 10% de desconto
- [2] A vista no cartão: 5% de desconto
- [3] Em até 2x no cartão, preço normal
- [4] Em 3x ou mais no cartão, 20% de juros

OPÇÃO: '''))

if forma_pagamento == 1:
    print('Forma de pagamento escolhida: A vista dinheiro ou debito, 10% de desconto.')
    print(f'O valor do produto é R$: {valor_produto:.2f}')
    print(f'Com 10% de desconto, fica R$: {valor_produto - (valor_produto * 10 /100):.2f}')
elif forma_pagamento == 2:
    print('Forma de pagamento escolhida: A vista no cartão: 5% de desconto.')
    print(f'O valor do produto é R$: {valor_produto:.2f}')
    print(f'Com 05% de desconto, fica R$: {valor_produto - (valor_produto *5 /100)}')
elif forma_pagamento == 3:
    print('Forma de pagamento escolhida: Em até 2x no cartão, preço normal.')
    print(f'O valor do produto é R$: {valor_produto:.2f} , em até 2x no cartão, não tem desconto.')
    parcela = (valor_produto /2)
    print(f'O valor parcelado em 2x é R$: {parcela:.2f}')
elif forma_pagamento == 4:
    print('Forma de pagamento escolhida: Em 3x ou mais no cartão, 20% de juros.')
    print(f'O valor do produto é R$: {valor_produto:.2f}.')
    total_parcelas = int(input('Digite a Quantidade de parcelas: '))
    if total_parcelas < 2:
        print('Forma de pagamento escolhida: A vista no cartão: 5% de desconto.')
        print(f'O valor do produto é R$: {valor_produto:.2f}')
        print(f'Com 05% de desconto, fica R$: {valor_produto - (valor_produto *5 /100):.2f}')
    elif total_parcelas == 2:
        print('Forma de pagamento escolhida: Em até 2x no cartão, preço normal.')
        print(f'O valor do produto é R$: {valor_produto:.2f} , em até 2x no cartão, não tem desconto.')
        parcela = (valor_produto /2)
        print(f'O valor parcelado em 2x é R$: {parcela:.2f}')
    else:   
        valor_com20juros = valor_produto + (valor_produto *20 /100)
        print(f'Com 20% de juros, visto que está sendo parcelado em mais de 2x, o valor fica R$ {valor_produto + (valor_produto *20 /100):.2f}')
        print(f'Quantidade de parcelas x{total_parcelas}, valor das percelas R$: {valor_com20juros / total_parcelas:.2f}')
else:
    print('ESCOLHA A OPÇÃO CORRETA...')