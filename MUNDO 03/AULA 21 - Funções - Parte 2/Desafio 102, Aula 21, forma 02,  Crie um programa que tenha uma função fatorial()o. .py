''' Crie um programa que tenha uma função fatorial(), que receba dois parâmetros: o primeiro que indique o número
a calcular e o outro chamado show, que será um valor lógico (opcional), indicando se será mostrado ou não na tela
o processo de cáculo do fatorial'''
#forma Guanabara.
def fatorial(n,show=False):
    '''
    --> Calcula o fatorial de um número.
    :param n: O número a ser cauculado
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do fatorial do número 'n'.
    '''
    f = 1
    for c in range(n,0, -1):
        if show:
            if c > 1:
                print(f'{c} X', end=' ')
            else:
                print(f'{c} = ', end=' ')
        f *= c
    return f

#programa principal
print(fatorial(5, True))
# help(fatorial)

