'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o úsuario tentar descobrir qual foi o número escolhido pelo computador'''

'''O programa deverá escrever na tela se o úsuario venceu ou perdeu.'''

import random
import time

print('--===--' * 20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
print('--===--' * 20)
userpensado = int(input('Em que número eu pensei?'))
computador = (random.randrange(0,5))
print('PROCESSANDO...')
time.sleep(3)
if computador == userpensado:
    print('Parabéns, você acertou, eu pensei no número: {}'.format(computador))
else:
    print('Ganhei, eu pensei no número: {}'.format(computador))



