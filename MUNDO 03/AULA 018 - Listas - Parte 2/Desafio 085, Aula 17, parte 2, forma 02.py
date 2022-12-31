''' Crie um programa onde o usuário possa digitar sete valores e cadastreos em uma lista única que mantenha separados os valores,
pares e impares. no final, mostre os valores pares e impares em ordem crescente. '''
#forma guanabara.

num = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'Todos os valores: {sorted(num)}')
print(f'Os valores pares digitados: {sorted(num[0])}')
print(f'OS valores impares digitados: {sorted(num[1])}')