'''Desafio 098, Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim, passo.
e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1.
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada.'''
def contagem (i,f,p,msg=''):
    # if msg == True:
    #     print('Agora é sua vez de personalizar a contagem!')
    import time
    print('-=' * 20)
    print(f'Contagem de {abs(i)} até {abs(f)} de {abs(p)} em {abs(p)}')
    if p <= 0:
        for num in range(i,f-1,p):
            time.sleep(0.5)
            print(num, end=' ')
        print(' FIM!')
        print('-=' * 20)
    else:
        for num in range(i,f+1,p):
            time.sleep(0.5)
            print(num, end=' ')
        print(' FIM!')
#duas linhas do principal
#duas linhas do principal
contagem(1,11-1,1)
contagem(10,0,-2)
# contagem(msg=True,i=int(input('Inicio: ')),
#          f=int(input('Fim: ')),
#          p=int(input('Passo: ')))
print('Agora é sua vez de personalizar a contagem!')
contagem(i=int(input('Inicio: ')),
         f=int(input('Fim: ')),
         p=int(input('Passo: ')))
