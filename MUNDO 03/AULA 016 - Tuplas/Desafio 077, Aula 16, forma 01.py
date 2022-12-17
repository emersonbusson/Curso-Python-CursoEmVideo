''' Crie um programa que tenha uma tupla com várias palavras, não usar acentos, depois disso, você deve mostrar para cada palavra, quais são suas vogais. '''

todas = ('aprender', 'programar', 'linguagem', 'python',
         'curso', 'gratis', 'estudar', 'praticar',
         'trabalhar', 'mercado', 'programador', 'futuro')
vogais = 'aeiou'
for indice, item in enumerate(todas):
    print(f'\33[33mNa palavra > {item.upper()}:\33[m')
    for y, L in enumerate(item):
        if L == 'a' or \
                L == 'e' or \
                L == 'i' or \
                L == 'o' or \
                L == 'u':
            print('\33[35mEncontrado a letra \33[31m{}\33[35m na posição: {}\33[m'.format(L, y))
    print('\33[34m-' * 50)
