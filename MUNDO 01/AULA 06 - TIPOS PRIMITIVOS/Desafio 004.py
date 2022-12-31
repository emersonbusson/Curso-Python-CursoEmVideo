# Desafio 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

entrada_dados = input('Digite algo para ter todas as informações possiveis sobre: ')
print(f'O tipo primitivo desse valor é: {type(entrada_dados)}')
print(f'é númerico? {entrada_dados.isdigit()}')
print(f'é alfanumérico? {entrada_dados.isalpha()}')
print(f'Tem estapços em branco: {entrada_dados.isspace()}')
print(f'Está em MAIÚSCULO: {entrada_dados.isupper()} ')
print(f'Está em minúsculo:{entrada_dados.islower()}')
print(f'Está capitalizada: {entrada_dados.istitle()}')