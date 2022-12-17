''' Crie um programa onde o usuário possa digitar sete valores e cadastreos em uma lista única que mantenha separados os valores,
pares e impares. no final, mostre os valores pares e impares em ordem crescente. '''



pares_inpares = list()
pares = list()
impares = list()
for e in range(0,7):
    tempvalor = int(input(f'Digite o {e}º valor: '))
    if tempvalor % 2 == 0:
        pares.append(tempvalor)
    else:
        impares.append(tempvalor)
pares_inpares.append(pares)
pares_inpares.append(impares)
print(f'OS valores pares digitados foram: {sorted(pares_inpares[0])}.')
print(f'Os valores impares digitados foram: {sorted(pares_inpares[1])}')
