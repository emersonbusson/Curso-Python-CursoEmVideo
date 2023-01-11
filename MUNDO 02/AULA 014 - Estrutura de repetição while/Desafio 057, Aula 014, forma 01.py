# Desafio 057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite seu sexo: [M/F]: ')).upper().strip()[0] # [0] vai pegar somente a primeira letra do indice.
while sexo not in 'MF':
    sexo = str(input('Opção incorreta, digite a opção correta [M/F]: ')).upper().strip()[0]
print(f'Sexo: [{sexo}], registrado com sucesso...')
