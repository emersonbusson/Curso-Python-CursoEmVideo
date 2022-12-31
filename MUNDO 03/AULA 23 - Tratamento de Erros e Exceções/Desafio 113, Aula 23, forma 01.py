'''Desafio 113, Aula 23, forma 01, Reescreva a função leiaint() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.

Aproveite e crie também uma função leiaFloot() com a mesma funcionalidade. '''


def leiaint(leia='',valor=0):
    while True:
        try:
            valor = int(input(leia))
        except KeyboardInterrupt:
            print('\n\33[35mO úsuario preferiu não digitar o valor.\33[m')
            break
        except:
            print('\33[31mERRO por favor, digite um número válido\33[m')
        else:
            break
    return valor

def leiareal(leia='', valor=0):
    while True:
        try:
            valor = float(input(leia))
        except KeyboardInterrupt:
            print('\n\33[33mO úsuario preferiu não digitar o valor\33[m')
            break
        except:
            print('\33[32mErro por favor, digite um número válido\33[m')
        else:
            break
    return valor


int = leiaint('Digite um número inteiro: ')
real = leiareal('Digite um número real: ')

print(f'O valor inteiro digitado foi: {int}, o valor real foi {real}.')


