# Desafio 023 - #faça um programa que leia de 0 a 9999 e mostre na tela cada um dos dígitos separados por: unidade, dezena, centena, milhar.

# forma 02 - utilizando indices.

numero = int(input('Informe um número: '))
print('Analisando o Nùmero: {} '.format(numero))
numero = str(numero)
print('Unidade: {}'.format(numero[3]))
print('Dezena: {}'.format(numero[2]))
print('Centena: {}'.format(numero[1]))
print('Milhar: {}'.format(numero[0]))