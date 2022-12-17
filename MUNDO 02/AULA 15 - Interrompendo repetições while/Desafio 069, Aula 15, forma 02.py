''' Crie um programa que leia a idade e o sexo de várias pessoas. a cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar, no final mostre:
A) qunatas pessoas tem mais de 18 anos. ok
B) quantos homens foram cadastrados. ok
C) quantas mulheres tem menos de 20 anos. '''
# forma guanabara

tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO: [M/F] ')).upper().strip()[0]
    if idade > 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('==' * 30)
print(f'# Total de pessoas com mais de 18 anos: {tot18}.')
print(f'# Ao todo temos {totH} homens cadastrados.')
print(f'# Temos {totM20} mulheres com menos de 20 anos.')

