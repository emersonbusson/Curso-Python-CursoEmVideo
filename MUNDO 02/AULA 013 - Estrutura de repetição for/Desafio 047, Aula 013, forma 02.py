'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50'''

lista = [0]
for n in range(1, 51):
    print('.', end= ' ') # cada pontinho vai indicar quantas vezes ele fez o laço. foram feitos dois laços nesse exemplo.
    if n % 2 == 0:
        print(n, end=' ')
print('ACABOU')