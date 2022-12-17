def teste (b):
    global a #se indicado 'global' antes da variavel 'a', ele não vai criar uma nova variavel 'a' de escopo local e vai utilizar a variavel já criada de escopo 'global'.
    a = 8   #Não é mais uma variavel de escopo local, visto que 'global a' foi declarado na linha anterior.
    b += 4                          #ESCOPO LOCAL, dentro da indentação.
    c = 2                           #ESCOPO LOCAL, dentro da indentação.
    print(f'A dentro Vale: {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5                                   #FAZ PARTE DO PROGRAMA PRINCIPAL, TEM ESCOPO GLOBAL.
teste(a)

print(f'A fora vale {a}') # A fora agora vale 8 no lugar de 5. visto que dentro da função 'a' foi declarado como 'global' a = 8, substituindo o 5 pelo 8.
''' print(f'B fora vale {b}')  ''' # vai dá erro, porque b tem escopo local (somente dentro da def).
''' print(f'C fora vale {c}') ''' # # vai dá erro, porque 'c' tem escopo local (somente dentro da def).