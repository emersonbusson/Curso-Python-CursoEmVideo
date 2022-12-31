'''Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A Média de idade do grupo.
C) Uma lista com todas as mulheres.
d) uma lista com todas as pessoas com idade acima da média. '''
# forma guanabara.

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! por favor, Digite apenas "M" ou "F".')
    pessoa['idade'] = int(input('idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro!, Digite apenas "S" ou "N".')
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram:', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}')
print('Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    for k, v in p.items():
        print(f'{k} = {v};', end='  ')
    print()
    print()
print('<< ENCERRADO >>')








