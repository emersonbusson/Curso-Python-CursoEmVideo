'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogaor e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogaor, mesmo que algum dado não tenha sido informado
corretamente.'''
#comentario youtube.

def ficha (nome='', gol=''):
    if nome == '':
        nome = '<DESCONHECIDO>'
    if not gol.isdigit():
        gol = 0
    print(f'O jogaor {nome} fez {gol} gols no campeonato')


#programa principal
nome = input('Nome do jogaor: ').strip().title()
gol = input('Nº de Gols: ')

ficha(nome,gol)

