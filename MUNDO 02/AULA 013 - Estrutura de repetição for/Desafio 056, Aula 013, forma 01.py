# Desafio 056 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

idade_grupo_media  = 0

homem_mais_velho = dict()

mulheres_menor20 = 0
for cont in range(1,5):

    print(f' ____ {}° PESSOA ____ '.format(cont))

    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('SEXO [M/F]: ')).strip()[0]
    print()

    idade_grupo_media += idade
    
    if cont == 1 and sexo in 'Mm':
        homem_mais_velho["nome"] = nome
        homem_mais_velho["idade"] = idade

    if sexo in 'Mm' and idade > homem_mais_velho['idade']:
        homem_mais_velho["nome"] = nome
        homem_mais_velho["idade"] = idade

    if sexo in 'Ff' and idade < 20:
        mulheres_menor20 += 1

idade_grupo_media  = idade_grupo_media / 4

print(f'A média de idade de grupo é: {idade_grupo_media}')

print(f'O homem mais velho tem {homem_mais_velho["idade"]} anos e se chama {homem_mais_velho["nome"]}.')

print(f'O Quantitativo de mulheres com menos de 20 anos: {mulheres_menor20}.')