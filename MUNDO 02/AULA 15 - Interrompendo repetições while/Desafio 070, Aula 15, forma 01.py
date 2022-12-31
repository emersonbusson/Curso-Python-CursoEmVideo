'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. no final mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.'''
print( '-=' *10,'LOJÃO BIDU', '=-' *10)
cont1 = 1
cont2 = cont3 = soma = 0
maior = menor = 0
nome_menor = ' '
nome_maior = ' '
while True:
    nome = str(input(f'Nome do {cont1}° produto: ')).strip()
    preço = float(input(f'Digite o valor do {cont1}° produto R$: '))
    soma += preço
    cont1 += 1
    cont3 += 1
    if preço > 1000:
        cont2 += 1
    if cont3 == 1:
        maior = preço
        menor = preço
        nome_menor = nome
        nome_maior = nome
    else:
        if preço > maior:
            maior = preço
            nome_maior = nome
        if preço < menor:
            menor = preço
            nome_menor = nome
    escolha = str(input('Você deseja continuar? [S/N]: ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Opção inválida, escolha uma opção válida! [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break
    print('--' * 66)
print('\33[34m--\33[m' * 66)
print(' -- PROGRAMA FINALIZADO --')
print('--' *66)
print(f'\33[31mO TOTAL DE PRODUTOS COMPRADOS: {cont3}.\33[m')
print('--' *66)
print(f'\33[35mA SOMA DO VALOR DE TODOS OS PRODUTOS É R$:{soma:.2f}.\33[m')
print('--' *66)
print(f'\33[33mQUATIDADE DE PRODUTOS QUE CUSTAM MAIS DE MIL R$: {cont2}. \33[m')
print('--' *66)
print(f'\33[36mO NOME DO PRODUTO MAIS BARATO É: ({nome_menor}), VALOR: R$: {menor:.2f}.\33[m')
print('--' *66)
print(f'\33[32mO NOME DO PRODUTO MAIS CARO É: ({nome_maior}), VALOR: R$: {maior:.2f}.\33[m')
print('--' *66)
