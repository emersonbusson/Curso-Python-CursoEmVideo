'''Faça um mini-sistema que utilize o interactive help do python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'Fim', o programa se encerrará.
Obs: use cores.
'''
c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7m'       # 6 - branco
     );


#forma guanabara.
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', cor=4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


#programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', cor=2)
    comando = str(input("função ou biblioteca: "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', cor=1)