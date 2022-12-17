''' Crie um programa onde o úsuario digite uma expressão qualquer que use parenteses.
Seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta.'''
#Comentario youtube.

expr = str(input('Digite uma expressão: '))
pilha = 0
for e in expr:
    if e == '(':
        pilha = pilha + 1
    if e == ')':
        pilha = pilha - 1
    if pilha == 0:
        break
if pilha == 0:
    print('Sua expressão é válida.')
else:
    print('Sua expressão está errada.')