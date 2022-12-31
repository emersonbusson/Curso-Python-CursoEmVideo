''' Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista, no final mostre:
#Quantas Pessoas foram cadastradas.
#Uma listam com as pessoas mais pesadas
#uma listagem com as pessoas mais leves. '''
todos = list()
temp = list()
cont = 0
while True:
    temp.append(str(input(f'Digite o nome da {cont+1}º pessoa: ')))
    temp.append(float(input('Digite seu peso: ')))
    if len(todos) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    todos.append(temp[:])
    temp.clear() #apaga 'nome' e 'peso' a cada laço depois de adicionado na lista todos.
    cont += 1
    r = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if r == 'N':
        break
print('-=' *30)

#print(f'Os dados cadastrados foram: {todos}.')
print(f'Ao todo, você Cadastrou {len(todos)} pessoas. ')

print(f'O maior peso foi de {mai}kg. Peso de: ', end='')
for p in todos:
    if p[1] == mai:
        print(f' [{p[0]}]', end='')
print()

print(f'O menor peso foi de {men}kg. Peso de: ', end='')
for p in todos:
    if p[1] == men:
        print(f' [{p[0]}]',end='')
print()


