import ExUteis
#foi importado o arquivo ".py" ExUteis criado anteriormente


#programa principal
num = int(input("Digite um valor: "))
fat = ExUteis.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {ExUteis.dobro(num)}.')
print(f'O triplo de {num} é {ExUteis.triplo(num)}.')
