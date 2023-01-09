print('-= '*10, 'VERIFICADOR DE FRASE POLINDROMO', '=-' * 10)

frase = str(input('Digite uma frase: ')).upper()

palavras = frase.split()  # separou a frase com o metodo split.

frase_junta = ''.join(palavras)  # juntou a frase, sem os espaços.

frase_invertida = ''

for letra in range(len(frase_junta) - 1, -1, -1):
    frase_invertida += frase_junta[letra]

if frase_invertida == frase_junta:
    print('O inverso de: {} é: {} , trata-se de um palindromo.'.format(frase_junta, frase_invertida))
else:
    print('O inverso de: {} é: {} , Não trata-se de um palíndromo.'.format(frase_junta, frase_invertida))