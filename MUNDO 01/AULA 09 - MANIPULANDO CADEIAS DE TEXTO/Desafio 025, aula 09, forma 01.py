# Desafio 025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem 'silva' no nome.

nome = str(input('Digite seu nome completo:')).upper().strip()
print('Seu nome completo é {}, tem "silva" no nome?: {} '.format(nome, 'SILVA' in nome))