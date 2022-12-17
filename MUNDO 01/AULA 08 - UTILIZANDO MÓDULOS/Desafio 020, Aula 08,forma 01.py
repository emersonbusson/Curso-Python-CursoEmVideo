''' O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos, faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada '''
import random
aluno1 =str(input('Digite o nome do Primeiro Aluno: '))
aluno2 =str(input('Digite o nome do Segundo Aluno: '))
aluno3 =str(input('Digite o nome do Terceiro Aluno: '))
aluno4 =str(input('Digite o nome do Quarto Aluno: '))
lista = [aluno1, aluno2, aluno3, aluno3]
print('O aluno escolhido foi: {}:'.format(random.choice(sorted(lista))))