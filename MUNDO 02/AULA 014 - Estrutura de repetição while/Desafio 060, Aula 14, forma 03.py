'''Faça um programa que leia um número qualquer e mostre o seu fatorial'''
# utilizando a estrutura For
n = int(input('Digite um número para calcular seu Factorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end=' ')
for c in range(n,0,-1):
#while c > 0:
    print('{}'.format(c), end=' ')
    print('X' if c > 1 else ' = ', end= ' ')
    f *= c
    c -= 1
print('{}'.format(f))