# Desafio 028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador, o programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time


print('{:=^80}'.format(" Acabei de pensar em um número entre 0 e 5, tente adivinhar! " ))

escolha_do_usuario = int(input('Em que número eu pensei?: '))
pensamento_do_computador = (random.randrange(0,5))

print('PROCESSANDO...')
time.sleep(1.5)
if pensamento_do_computador == escolha_do_usuario:
    print('Parabéns, você acertou, eu pensei no número: {}'.format(pensamento_do_computador))
else:
    print('Você errou, eu pensei no número: {}'.format(pensamento_do_computador))
