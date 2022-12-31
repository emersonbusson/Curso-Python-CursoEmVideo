'''  Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta
No final, mostre um boletim contendo a média de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente '''
biglist = []
pessoa = []
r = ''
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    pessoa.append(nome)
    pessoa.append(nota1)
    pessoa.append(nota2)
    biglist.append(pessoa[:])
    pessoa.clear()
    r = str(input('Quer continuar? [S/N]'))[0].strip().upper()
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]'))[0].strip().upper()
    if r == 'N':
        break
print('-=' *30)
print(f'{"Nº":<10}{"NOME":<10}{"MÉDIA":<10}')
print('--' *15)
for i, e in enumerate(biglist):
    print(f'{i:<10}{biglist[i][0]:<15}{(biglist[i][1] + biglist[i][2]) / 2:<10}')
print('--' *15)
mostrar = ()
while True:
    mostrar = int(input('Mostrar notas de qual Aluno? (999 interrompe): '))
    if mostrar == 999:
        break
    print(f'Notas de {biglist[mostrar][0]} São: {biglist[mostrar][1:3]}')
    # if mostrar == 999:
    #     break
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')