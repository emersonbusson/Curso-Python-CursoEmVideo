# Desafio 023 - #faça um programa que leia de 0 a 9999 e mostre na tela cada um dos dígitos separados por: unidade, dezena, centena, milhar.

numero = int(input('Digite o numero desejado:'))
print('Analisando o número digitado')
unidade = numero//1% 10
dezena = numero//10% 10
Centena = numero//100% 10
milhar = numero//1000% 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('milhar: {}'.format(m))

