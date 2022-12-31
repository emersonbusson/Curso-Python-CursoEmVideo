''' Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero vinte. 
Seu pograma deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso '''
# forma guanabara
cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze','catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.', end=' ')
print(f'Você digitou o Nº: \33[33m{cont[num]}\33[m.')
