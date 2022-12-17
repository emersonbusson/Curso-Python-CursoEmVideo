#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Digite o preço do produto:'))
calc = preço *5 / 100
desc = calc
result = preço - calc

print('Sua compra no valor de R$ {:.2f}. \n Com um desconto de 5% que é de: R$ {:.2f}. \n Fica um total de R$ {:.2f} com o desconto.'.format(preço,calc,result))