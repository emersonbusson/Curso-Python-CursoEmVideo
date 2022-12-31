from lib.interface import *
from lib.arqv import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):              #if arquivoExiste(arq):
    criarArquivo(arq)                       #print('Arquivo encontrado com sucesso!')
                                        #else:
                                            #print('Arquivo Não encontrado!')'''

while True:
    cabeçalho('MENU PRINCIPAL')
    resposta = menu(['VER PESSOAS CADASTRADAS','CADASTRAR NOVA PESSOA', 'SAIR DO SISTEMA'])
    if resposta == 1:
        #opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\33[31mERRO! Digite uma Opção válida!\33[m')
    sleep(2)

