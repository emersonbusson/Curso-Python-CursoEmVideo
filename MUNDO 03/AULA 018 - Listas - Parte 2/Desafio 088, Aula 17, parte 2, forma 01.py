''' Faça um programa que ajude um jogador da mega sena a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta. '''
from random import choices
from time import sleep
x = 0
jogoslista = []
print('--'*15)
print(f'{"JOGA NA MEGA SENA":^30}')
print('--'*15)
qtjogos = int(input('Quantos jogos você quer que eu sorteie?: '))
print(f'-=-=-= SORTEANDO {qtjogos} JOGOS -=-=-=')
for e in range(0,qtjogos):
    jogoslista.append(choices(range(1,60),k=6))
    x += 1
for i, d in enumerate(jogoslista):
    sleep(1)
    print(f'Jogo {i+1}: {jogoslista[i]} ')
print(f'-=-=-= < BOA SORTE > -=-=-=')
