'''Desafio 113, Aula 23, forma 01, Reescreva a função leiaint() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloot() com a mesma funcionalidade. '''
#forma guanabara.

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\33[31mERRO: por favor, digite um número válido.\33[m')
            continue #continue joga direto para o while.
        except (KeyboardInterrupt):
            print('\33[31mUsuario preferiu não digitar esse número.\33[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print('\33[31mERRO: por favor, digite um número válido.\33[m')
        except (KeyboardInterrupt):
            print('\33[31mUsuario preferiu não digitar esse número.\33[m')
            return 0
        else:
            return n

num = leiaint('Digite um valor: ')
num2 = leiafloat('Digite um real: ')
print(f'O valor inteiro digitado foi: {num}, e o real {num2}.')