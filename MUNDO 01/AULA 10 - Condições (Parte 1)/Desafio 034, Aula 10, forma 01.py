# Desafio 034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

from time import sleep

salario = float(input('Digite o valor do seu salário R$: '))
sleep(1)
print('Processando...')

if salario > 1250:
    aumento_10 = salario * 0.10
    print(f'Você terá um aumento de salário de 10% R$: {aumento_10:.2f} valor com aumento R$: {salario + aumento_10:.2f}')
else:
    aumento_15 = salario * 0.15
    print(f'Você terá um aumento de salário de 15% R$: {aumento_15:.2f}  valor com aumento R$: {salario + aumento_15:.2f}')