def somar (a, b, c):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3,2,5) #(3) vai ser copiado para dentro da variavel 'A'. # (2) vai ser copiado para dentro da variavel 'B'. # (5) vai ser copiado para dentro da variavel 'C'.

'somar(8,4)' # se não colocar o terceiro parâmetro 'C' de forma opcional (c=0), o programa irá dá erro por não ter colocado um terceiro parâmetro 'c'.

def somaop(a=0,b=0, c=0): #função de exemplo de parâmetro (opcional) a=0, b=0,c=0.
    s = a + b + c
    print(f'A soma vale {s}')

somaop(2,1) # com o parâmetro opcional, não dá erro.
