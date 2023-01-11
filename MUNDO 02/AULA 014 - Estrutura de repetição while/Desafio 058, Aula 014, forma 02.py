# Desafio 058 - Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
# Forma 02

from random import randint

jogada_computador = randint(0,10)
print('Sou seu computador... acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

acertou = False
tentativas = 0

while not acertou:
    jogada_player = int(input('Qual é o seu paupite? '))
    tentativas += 1
    if jogada_player == jogada_computador:
        acertou = True
    else:
        if jogada_player < jogada_computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')

print(f'Acertou com o total de {tentativas} tentativas, eu pensei no número {jogada_computador}, parabéns.')