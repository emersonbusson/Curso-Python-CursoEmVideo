def teste (b):
    b += 4                          #ESCOPO LOCAL, dentro da indentação.
    c = 2                           #ESCOPO LOCAL, dentro da indentação.
    print(f'A dentro Vale: {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5                                   #FAZ PARTE DO PROGRAMA PRINCIPAL, TEM ESCOPO GLOBAL.
teste(a)

print(f'A fora vale {a}')
''' print(f'B fora vale {b}')  ''' # vai dá erro, porque b tem escopo local (somente dentro da def).
''' print(f'C fora vale {c}') ''' # # vai dá erro, porque 'c' tem escopo local (somente dentro da def).