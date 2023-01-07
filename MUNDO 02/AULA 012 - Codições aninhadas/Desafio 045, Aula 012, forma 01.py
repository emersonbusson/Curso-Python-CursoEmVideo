# Desafio 045 - Crie um programa que faça o computador jogar Jokenpô com você.

import random
import time

print(f'{" JOKENPO ":=^40}')

jogada_player = int(input('''
Faça sua jogada!
[ 0 ] PEDRA                              
[ 1 ] PAPEL
[ 2 ] TESOURA
Digite a sua opção: '''))

pedra = 0
papel = 1
tesoura = 2
lista = [pedra, papel, tesoura]
jogada_computador = random.choice(sorted(lista))

print('-=' * 15)
time.sleep(1)
print(f' {" JÔ ":^5} ')
time.sleep(1)
print(f'{" KEN ":^25}')
time.sleep(1)
print(f'{" PO ":^50}')1
print('-=' * 15)

if jogada_player == 0:
    print('Jogador Escolheu: PEDRA')
    if jogada_computador == 0:
        print('Computador Escolheu: PEDRA')
        print('EMPATE!!')
    elif jogada_computador == 1:
        print('Computador Escolheu: PAPEL')
        print('Computador Venceu!!')
    else:
        print('Computador Escolheu: TESOURA')
        print('Jogador Venceu!!')

elif jogada_player == 1:
    print('Jogador Escolheu: PAPEL')
    if jogada_computador == 0:
        print('Computador Escolheu: PEDRA')
        print('Jogador Venceu!!')
    elif jogada_computador == 1:
        print('Computador Escolheu: PAPEL')
        print('EMPATE!!')
    else:
        print('Computador Escolheu: TESOURA')
        print('Computador Venceu!!')
        
elif jogada_player == 2:
    print('Jogador Escolheu: TESOURA')
    if jogada_computador == 0:
        print('Computador Escolheu: PEDRA')
        print('Computador Venceu!!')
    elif jogada_computador == 1:
        print('Computador Escolheu: PAPEL')
        print('Jogador Venceu!!')
    else:
        print('Computador Escolheu: TESOURA')
        print('EMPATE!!')
else:
    print('Escolha a Opção Correta >> (0, 1, 2)...')