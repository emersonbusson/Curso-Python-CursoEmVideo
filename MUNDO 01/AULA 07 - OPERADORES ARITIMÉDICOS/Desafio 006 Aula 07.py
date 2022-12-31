# Desafio 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um número:'))
dobro_numero =  numero * 2
triplo_numero = numero * 3
raiz_numero = numero **(1/2)
print('O dobro do número é: {}\nO Triplo é: {}\nA Raiz é: {} '.format(dobro_numero,triplo_numero, raiz_numero))