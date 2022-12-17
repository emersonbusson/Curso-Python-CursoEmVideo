''' Crie um programa que tenha uma tupla com várias palavras, não usar acentos, depois disso, você deve mostrar para cada palavra, quais são suas vogais. '''

#Forma guanabara.


todas = ('aprender', 'programar', 'linguagem', 'python',
         'curso', 'gratis', 'estudar', 'praticar',
         'trabalhar', 'mercado', 'programador', 'futuro')

for p in todas:
    print(F'\nNa palavra {p.upper()} temos: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')

