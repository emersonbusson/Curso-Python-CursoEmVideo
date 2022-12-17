'''Aprimore o desafio 086, mostrando no final:
a) a soma de todos os valores pares digitados
b) a soma dos valores da terceira coula
c) o maior valor da segunda linha '''
soma = 0
matriz = [[[], [], []], [[], [], []], [[], [], []]]
for i, e in enumerate(matriz[0]):
    temp = int(input(f'Digite um valor para [0,{i}]: '))
    if temp % 2 == 0:
        soma += temp
    matriz[0][i].append(temp)
for i, e in enumerate(matriz[1]):
    temp = int(input(f'Digite um valor para [1,{i}]: '))
    if temp % 2 == 0:
        soma += temp
    matriz[1][i].append(temp)
for i, e in enumerate(matriz[2]):
    temp = int(input(f'Digite um valor para [2,{i}]: '))
    if temp % 2 == 0:
        soma += temp
    matriz[2][i].append(temp)
print('-=' * 30)
for e in matriz[0]:
    print(f' {e} ',end=' ')
print()
for e in matriz[1]:
    print(f' {e} ',end=' ')
print()
for e in matriz[2]:
    print(f' {e} ',end=' ')
print()
print('-=' *30)
print(f'A soma dos valores pares é: {soma}')
print(f'A soma dos valores da terceira coluna é: {sum(matriz[0][2] + matriz[1][2] + matriz[2][2])}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')