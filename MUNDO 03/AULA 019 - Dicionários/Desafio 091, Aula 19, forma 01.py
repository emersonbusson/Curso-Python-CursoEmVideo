''' Crie um programa onde 4 jogadores joguem um dado e tenham resultados aléatorios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionario em ordem,
sabendo que o vencedor tirou o maior número no dado. '''
import random
from time import sleep as tempo
c = 1
jogador = dict()
print('Valores Sorteados: ')
for j in range(0,4):
    jogador[f"Jogador{j+1}"] = random.randint(1,6)
for k,v in jogador.items():
    print(f'   O {k} tirou {v}')
    tempo(1)

print('Ranking dos jogadores:')
for i in sorted(jogador, key=jogador.get, reverse=True):
    print(f'   {c}º lugar: ', end='')
    print(f'{i} com {jogador[i]}')
    tempo(1)
    c += 1