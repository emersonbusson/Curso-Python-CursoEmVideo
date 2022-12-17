num = [2, 5, 9, 1]
print(num)
num[2] = 3 # No indice '2' a lista recebe o valor '3', valor '5' que antes existia foi eliminado(substituido).
print(num)
num.append(7) #A lista recebe o valor '7' ao final, com um novo indice.
print(num)
num.sort() #A lista foi ordenada.
print(num)
num.sort(reverse=True) # a lista foi ordenada de trás para frente, de forma reversa.
print(num)
num.insert(2, 0) # No indice '2', será colocado '0' e os indices ordenados novamente com uma nova quantidade de indices.
print(num)
num.pop() #Sem nada entre paramentro, o método pop, remove o último valor da lista.
print(num)
num.pop(2) #Remove o valor que está no indice entre parametro. no caso, removeu o número '0', que estava no indice '2'.
print(num)
print(f'Essa lista tem {len(num)} elementos') # lê a quantidade de elementos dentro da lista.
