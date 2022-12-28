# Desafio 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
aluno_1 =str(input('Digite o nome do Primeiro Aluno: '))
aluno_2 =str(input('Digite o nome do Segundo Aluno: '))
aluno_3 =str(input('Digite o nome do Terceiro Aluno: '))
aluno_4 =str(input('Digite o nome do Quarto Aluno: '))
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
print('O aluno escolhido foi: {}.'.format(random.choice(sorted(lista))))