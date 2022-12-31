''' Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares, se o valor digitado for impar, desconsidereo'''
cont = 0
soma = 0
for c in range(0,6):
        cont += 1
        print('\33[31m-=\33[m' * 30)
        numero = int(input(f'Digite o {cont}º número inteiro: '))
        if numero % 2 == 0 and numero != 0:
            soma += numero
print(soma)


