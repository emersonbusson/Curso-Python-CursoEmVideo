'''Faça um mini-sistema que utilize o interactive help do python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'Fim', o programa se encerrará.
Obs: use cores.
'''
import sys
from io import StringIO


def escreva(titulo='DIGITE A MENSAGEM'):
        lendetitulo = len(titulo) + 6
        texto = '\33[42m~'
        print(f'{texto}' * lendetitulo)
        print(f'{titulo:^{lendetitulo}}')
        print(f'{texto}' * lendetitulo,'\n\33[m',end='')


def ajuda(comando=''):
     mostrar = str(help(comando))

     return repr(mostrar)

while True:
    escreva('Sistema de AJUDA PyHelp')
    opção = str(input('Função ou Biblioteca >')).strip().lower()
    if opção == 'fim':
        escreva('ATÉ LOGO')
        break
    escreva(f'Acessando o manual do comando "{opção}"')
    sys.stdout = texto = StringIO()
    help(opção)
    sys.stdout = sys.__stdout__
    texto = texto.getvalue()
    texto = f'\33[31m{texto}\33[m'
    print(texto)