#Desafio 043 - Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo: abaixo de 18.5: abaixo do peso; entre 18.5 e 25: peso ideal; de 25 até 30: sobrepeso; de 30 até 40: obesidade; acima de 40: obesidade mórbida.

print(f'{" calculo imc ":=^50}'.upper())
print('EX: PESO: 85'.capitalize())
print('EX: ALTURA: 1.75'.capitalize())
print('=' * 50)

altura_usuario  = float(input('Digite sua altura em metros: '))

peso_usuario = float(input('Digite seu peso em kg: '))

imc = peso_usuario / ( altura_usuario  * altura_usuario )

if imc < 18.5:
    print(f'Seu IMC é: {imc:5.2f} - status: ABAIXO DO PESO')
elif imc >= 18.5 and imc <=25:
    print(f'Seu IMC é: {imc:5.2f} - status: PESO IDEAL')
elif imc > 25 and imc <=30:
    print(f'Seu IMC é: {imc:5.2f} - status: SOBREPESO')
elif imc >30 and imc <=40:
    print(f'Seu IMC é: {imc:5.2f} - status: OBESIDADE')
else:
    print(f'Seu IMC é: {imc:5.2f} - status: OBESISADE MÓRBITA')