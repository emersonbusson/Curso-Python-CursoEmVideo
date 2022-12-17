''' Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero vinte. 
Seu pograma deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso '''

numeros_ex = (
'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
'catorze',
'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

indice = int(input('Digite um número entre 0 e 20: '))
while indice > 20:
    indice = int(input('\33[31mValor Incorreto, Digite um número entre 0 e 20: \33[m'))

print(f'Você digitou o número: \33[31m{numeros_ex[indice]}\33[m.')
