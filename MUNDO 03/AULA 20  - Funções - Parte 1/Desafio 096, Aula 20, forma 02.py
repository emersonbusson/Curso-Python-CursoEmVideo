'''Desafio 096, Aula 20, forma 01, Faça um programa que tenha uma função chamada aréa(),
que receba as dimensões de um terreno rentangular(largura e comprimento) e mostre a aréa do terreno.'''
# forma guanabara.

def area(larg, comp):
    a = larg * comp
    print(f'A aréa de um terreno {larg} X {comp} é de {a}m².')


# programa principal
print(' Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
