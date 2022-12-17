'''Desafio 098, Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim, passo.
e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1.
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada.'''
#forma guanabara.
from time import  sleep

def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True) # flush = True, não vai ligar o buffet de tela, mais informações sobre o fluash > https://pt.stackoverflow.com/questions/291779/o-que-%C3%A9-o-par%C3%A2metro-flush-da-fun%C3%A7%C3%A3o-print
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True) #
            sleep(0.5)
            cont -= p
        print('FIM!')


# programa principal
contador(0,100,10)
contador(10,0,2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('FIM: '))
pas = int(input('Passo: '))
contador(ini,fim,pas)