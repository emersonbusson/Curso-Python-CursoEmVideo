'''Desafio 098, Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim, passo.
e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1.
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada.'''
#forma guanabara.
print('-=' * 20)
def contador(i,f,p):
    from time import sleep
    # print(f'Contagem de {i} até {f} de {p} e {p}')
    if i < f:
        print(f'Contagem de {i} até {f} de {p} e {p}')
        i = 0
        while i < f:
            i += p
            sleep(0.5)
            print(f' {i} ', end='')
    else:
        print(f'Contagem de {i} até {f} de {p} eM {p}')
        while i >= f:
                # i -= p # colocar esse código antes, vai ficar parecendo 11 em vez de 10.
                sleep(0.5)
                print(f' {i} ', end='')
                i -= p
    print(f'FIM!',end='')
    print()
    print('-=' * 20)

contador(1,10,1)
contador(10,1,1)
print('Agora é sua vez de personalizar sua contagem')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print('-=' * 20)
contador(i,f,p)

