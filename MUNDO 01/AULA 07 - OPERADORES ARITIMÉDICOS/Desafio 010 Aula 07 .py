#Desafio 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Digite quantos R$(Reias) tem na carteira: '))
preco_dolar = 5.21
preco_euro = 5.54
cartateira_real_dolar = real / preco_dolar
cartateira_real_euro = real / preco_euro
print('___'*12)
print('Com R$ {:.2f} na carteira!\nVocê pode comprar:\nUS$: {:.2f}\n€: {:.2f}'.format(real,cartateira_real_dolar,cartateira_real_euro))
print('___'*12) 