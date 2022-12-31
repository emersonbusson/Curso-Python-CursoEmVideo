''' Desafio 097, Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com o tamanho adaptável.'''
#forma Guanabara.

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)



# programa principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('Cev')