''' Crie um programa que tenha uma tupla com várias palavras, não usar acentos, depois disso, você deve mostrar para cada palavra, quais são suas vogais. '''
#forma alternativa.

import re
todas = ('aprender', 'programar', 'linguagem', 'python',
         'curso', 'gratis', 'estudar', 'praticar',
         'trabalhar', 'mercado', 'programador', 'futuro')
for indice, item in enumerate(todas):
    print(f'\33[33mNa palavra > {item.upper()}:\33[m',end=' ')
    for y, L in enumerate(item):
        vogais = re.findall(r"[aeiou]", L, re.IGNORECASE)
        print('{}'.format(vogais),end='',)
    print(end='\n')
    print('\33[34m-' * 50)
