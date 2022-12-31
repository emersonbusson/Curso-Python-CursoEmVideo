''' Crie um programa que leia a idade e o sexo de várias pessoas. a cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar, no final mostre:
A) qunatas pessoas tem mais de 18 anos. ok
B) quantos homens foram cadastrados. ok
C) quantas mulheres tem menos de 20 anos. '''
print('='*10,'ANALISADOR','=' * 10)
contm = total18 = contfmenos20 = 0
while True:
    idade = int(input('Digite Sua Idade: '))
    sexo = str(input('Digite seu Sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Incorreto, Tente Novamente [M/F]: ')).upper().strip()[0]
    print(f'Idade: {idade}. / Sexo: {sexo}. Registrado!')
    if idade > 18:
        total18 += 1
    if sexo == 'M':
        contm += 1
    else:
        if idade < 20:
            contfmenos20 += 1
    print('=' *40)
    escolha = str(input('DESEJA CONTINUAR A CADASTRAR? [S/N]: ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('- - Escolha uma opção Válida [S/N]: ')).strip().upper()[0]
    if escolha == 'S':
            print('-- CONTINUANDO PARA NOVO CADASTRO --')
    else:
        break
print('----Programa Encerrado----')

print(f'Total de pessoas com mais de 18 anos: {total18}.')
print(f'Total de homens cadastrados: {contm}')
print(f'Total de mulheres com menos de 20 anos: {contfmenos20}.')