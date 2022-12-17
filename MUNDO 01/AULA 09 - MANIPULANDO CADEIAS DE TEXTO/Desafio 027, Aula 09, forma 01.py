'''FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA.'''
'''MOSTRANDO EM SEGUIDA O PRIMEIRO E O ULTIMO NOME'''



nome = str(input('Digite seu nome completo:')).upper().strip()
nome2 = nome.split()
print('O primeiro nome é: {}'.format(nome2[0]))
print('O último nome é: {}.'.format(nome2[len(nome2)-1]))
