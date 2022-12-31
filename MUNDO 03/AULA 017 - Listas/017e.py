a = [2, 3, 4, 7]
b = a # ao igualar uma lista com outra, o python cria uma ligação entre elas.
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('--'*30)
b[2] = 7 # Como foi igualado, ambas as listas foram alteradas (visto que estão interligadas).
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('--'*30)
#forma correta de fazer uma cópia da lista sem fazer uma ligação.
b = a[:] # cópia da lista.
b[2] = 8 #Agora o valor foi alterado somente na lista 'B', visto que agora houve uma cópia da lista.
print(f'Lista A: {a}')
print(f'Lista B: {b}')
