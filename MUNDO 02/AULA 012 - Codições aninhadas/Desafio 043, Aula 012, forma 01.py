'''Desemvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela a baixo:'''
# Abaixo de 18.5: abaixo do peso.
# entre 18.5 e 25: peso ideal.
# de 25 até 30: sobrepeso.
# de 30 até 40: obesidade
# acima de 40: obsidade mórbida.

print(' calculo imc-=- '.upper() *3)
print('\33[31m=-\33[m' * 20)

print('EX: PESO: 85')
print('EX: ALTURA: 1.75')


altura_user = float(input('\33[34m Agora, Digite sua altura em metros: '))
peso_user = float(input('\33[32m Digite Seu Peso em kg: \33[m'))

calculo_imc = peso_user / (altura_user * altura_user)
print('\33[31m=-\33[m' * 20)
print(f' Seu IMC É: {calculo_imc:5.2f}')
print('\33[31m=-\33[m' * 20)

if calculo_imc < 18.5:
    print('ABAIXO DO PESO')

elif calculo_imc > 18.5 and calculo_imc <=25:
    print('\33[33mPESO IDEAL\33[m')
elif calculo_imc > 25 and calculo_imc <=30:
    print('\33[33mSOBREPESO\33[m')
elif calculo_imc >30 and calculo_imc <=40:
    print('\33[35mOBESIDADE\33[m')
else:
    print('\33[:7mOBESISADE MÓRBITA\33[m')


print('\33[31m=-\33[m' * 20)