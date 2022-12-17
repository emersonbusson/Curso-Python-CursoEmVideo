 #Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.

real = float(input('Digite quanto dinheiro você tem na carteira: '))
dolar = 5.53
eur = 6.40
cart = real / dolar
cart2 = real / eur
print('___'*12)
print('Com R$ {:.2f} na carteira! \n Você pode comprar: \n US$: {:.2f} \n €: {:.2f}'.format(real,cart, cart2))
print('___'*12) 