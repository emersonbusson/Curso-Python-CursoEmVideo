# Desafio 019 ~ O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos, faça um programa que leia o nome dos quarto alunos e mostre a ordem sorteada.
import random
a1 = str(input('Digite o nome do primeiro aluno:'))
a2 = str(input('Digite o nome do segundo aluno:'))
a3 = str(input('Digite o nome do terceiro aluno:'))
a4 = str(input('Digite o nome do quarto aluno:'))
lista = [a1,a2,a3,a4]
lista = random.sample(lista,len(lista))
print('A lista sequencial de alunos sorteados é: {} '.format(lista))