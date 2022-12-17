'''Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.'''
'''O programa vai perguntar o valor da casa, o sálario do comprador e em quantos anos ele vai pagar. '''

'''Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do sálario  ou então o emprestimo será negado.'''
import time

print('\33[31m-=' * 50)

valordacasa = float(input('qual é o valor em R$ da casa que você deseja comprar?'.title()))

print('\33[32m-=' * 50)

salario = float(input('qual o valor do seu ganho mensal em R$?'.title()))

print('\33[35m-=' * 50)

idade = int(input('qual a sua idade atual? '.title()))

print('\33[33m-=' *50)

qtosAnos = float(input('em quantos anos você vai financiar a casa?'.title()))

print('\33[37m-=\33[m' *50)


print('\33[31mCALCULANDO AS INFORMAÇÕES, \33[4:33m"AVISO: VOCÊ TEM DE ESTÁ CIENTE QUE O VALOR MENSAL DAS PRESTAÇÕES NÃO PODEM ULTRAPASSAR DE 30% DO SEU SÁLARIO R$: {:.1f}.\33[35m POR FAVOR, AGUARDE.....\33[m'.format(salario))
time.sleep(3)

porcentosalario = (salario *30 / 100)

mesesfinanciamento = (qtosAnos * 12)

prestacao = (valordacasa / mesesfinanciamento)

if prestacao < porcentosalario:
 print('Para pagar uma casa de R$ {:.2f}, em {:.0f} anos, a prestação será de R${:.2f}, (financiamento aprovado), parabéns.'.title().format(valordacasa, qtosAnos, prestacao))

elif prestacao > porcentosalario:
 print('Para pagar uma casa de R$ {:.2f}, em {:.0f} anos, a prestação será de R${:.2f}, (financiamento negado), sentimos muito.'.title().format(valordacasa, qtosAnos, prestacao))

print('\33[7m..EXTRAINDO RESUMO..\33[m' *3)

print('30% do sálaro do comprador é R$: {:.2f}'.title().format(porcentosalario))
print('A quantidade de meses de financiamento é de: {:.0f} meses.'.title().format(mesesfinanciamento))
print('O valor da prestação é de R$: {:.2f}.'.title().format(prestacao))

