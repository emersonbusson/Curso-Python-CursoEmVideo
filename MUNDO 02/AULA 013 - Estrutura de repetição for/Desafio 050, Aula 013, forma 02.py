''' Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares, se o valor digitado for impar, desconsidereo '''

soma = 0
for c in range(1,7):
        print('\33[35m-=\33[m' * 30)
        numero = int(input(f'\33[31mDigite o {c}° número: \33[m'))
        if numero % 2 == 0:
            soma += numero
print(soma)