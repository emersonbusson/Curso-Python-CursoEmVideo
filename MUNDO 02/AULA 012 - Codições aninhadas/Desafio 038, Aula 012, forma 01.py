'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais. '''

numero_inteiro1 = int(input('Digite o primeiro valor:'.title()))
numero_inteiro2 = int(input('Digite o segundo valor:'.title()))

if numero_inteiro1 > numero_inteiro2:
    print('o primeiro valor é maior. Valor Digitado: {}.'.title().format(numero_inteiro1))
elif numero_inteiro2 > numero_inteiro1:
    print('o segundo valor é maior, valor Digitado: {}.'.title().format(numero_inteiro2))
else:
    print('não existe valor maior, os dois são iguais, primeiro valor: {}, Segundo valor:  {}.'.title().format(numero_inteiro1, numero_inteiro2))