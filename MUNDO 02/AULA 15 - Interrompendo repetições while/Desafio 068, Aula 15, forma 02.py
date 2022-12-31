'''Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador PERDER, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo. '''

# Forma Guanabara.
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou: {jogador} e o computador: {computador}. Total  deu: {total}. ', end=' ')
    print('= Deu Par' if total % 2 == 0 else '= Deu Impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!!.')
            v += 1
            print('Vamos jogar novamente...')
        else:
            print('Você PERDEU!!.')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!!.')
            v += 1
            print('Vamos jogar novamente...')
        else:
            print('Você PERDEU!!.')
            break
