# Desafio 024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'santo'.

nome_cidade = str(input('Digite o nome da cidade: ')).strip().upper()
print('Analisando...')
print('O nome da Cidade digitada é: {}, o nome "santo" existe? {}'.format(nome_cidade, 'SANTO' in nome_cidade))