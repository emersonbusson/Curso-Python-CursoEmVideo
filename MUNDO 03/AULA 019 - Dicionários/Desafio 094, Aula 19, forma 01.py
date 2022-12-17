'''Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A Média de idade do grupo.
C) Uma lista com todas as mulheres.
d) uma lista com todas as pessoas com idade acima da média. '''
pessoa = dict()
grupo = list()
c = 0
somaidade = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    pessoa['idade'] = int(input('idade: '))
    somaidade += pessoa['idade']
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    grupo.append(pessoa.copy())
    c += 1
    if r == 'N':
        break
# print(grupo)
mediaidade = somaidade / c
print(f'- O grupo tem {c} pessoas.')
print(f'- A média de idade é de {mediaidade:.2f} anos.')
print(f'- As mulheres cadastradas foram: ',end='')
for e in grupo:
    if e['sexo'] == 'F':
        print(e['nome'],end=' ')
print()
print('- Lista de pessoas que estão acima da média: ')
print()
for p in grupo:
    if p['idade'] > mediaidade:
        for k, v in p.items():
            print(f'{k} = {v};',end='  ')
        print()
        print()
print('\33[31m<< ENCERRADO >> \33[m')
