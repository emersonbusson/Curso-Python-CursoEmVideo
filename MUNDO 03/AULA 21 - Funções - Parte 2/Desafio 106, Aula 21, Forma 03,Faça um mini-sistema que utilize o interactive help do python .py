'''Faça um mini-sistema que utilize o interactive help do python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'Fim', o programa se encerrará.
Obs: use cores.
'''

from time import sleep
import sys
from io import StringIO

def escreva(titulo='DIGITE A MENSAGEM', exibir=False, color=1):
    if exibir == True:
        cores = dict()
        cores["RED"] = '\33[41m'
        cores["GREEN"] = '\33[42m'
        cores["REVERSE"] = '\33[7m'
        cores["BLUE"] = '\33[44m'
        if color == 1:
            color = cores["RED"]
        elif color == 2:
            color = cores["GREEN"]
        elif color == 3:
            color = cores["BLUE"]
        elif color == 4:
            color = cores["REVERSE"]
        lendetitulo = len(titulo) + 6
        print(f'{color}~' * lendetitulo)
        print(f'{titulo:^{lendetitulo}}')
        print(f'~' * lendetitulo,'\n\33[m',end='')

    else:
        lendetitulo = len(titulo) + 6
        print(f'~' * lendetitulo)
        print(f'{titulo:^{lendetitulo}}')
        print(f'~\33[m' * lendetitulo)


while True:
    escreva('Sistema de AJUDA PyHelp', exibir=True, color=2)

    opção = str(input('\33[mFunção ou Biblioteca >')).strip().lower()

    if opção == 'fim':
        escreva('ATÉ LOGO', exibir=True, color=1)
        break
    escreva(f'Acessando o manual do comando "{opção}"', exibir=True, color=3)
    sys.stdout = texto = StringIO()
    help(opção)
    sys.stdout = sys.__stdout__
    texto = texto.getvalue()
    texto = f'\33[7m{texto}'
    sleep(1)
    print(f'{texto}',end='\33[m')