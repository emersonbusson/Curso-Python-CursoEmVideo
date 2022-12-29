# Desafio 027 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome_completo = str(input('Digite seu nome completo:')).upper().strip()
nome_separado = nome_completo.split()
print('O primeiro nome é: {}'.format(nome_separado[0]))
print('O último nome é: {}.'.format(nome_separado[len(nome_separado)-1]))