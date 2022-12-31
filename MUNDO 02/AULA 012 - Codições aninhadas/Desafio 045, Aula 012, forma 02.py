'''Crie um programa que faça o computador jogar jokenpô com você. '''
import time
import random
itens = ('PEDRA', 'PAPEL', 'TESOURA')
jogada_computador = random.randint( 0,2)

opção_jogador = int(input('''
Faça sua jogada!
                  [ 0 ] PEDRA                              
                  [ 1 ] PAPEL
                  [ 2 ] TESOURA
                  Digite a sua opção: '''))

if opção_jogador != 0 and opção_jogador != 1 and opção_jogador !=2:
    print('OPÇÃO INCORRETA, TENTE NOVAMENTE UMAS DAS SEGUITES (OPÇÕES: 1, 2, 3')

else:
    print(('_' * 39))

    print(f'Computador jogou: {itens[jogada_computador]}')
    print(('_' * 39))
    print(f'Jogador Jogou: {itens[opção_jogador]}')
    print(('_' * 39))

if jogada_computador == 0: # Computador jogou: PEDRA
    if opção_jogador == 0:
        print('EMPATE!!!')
    elif opção_jogador == 1:
        print('JOGADOR VENCEU!!')
    elif opção_jogador == 2:
        print('COMPUTADOR VENCEU!!')

elif jogada_computador == 1: # Computador jogou: PAPEL
    if opção_jogador == 0:
        print('COMPUTADOR VENCEU!!')
    elif opção_jogador == 1:
        print('EMPATE!!')
    elif opção_jogador == 2:
        print('JOGADOR VENCEU!!')

elif jogada_computador == 2: # Computador jogou: TESOURA
    if opção_jogador == 0:
        print('JOGADOR VENCEU!!')
    elif opção_jogador == 1:
        print('COMPUTADOR VENCEU!!')
    elif opção_jogador == 2:
        print('EMPATE!!')