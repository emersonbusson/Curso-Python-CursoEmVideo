from math import radians, sin, cos, tan
angu = float(input('Digite o Ângulo Desejado:'))
seno = sin(radians(angu))
coss = cos(radians(angu))
tan1 = tan(radians(angu))
print('O Ângulo de: {:.2f}, tem o SENO de: {:.2f}'.format(angu,seno))
print('O Ângulo de: {:.2f}, tem o COSSENO de: {:.2f}'.format(angu,coss))
print('O Ângulo de: {:.2f}, tem a TANGENTE de: {:.2f}'.format(angu, tan1))


#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosceno e tangente.