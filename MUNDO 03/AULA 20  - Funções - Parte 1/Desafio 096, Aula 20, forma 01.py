'''Desafio 096, Aula 20, forma 01, Faça um programa que tenha uma função chamada aréa(),
que receba as dimensões de um terreno rentangular(largura e comprimento) e mostre a aréa do terreno.'''


def area(l, c):
    print()
    print(f'{"Controle de Terrenos":^41}')
    print('-' * 41)
    print()
    a = l * c #aréa      > LAGURA * COMPRIMENTO = ARÉA
    print(f'A Aréa do terreno é {l:.1f} X {c:.1f} é de {a:.1f}m²')


area(l=float(input('LARGURA (m): ')),c= float(input('COMPRIMENTO (m): ')))