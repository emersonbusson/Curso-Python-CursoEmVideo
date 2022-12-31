print('-= '*10, 'VERIFICADOR DE FRASE POLINDROMO', '=-' *10)
frase = str(input('Digite uma frase: ')).upper()
palavras = frase.split() #separou a frase com o metodo split.
junto = ''.join(palavras) # juntou a frase, sem os espaços.
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('O inverso de: {} é: {} , trata-se de um palindromo'.title().format(junto, inverso))
else:
    print('O inverso de: {} é: {} , Não trata-se de um palíndromo'.title().format(junto, inverso))

