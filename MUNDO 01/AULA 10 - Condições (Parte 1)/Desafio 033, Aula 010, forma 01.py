# Desafio 034 - Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.
# Utilizando listas e as funções min() e max().

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo  valor: '))
valor3 = float(input('Digite o terceiro valor: '))

lista = [valor1, valor2, valor3]

print('O Menor Valor Digitado Foi: {}'.format(min(lista)))
print('O Maior Valor Digitado Foi: {}'.format(max(lista)))