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
    todos.append(temp[:])
    temp.clear() #apaga 'nome' e 'peso' a cada laço depois de adicionado na lista todos.
    cont += 1
    r = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if r == 'N':
        break
print('\33[31m-=' *30)
print(todos)
print('\33[31m-=\33[m' *30)
maior = max(todos, key=lambda x: x[1]) #aqui você determina o ('X' ou segundo iteravel do max) como indice do nome na lista.
menor = min(todos, key=lambda x: x[1] )
print(f'O {maior[0]} tem o maior peso: {maior[1]} kg.')
print(f'O {menor[0]} tem o menor peso: {menor[1]} kg.')
