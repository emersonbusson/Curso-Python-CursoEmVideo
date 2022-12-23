#Desafio 005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.

numero = int(input('Digite um número:'))
numero_sucessor =  numero - 1
numero_antecessor =  numero + 1
print('O número antecessor é: {}'.format(numero_sucessor))
print('O número sucessor é: {}'.format(numero_antecessor))