# Desafio 050 -  Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for cont in range(6):
    print('-=' * 15)
    numero = int(input(f'Digite o {cont+1}º número inteiro: '))
    if numero % 2 == 0 and numero != 0:
        soma += numero
print(f'A soma dos números pares digitados é: {soma}')