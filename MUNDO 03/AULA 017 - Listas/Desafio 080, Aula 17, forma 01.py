''' Crie um programa onde o usúario possa digitar cinco valores numéricos e cadastre-os na posição correta sem uscar o sort
No final, mostre a lista ordenada na tela. '''
#Método de Bolhas

numeros = list()
fim = 5
for n in range(0,5):
    num = int(input('Digite um valor: '))
    numeros.append(num)
print(f'Lista sem Ordenação: {numeros}.')
while fim > 1:
    trocou = False
    x = 0
    while x < (fim -1):
        if numeros[x] > numeros[x + 1]:
            trocou = True
            temp = numeros[x]
            numeros[x] = numeros[x + 1]
            numeros[x + 1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1
print(f'Lista Ordenada: {numeros}')


