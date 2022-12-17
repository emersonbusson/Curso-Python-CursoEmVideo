'''Faça um programa que leia nome e média de um aluno, guardando também a situação
em um dicionario. no final, mostre o conteúdo da estrutura na tela '''
#forma Guanarabara.
aluno = dict()
aluno["nome"] = str(input('Nome: ')).upper()
aluno["média"] = float(input(f'Média de {aluno["nome"]}: '))
if aluno["média"] >= 7:
    aluno["situação"] = 'Aprovado.'
elif 5 <= aluno["média"] < 7:
    aluno["situação"] = 'Recuperação.'
else:
    aluno["situação"] = 'Reprovado.'
for k, v in aluno.items():
    print(f'- {k} é igual a {v} ')