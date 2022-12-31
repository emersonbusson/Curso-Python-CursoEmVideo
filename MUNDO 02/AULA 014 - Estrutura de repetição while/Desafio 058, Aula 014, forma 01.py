''' Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''


import random
import time
cont = 1
print('--===--' * 20)
print('Acabei de pensar em um número entre 0 e 10')
print('--===--' * 20)

print('Será que você consegue adivinhar qual foi?')
userpensado = int(input('Em que número eu pensei?'))
computador = (random.randrange(0,10))

print('PROCESSANDO...')
time.sleep(3)
while computador != userpensado:
    cont += 1
    if userpensado > computador:
        print('Menos... Tente Mais uma vez.')
        userpensado = int(input('Qual é seu paupite? '))
    else:
        print('Mais... Tente mais uma vez.')
        userpensado = int(input('Qual é seu paupite? '))

else:
    print('Você acertou, eu pensei no número: {}'.format(computador))

print('parabéns você acertou depois de {} tentativas'.format(cont))