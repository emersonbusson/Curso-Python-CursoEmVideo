''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas, no final do programa, mostre, a média de dade do grupo
qual é o nome do homem mais velho, quantas mulheres tem menos de 20 anos '''

media_idade = int(0)
soma_idade = int(0)
idade_homemvelho = int(0)
homemvelho_nome = str()
totalmulher20 = int(0)
for p in range(1,5):
    print(' ____ {}° PESSOA ____ '.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        idade_homemvelho = idade
        nome_homemvelho = nome
    if sexo in 'Mm' and idade > idade_homemvelho:
        idade_homemvelho = idade
        nome_homemvelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1

media_idade = soma_idade / 4
print('A média de idade de grupo é: {}.'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(idade_homemvelho,nome_homemvelho))
print('Quantitativo de mulheres com menos de 20 anos: {}.'.format(totalmulher20))