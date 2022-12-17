''' Faça um programa que leia o sexo de uma pessoa,
 mas só aceite os valores ,M, e ,F, caso esteja errado, peça a digitação novamente até ter um valor correto '''


sex = str(input('Digite seu sexo: [M/F]: ')).upper().strip()[0] # [0] vai pegar somente a primeira letra.
while sex not in 'MF':
    sex = str(input('Opção incorreta, digite a opção correta [M/F]: ')).upper().strip()[0]
print('Sexo: {}, registrado com sucesso...'.format(sex))
