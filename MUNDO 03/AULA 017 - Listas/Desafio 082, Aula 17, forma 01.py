'''  Crie um programa que vai ler vários números e colocar em uma lista, depois crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

print('-='* 10,'\33[31mColetor de PAres e IMpares\33[m','-='* 10)
pares = []
impares = []
todos = []
while True:
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        pares.append(num)
        todos.append(num)
    else:
        impares.append(num)
        todos.append(num)
    resp = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    while resp  not in 'SsNn':
        resp = str(input('Opção inválida, Deseja continuar? [S/N]: ')).strip()[0]
    if resp in 'nN':
        break
print(f'A lista completa é: {todos}')
print(f'A Lista de PAres:{pares}.')
print(f'A lista de IMpares:{impares}.')


