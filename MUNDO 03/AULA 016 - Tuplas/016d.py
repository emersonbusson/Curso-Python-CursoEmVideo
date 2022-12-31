lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

for cont in range(0, len(lanche)):                            #utilizando o Range + LEN
    print(f'\33[31mEu vou comer {lanche[cont]}.\33[m') #mostrar lanche na posição [cont].
print('\33[33mComi para caramba!\33[m')


for comida in lanche:                                           #utilizando a váriavel composta diretamente.
    print(f'Eu vou comer {comida}.')          # for(para) cada comida(contando?) in(em) lanche(váriavél composta lanche).
print('Comi pra caramba!')

for cont in range(0, len(lanche)):                            #utilizando o Range + LEN
    print(f'\33[35mEu vou comer {lanche[cont]} na posição {cont}.\33[m') #mostrar lanche na posição [cont].
print('\33[33mComi para caramba!\33[m')

for pos, comida in enumerate(lanche):                        #duas váriaveis no for separadas por ','
    print(f'\33[34mEu vou comer {comida} na posição {pos}\33[m')
print('Comi pra caramba!')


