# Desafio 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Digita quantos metros a ser convertido:'))
centimetros = metros *100
milimetros = metros *1000
print('O valor em metros digitado: {}\nO valor convertido para centímetros é: {}\nO valor convertido para milímetros é: {}'.format(metros,centimetros,milimetros))