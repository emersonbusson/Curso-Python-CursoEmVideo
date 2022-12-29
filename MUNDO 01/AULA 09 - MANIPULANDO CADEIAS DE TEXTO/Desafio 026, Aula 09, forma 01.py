# Desafio 026: faça um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite qualquer frase para a contagem: ')).upper().strip()

print('Sua frase digitada é: {}\nTem a quantidade de letras "A": {}'.format(frase, frase.count('A')))
print('A frase tem indice total de: {}'.format(len(frase)))
print('A quantidade de caracteres sem os espaços é: {}'.format(len(frase) - frase.count(' ')))
print('A primeira letra ''A'' apareceu na posição: {}'.format(frase.find('A')))
print(' A útima letra ''A'', apareceu na posição: {}'.format(frase.rfind('A')))