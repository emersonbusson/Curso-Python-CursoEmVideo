'''Crie um programa que leia uma frase qualquer e diga se ela é um polindromo, desconsiderando os espaços'''

print( 5* '-=','DETECTOR DE PALINDROMO', 5*'-=')

texto_dig_user = str(input('Digite um frase:')).upper().strip()
texto_dig_user = texto_dig_user.replace(" ","")
texto_dig_user = texto_dig_user.lower().title()
palidromo = texto_dig_user [::-1]
if texto_dig_user == texto_dig_user [::-1]:
    print('A palavra ou frase: {}, de trás para frente fica: {}, trata-se de um palidromo.'.title().format(texto_dig_user, palidromo))
else:
    print('A palavra ou frase: {}, de trás para frente fica: {}, não trata-se de um palidromo.'.title().format(texto_dig_user, palidromo))
