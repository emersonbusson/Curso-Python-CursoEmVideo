''' Crie um programa onde o úsuario digite uma expressão qualquer que use parenteses.
Seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta.'''
lista = []
lista.append(str(input('Digite a sua expressão: ')))
if '(' and ')' in lista[0]:
    p1 = lista[0].count('(')
    p2 = lista[0].count(')')
    if p1 == p2:
        print('A Expressão é válida')
    else:
        print('A Expressão não é válida')
else:
    print('Expessão não é válida')