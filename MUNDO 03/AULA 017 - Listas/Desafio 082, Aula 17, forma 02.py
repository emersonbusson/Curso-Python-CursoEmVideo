'''  Crie um programa que vai ler vários números e colocar em uma lista, depois crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

print('-='* 10,'\33[31mColetor de PAres e IMpares\33[m','-='* 10)
pares = []
impares = []
lista = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    resp = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if resp in 'Nn':
        break
for e in lista:
    if e % 2 == 0:
        pares.append(e)
    else:
        impares.append(e)
print(f'A lista com todos os elementos: {lista}.')
print(f'A lista com todos os elementos impares: {impares}')
print(f'A lista com todos os elementos pares: {pares}')

