# Desafio 019 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos, faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

aluno_1 = str(input('Digite o nome do primeiro aluno: '))
aluno_2 = str(input('Digite o nome do segundo aluno: '))
aluno_3 = str(input('Digite o nome do terceiro aluno: '))
aluno_4 = str(input('Digite o nome do quarto aluno: '))
lista_sorteio = [aluno_1,aluno_2,aluno_3,aluno_4]
sorteados = random.sample(lista_sorteio,len(lista_sorteio))

for indice, aluno in enumerate(sorteados):
    print('O a ordem de apresentação é: {}° - {} '.format(indice + 1, aluno))