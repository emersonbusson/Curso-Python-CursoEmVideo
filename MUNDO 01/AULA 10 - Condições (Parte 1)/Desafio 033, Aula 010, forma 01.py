'''FAÇA UM PROGRAMA QUE LEIA 3 NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR.'''

valor1 = float(input('Digite o Primeiro Valor:'))
valor2 = float(input('Digite o Segundo  Valor:'))
valor3 = float(input('Digite o Terceiro Valor:'))

lista = [valor1, valor2, valor3]

print('O Menor Valor Digitado Foi: {}'.format(min(lista)))
print('O Maior Valor Digitado Foi: {}'.format(max(lista)))