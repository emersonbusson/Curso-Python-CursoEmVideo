#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosceno e tangente.

import math

user_digitado = float(input('Digite um angulo qualquer:'))
angu = user_digitado
angu = math.radians(angu)
sen01 = math.sin(angu)
cos01 = math.cos(angu)
tang01 = math.tan(angu)


print('O Ângulo de: {:.1f} , tem o SENO de: {:.2f},'.format(user_digitado, sen01))
print('O Ângulo de: {:.1f} , tem o COSSENO de: {:.2f}'.format(user_digitado,cos01))
print('O Ângulo de: {:.1f} , tem a TANGENTE de: {:.2f}'.format(user_digitado,tang01))