''' Crie um programa onde o usúario possa digitar cinco valores numéricos e cadastre-os na posição correta sem uscar o sort
No final, mostre a lista ordenada na tela. '''
#Forma Guanabara.
x = 0
lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[len(lista)-1]: # ou lista[-1]
        lista.append(n)
        print(f'O número {n}, foi adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição: {pos}.')
                break
            pos += 1
print(f'Lista Ordenada: {lista}')