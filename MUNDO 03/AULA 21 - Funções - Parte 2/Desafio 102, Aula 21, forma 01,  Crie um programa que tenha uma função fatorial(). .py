''' Crie um programa que tenha uma função fatorial(), que receba dois parâmetros: o primeiro que indique o número
a calcular e o outro chamado show, que será um valor lógico (opcional), indicando se será mostrado ou não na tela
o processo de cáculo do fatorial'''

def fatorial (num=0,show=False):
    ''' => Calcula o Fatorial de uma número.
    :param num:  (opcional) O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return O valor do Fatorial de um número 'num'.'''
    print()
    print('-=' * 20)
    if num == 0:
        print('0! = 1')
    else:
        fatorial = num
        f = 1
        while fatorial > 0:
            if show == True:
                print(f'{fatorial}', end=' ')
                print('x' if fatorial > 1 else ' = ', end=' ')
            f *= fatorial
            fatorial -= 1
        return print(f)

fatorial(5,show=True)

print('#' * 100)
print()
help(fatorial)