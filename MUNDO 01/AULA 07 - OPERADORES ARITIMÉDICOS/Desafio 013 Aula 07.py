# Desafio 013 - Faça um algorítimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario_funcionario = float(input('Qual é o sálario do funcionario? R$: '))
salario_15aumento = salario_funcionario * 0.15
print(f'Um Funcionario que ganhava R$: {salario_funcionario:6.2f}.\nCom 15% de aumento R$ {salario_15aumento:6.2f}.\nAgora passa a receber R$: {salario_funcionario + salario_15aumento:6.2f}.')