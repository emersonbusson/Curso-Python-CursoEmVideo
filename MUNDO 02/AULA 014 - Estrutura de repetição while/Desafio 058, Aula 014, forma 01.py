# Desafio 058 - Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
import time
cont = 1

print('{:=^80}'.format(" Acabei de pensar em um número entre 0 e 10, tente adivinhar! "))

escolha_do_usuario = int(input('Em que número eu pensei? '))
pensamento_do_computador = (random.randrange(0,10))

print('PROCESSANDO...')
time.sleep(0.5)
while pensamento_do_computador != escolha_do_usuario:
    cont += 1
    if escolha_do_usuario > pensamento_do_computador:
        print('Menos... Tente mais uma vez.')
        escolha_do_usuario = int(input('Qual é seu novo paupite? '))
    else:
        print('Mais... Tente mais uma vez.')
        escolha_do_usuario = int(input('Qual é seu novo paupite? '))

else:
    print(f'Você acertou, eu pensei no número: {pensamento_do_computador}')

print(f'Parabéns você acertou depois de {cont} tentativas')