# Desafio 053 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

print( 5* '-=','DETECTOR DE PALINDROMO', 5*'-=')

frase = str(input('Digite um frase: '))
frase = frase.replace(" ","").lower()
frase_invertida = frase [::-1]
if frase == frase_invertida:
    print('A palavra ou frase: {}, de trás para frente fica: {}, trata-se de um palidromo.'.title().format(frase, frase_invertida))
else:
    print('A palavra ou frase: {}, de trás para frente fica: {}, não trata-se de um palidromo.'.title().format(frase, frase_invertida))
