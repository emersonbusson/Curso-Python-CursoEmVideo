'''Crie um programa que faça o computador jogar jokenpô com você. '''
import random
import time
print('{:=^40}'.format('JOKENPO'))

opção_jogador = int(input('''\33[31mFaça sua jogada!
                  [ 0 ] PEDRA                              
                  [ 1 ] PAPEL
                  [ 2 ] TESAOURA
                  Digite a sua opção: 
                  \33[m'''))
pedra = 0
papel = 1
tesoura = 2
lista = [ pedra, papel, tesoura]
escolha_computador = random.choice(sorted(lista))

print('\33[34m-=\33[m' * 30)
time.sleep(1)
print('\33[31mJO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
print('\33[34m-=\33[m' * 30)

if opção_jogador == 0:
    print('\33[33mJogador Escolheu: PEDRA.')
    if escolha_computador == 0:
        print('Computador Escolheu: PEDRA')
        print('EMPATE!!')
    elif escolha_computador == 1:
        print('Computador Escolheu: PAPEL')
        print('Computador Venceu!!')
    else:
        print('Computador Escolheu: TESOURA')
        print('Jogador Venceu!!')
elif opção_jogador == 1:
    print('\33[35mJogador Escolheu: PAPEL')
    if escolha_computador == 0:
        print('Computador Escolheu: PEDRA')
        print('Jogador Venceu!!')
    elif escolha_computador == 1:
        print('Computador Escolheu: PAPEL')
        print('EMPATE!!')
    else:
        print('Computador Escolheu: TESOURA')
        print('Computador Venceu!!')
elif opção_jogador == 2:
    print('\33[32mJogador Escolheu TESOURA')
    if escolha_computador == 0:
        print('Computador Escolheu: PEDRA')
        print('Computador Venceu!!')
    elif escolha_computador == 1:
        print('Computador Escolheu: PAPEL')
        print('Jogador Venceu!!')
    else:
        print('Computador Escolheu: TESOURA')
        print('EMPATE!!')
else:
    print('\33[7mEscolha a Opção Correta >> (0, 1, 2) ...')


