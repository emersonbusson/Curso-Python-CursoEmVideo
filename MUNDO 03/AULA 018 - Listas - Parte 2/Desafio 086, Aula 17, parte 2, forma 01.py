''' Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final mostre a matriz na tela, com a formatação correta. '''

matriz = [[[], [], []], [[], [], []], [[], [], []]]
for i, e in enumerate(matriz[0]):
    matriz[0][i].append(int(input(f'Digite um valor para [0,{i}]: ')))
for i, e in enumerate(matriz[1]):
    matriz[1][i].append(int(input(f'Digite um valor para [1,{i}]: ')))
for i, e in enumerate(matriz[2]):
    matriz[2][i].append(int(input(f'Digite um valor para [2,{i}]: ')))
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



