# Desafio 036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Qual é o valor da casa: '))

salario = float(input('Qual o valor do seu ganho mensal R$: '))

idade = int(input('Qual a sua idade atual: '))

anos_financiamento = float(input('Em quantos anos você vai financiar a casa: '))

# calcula 30% do salário e armazena o resultado em na variável.
porcentagem30salario = (salario *30 / 100)
# calcula o número de meses em um determinado número de anos e armazena o resultado na variavel.
meses_financiamento = (anos_financiamento * 12)
# o valor da prestação mensal dividindo o valor total da casa pelo número de meses de financiamento e armazena o resultado na variável.
prestacao = (valor_casa / meses_financiamento)

if prestacao < porcentagem30salario:
    print('Para pagar uma casa de R$ {:.2f} em {:.0f} anos a prestação será de R$ {:.2f} \33[34m30% salário R$ {}\33[m -> (financiamento aprovado) parabéns.'.format(valor_casa, anos_financiamento, prestacao, porcentagem30salario))
else:
    print('Para pagar uma casa de R$ {:.2f} em {:.0f} anos a prestação será de R${:.2f} \33[31m30% salário R$ {}\33[m -> (financiamento negado) sentimos muito.'.format(valor_casa, anos_financiamento, prestacao, porcentagem30salario))
