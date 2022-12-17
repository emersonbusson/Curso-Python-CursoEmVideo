'''CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM 'SILVA' NO NOME. '''

nome = str(input('Digite seu nome completo:')).upper().strip()
print('Seu nome completo é {}, tem silva no nome?: {} '.format(nome, 'SILVA' in nome))

