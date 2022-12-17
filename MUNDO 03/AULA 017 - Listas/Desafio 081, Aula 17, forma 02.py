''' Crie um programa que vai ler vários número e colocar em uma lista
depois disso, mostre:
# quantos números foram digitados.
# A lista de válores ordenada de forma crescente.
#Se o valor 5 foi digitado ou está ou não na lista.  '''
#forma guanabara.
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Você quer continuar? [S/N].')).strip()[0]
    if resp in 'Nn':
        break
print('-=' *30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrecente são {valores}.')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')