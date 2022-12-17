num = [2, 5, 2, 9, 1]
num.remove(2) #remove somente a primeira ôcorrencia do valor dentro do parametro, para excluir as próximas ocorrencias(caso tenha mais válores repetidos), tem que colocar em uma estrutura de repetição.
#num.remove(4)  'Caso o valor a ser removido, não exista na lista, o programa dá erro, para resolver o erro, tem que ser utilizada uma condição.
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4.') #Como não existe o número 4 na lista, será mostrado o print.
if 5 in num:
    num.remove(5) # o número 5, como existe na lista, ele foi removido.
else:
    print('Não achou o número 5')
print(num)