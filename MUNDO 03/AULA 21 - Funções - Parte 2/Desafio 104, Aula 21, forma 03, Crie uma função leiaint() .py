'''Desafio 104, Crie uma função leiaint(), que vai funcionar de forma semelhante a função input() do python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leia('Digite um n: ')
'''
#forma guanabara.
def leitaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\33[31mERRO! Digite um número inteiro válido.\33[m')
        if ok: # se ok == True, o programa para.
            break
    return valor

#programa principal
n = leitaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
