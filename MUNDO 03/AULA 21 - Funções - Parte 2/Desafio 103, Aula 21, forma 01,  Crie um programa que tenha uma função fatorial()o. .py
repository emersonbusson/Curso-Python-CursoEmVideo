'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogaor e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogaor, mesmo que algum dado não tenha sido informado
corretamente.'''
# forma guanabara.

def ficha(jogador='<Desconhecido>', gol=0):
    print(f'O jogador {jogador} fez {gol} gol(s) no campeonato.')



n = str(input('Nome do jogador: '))
g = str(input('Numero de Gols: ')) # string pode ser vazia, número inteiro e float não.
if g.isdigit(): # se não for númerico, vai para o else e g recebe 0.
    g = int(g) # se for número g vai receber uma conversão de 'g' de 'str' para 'int'.
else:
    g = 0
if n.strip() == '': # se tirado todos os espaços e ficou vazio, a função vai receber o parametro opcional 'desconhecido', e a função recebe somente a quantidade de gols em 'g', como parametro.
    ficha(gol=g)
else:
    ficha(n,g) #se não tiver vazio, vai receber o 'g' e o 'n'.

