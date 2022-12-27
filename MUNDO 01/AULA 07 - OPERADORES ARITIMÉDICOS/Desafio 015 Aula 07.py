#Desafio 015 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 dia e R$ 0,15 por km rodado.

dias_alugados = int(input('Qual a quantidade de dias pelo qual o carro foi alugado?: '))
km_percorrido = float(input('Qual a [Km]quilometragem foi percorrida pelo carro?: '))
valor_diarias = dias_alugados * 60
valor_km = km_percorrido * 0.15
preco_pagar = valor_diarias + valor_km
print(f'O valor a pagar por {dias_alugados} diarias R$: {valor_diarias:6.2f}')
print(f'O valor a pagar por {int(km_percorrido)} Km R$: {valor_km:6.2f}')
print(f'Valor final a pagar R$: {preco_pagar:6.2f}')