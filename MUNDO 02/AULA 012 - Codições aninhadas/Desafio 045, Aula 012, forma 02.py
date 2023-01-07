# Desafio 045 - Crie um programa que faça o computador jogar Jokenpô com você.
#Forma 02

import time
import random

itens = ('PEDRA', 'PAPEL', 'TESOURA')
jogada_computador = random.randint(0,2)

jogada_player = int(input('''
Faça sua jogada!
[ 0 ] PEDRA                              
[ 1 ] PAPEL
[ 2 ] TESOURA
Digite a sua opção: '''))

if jogada_player != 0 and jogada_player != 1 and jogada_player !=2:
    print('Opção incorreta, tente novamente uma das seguintes opções: [0, 1, 2]')

else:
    print('-=' * 15)
    print(f'Computador jogou: {itens[jogada_computador]}')
    print(f'Jogador Jogou: {itens[jogada_player]}')
    print('-=' * 15)

if jogada_computador == 0: # Computador jogou: PEDRA
    if jogada_player == 0:
        print('EMPATE!!!')
    elif jogada_player == 1:
        print('JOGADOR VENCEU!!')
    elif jogada_player == 2:
        print('COMPUTADOR VENCEU!!')

elif jogada_computador == 1: # Computador jogou: PAPEL
    if jogada_player == 0:
        print('COMPUTADOR VENCEU!!')
    elif jogada_player == 1:
        print('EMPATE!!')
    elif jogada_player == 2:
        print('JOGADOR VENCEU!!')

elif jogada_computador == 2: # Computador jogou: TESOURA
    if jogada_player == 0:
        print('JOGADOR VENCEU!!')
    elif jogada_player == 1:
        print('COMPUTADOR VENCEU!!')
    elif jogada_player == 2:
        print('EMPATE!!')