'''Faça um programa que leia nome e média de um aluno, guardando também a situação
em um dicionario. no final, mostre o conteúdo da estrutura na tela '''

pessoa = dict()
pessoa['nome'] = str(input('Nome: ')).upper()
pessoa['media'] = float(input(f"Média de {pessoa['nome']}: "))
if pessoa['media'] >= 7:
    pessoa['situação'] = 'Aprovado.'
elif 5 <= pessoa['media'] < 7:
    pessoa['situação'] = 'Recuperação.'
else:
    pessoa['situação'] = 'Reprovado.'

print(f"O nome é igual a {pessoa['nome']}.")
print(f"A Média é igual a {pessoa['media']}.")
print(f"A situação é igual a {pessoa['situação']}")
