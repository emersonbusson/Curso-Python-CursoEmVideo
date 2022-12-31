'''Desafio 104, Crie uma função leiaint(), que vai funcionar de forma semelhante a função input() do python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leia('Digite um n: ')
'''
#Forma 02
def leiaint(msg):
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('\33[31mERRO! Digite um número inteiro válido.\33[m')
    return valor

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número: {n}.')