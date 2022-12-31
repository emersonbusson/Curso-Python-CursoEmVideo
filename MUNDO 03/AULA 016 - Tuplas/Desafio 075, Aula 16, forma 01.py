''' Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final mostre:
A- Quantas vezes apareceu o valor 9
B- Em que posição foi digitado o primeiro valor 3.
C- Quais forem os números pares.
'''

valores = (int(input('Digite o 1º valor: ')),
           int(input('Digite o 2º valor: ')),
           int(input('Digite o 3º valor: ')),
           int(input('Digite o 4º valor: ')))
print(f'Você digitou os valores: \33[31m{valores}\33[m')
print(f'O valor 9 apareceu {valores.count(9)} vezes')

if 3 in valores:
    print(f'O valor 3 foi digitado na posição: {valores.index(3) +1}.')
else:
    print(f'O valor 3 não foi diigitado em nenhuma posição.')
print('Valores pares que foram digitados:',end=' ')
for par in valores:
    if par %2 == 0:
     print(f'{par}', end= ' ')
    else:
        print('Nenhum!')
    break
