#Desafio 012 - Faça um algorítimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco_produto = float(input('Digite o preço do produto: '))
desconto_produto = preco_produto1 * 5 / 100
novo_preco_desconto = preco_produto - desconto_produto

print('Sua compra no valor de R$ {:.2f}.\nO desconto de 5% é de R${:.2f}.\nFica um total de R$ {:.2f} com o desconto aplicado.'.format(preco_produto,desconto_produto,novo_preco_desconto))