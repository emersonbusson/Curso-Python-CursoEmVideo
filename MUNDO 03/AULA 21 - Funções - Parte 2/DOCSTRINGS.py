def contador(i, f, p):
    ''' Faz uma contagem e mostra na tela. 
    :param i: inicio da contagem.
    :param f: Fim da contagem.
    :param p: passo da contagem.
    :return: sem retorno'''         #< docstring
    c = i   # c igual a (contador)
    while c <= f: # enquanto o parametro ''' 'fim' = 'f' ''' não for menor ou igual a 'c'.
        print(f'{c}', end='..') # a condição enquanto vai executar esses passos seguintes.
        c += p  # c vai receber ele mesmo + o 'p' = 'passo'.
        print('FIM!') # mostra fim na tela no final de cada número mostrado


contador(1,10,1)
print()

help(contador) # mostra o interactive helpe "ele irá mostrar as informaçoes sobre as funções ou métodos''.