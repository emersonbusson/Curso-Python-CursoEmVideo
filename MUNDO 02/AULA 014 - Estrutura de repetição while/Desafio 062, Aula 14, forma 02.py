'''Melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos.
o programa encerra quando ele disser que quer mostrar 0 termos..'''

''' Refaça o desafio 051, lendo o primeiro terma e a razão de uma PA,
mostrando os 10 primeiro termos da progressão usando a estrutura while.'''

#Forma Guanabara.


print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
termo = primeiro
razão = int(input('Razão da PA: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} < '.format(termo), end= ' ')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão Finalizada Com {} Termos Mostrados'.format(total))

