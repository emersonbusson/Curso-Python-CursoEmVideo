'''Aprimore o desafio 086, mostrando no final:
a) a soma de todos os valores pares digitados
b) a soma dos valores da terceira coula
c) o maior valor da segunda linha '''
# minha forma com o código do Guanabara.
soma = 0
matriz = [[[0], [0], [0]], [[0], [0], [0]], [[0], [0], [0]]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor: para [{l},{c}]:  '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print()
print(f'A soma dos valores pares é: {soma}.')
valores = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna é: {valores}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}.')