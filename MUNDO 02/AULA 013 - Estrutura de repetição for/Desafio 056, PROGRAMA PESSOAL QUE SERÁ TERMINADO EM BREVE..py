''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas, no final do programa, mostre, a média de dade do grupo
qual é o nome do homem mais velho, quantas mulheres tem menos de 20 anos '''
nome = str()
idade = int()
idade_acumulador = int(0)
idade_maior = int()
idade_menor = int()
idade_maior_sex_masculino = int()
mulheres_menos_de_20_contador = int(0)

nome_mais_velho = str()
sex = str()
sexstr = 'fFmM'

for c in range(1,5):
    print('\33[33m{} A {} PESSOA DO GRUPO {}\33[m'.format('-=' *4, c , '=-' *4))
    nome = str(input('Digite seu primeiro nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sex = str(input('Digite seu sexo [M/F]: '))
    if not nome.isalpha():
        nome = str(input('Nome digitado é inválido,tente novamente um nome válido: ')).strip()
    if not idade.isnumeric():
        idade = int(input('O valor da idade foi digitado é inválido, tente novamente um valor válido: '))
    if sex not in sexstr:  # letra do sexo digitado está correto?
        sex = str(input('Valor incorreto, Digite seu sexo: M ou F: ')).strip()
    idade_acumulador += int(idade)
    if c == 1:                              # qual a maior idade do grupo?
        idade_maior = idade
        idade_menor = idade
    else:
        if idade > idade_maior:             # idade maior.
            idade_maior = idade
            if sex in 'Mm':                         # nome e idade homem mais velho.
                idade_maior_sex_masculino = idade
                nome_mais_velho = nome
        if idade < idade_menor:             #idade menor.
            idade_menor = idade


#    if idade < 20 and sex in 'fF':  #quantas mulheres tem menos de 20 anos?
            mulheres_menos_de_20_contador += 1

print('\33[31mA maior idade do grupo é: {}.\33[m'.format(idade_maior))
print('A menor idade do grupo é: {}. '.format(idade_menor))
print('\33[32mA media de idade do grupo é: {}. \33[m'.format(idade_acumulador /4))
print('O homem mais velho se chama: {} e tem {} anos.'.format(nome_mais_velho, idade_maior_sex_masculino))
print('\33[35mA quantidade de mulheres do grupo com menos de 20 anos é: {}\33[m'.format(mulheres_menos_de_20_contador))


