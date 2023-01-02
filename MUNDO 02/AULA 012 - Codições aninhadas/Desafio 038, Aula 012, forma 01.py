# Desafio 038 - Escreva um programa que leia dois números inteiros e compare-os, exibindo uma mensagem indicando qual é o maior ou, caso os dois sejam iguais, informando que não existe um valor maior.

primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))

if primeiro_valor > segundo_valor:
    print('O primeiro valor é maior, valor digitado: {}.'.format(primeiro_valor))
elif segundo_valor > primeiro_valor:
    print('O segundo valor é maior, valor digitado: {}.'.format(segundo_valor))
else:
    print('Não existe valor maior, os dois são iguais, primeiro valor: {}, Segundo valor:  {}.'.format(primeiro_valor, segundo_valor))