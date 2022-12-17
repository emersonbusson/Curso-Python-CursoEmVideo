''' Faça um algoritimo que leia o salário de um funcionario e mostre seu novo sálario, com 15% de aumento'''

sala = float(input('Qual é o sálario do funcionario? R$: '))
novo = sala + (sala * 15 /100)
print('Um Funcionario que ganhava R$: {}, com 15% de aumento, passa a receber R$: {}'.format(sala, novo))