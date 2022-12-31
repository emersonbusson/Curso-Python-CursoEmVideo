'''Desafio 104, Crie uma função leiaint(), que vai funcionar de forma semelhante a função input() do python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leia('Digite um n: ')
'''

def leiaint(leia='',valor=''):
    valor = input(leia)
    while True:
        if valor.isdigit():
            break
        else:
            print('\33[31mERRO! Digite um número inteiro válido.\33[m')
            valor = input(leia)
    return valor


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número: {n}')


