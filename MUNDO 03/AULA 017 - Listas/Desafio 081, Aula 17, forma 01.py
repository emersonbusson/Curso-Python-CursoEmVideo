''' Crie um programa que vai ler vários número e colocar em uma lista
depois disso, mostre:
# quantos números foram digitados.
# A lista de válores ordenada de forma crescente.
#Se o valor 5 foi digitado ou está ou não na lista.  '''

lista = []
vdc = ['S','N']
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    r = str(input('Você deseja continuar? [S/N]')).strip().upper()[0]
    while r not in vdc:
        print('Opção incorreta, tente novamente..')
        r = str(input('Você deseja continuar? [S/N]')).strip().upper()[0]
    if r == vdc[0]:
        print('Continuando..')
    elif r == vdc[1]:
        print('Finalizando..')
        break
print(f'Você digitou o total de {len(lista)} elementos. ')
print(f'Os valores em ordem decescente são: {sorted(lista,reverse=True)}')
if 5 in lista:
    print(f'O valor: 5, foi encontrado na lista na posição: {lista.index(5)}')
else:
    print(f'O valor 5, não foi encontrado na lista :((')
