'''FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:'''

'''quantas vezes aparece a letra "A". '''
'''Em que posição ela aparece a primeira vez'''
'''Em que posição ela aparece a ultima vez'''

frase = str(input('Digite qualquer frase para a contragem:')).upper().strip()

print('Sua frase digitada é: {}, e tem a quantidade de letras A: {}'.format(frase, frase.count('A')))
print('A frase tem o total de: {} caracteres no indice.'.format(len(frase)))
print('A primeira letra ''A'' apareceu na posição: {}.'.format(frase.find('A')))
print(' A útima letra ''A'', apareceu na posição: {}'.format(frase.rfind('A')))