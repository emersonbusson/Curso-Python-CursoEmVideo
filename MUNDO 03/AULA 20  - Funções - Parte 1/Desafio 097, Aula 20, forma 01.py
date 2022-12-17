''' Desafio 097, Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com o tamanho adaptável.'''

def escreva(msg):
    num = len(msg) + 6
    print('~' * num)
    print(f'{msg:^{num}}')
    print('~' * num)

    # entre a def(função) e o programa principal, tem que ter duas linhas vazias.
    # programa principal
escreva(str(input('\33[31mDigite uma frase: \33[m')))
escreva(str(input('\33[31mDigite uma frase: \33[m')))
escreva(str(input('\33[31mDigite uma frase: \33[m')))

