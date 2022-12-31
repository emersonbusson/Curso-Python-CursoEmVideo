def mostralinha():
    print('-' *30)
# entre a def(função) e o programa principal, tem que ter duas linhas vazias.
#programa principal
mostralinha()
print(f'{"SISTEMA DE ALUNOS":^30}')
mostralinha()
mostralinha()
print(f'{"CADASTRO DE FUNCIONARIOS":^30}')
mostralinha()
mostralinha()
print(f'{"ERRO DO SISTEMA":^30}')
mostralinha()

print()
print('\33[31m-' *30,f'{"FUNÇÃO COM PARÂMETRO":^10}','-' *30 )
print('\33[m')

#função(def) com parâmetros.
def mensagem(msg):
    print('-' *30)
    print(msg)
    print('-' *30)
# entre a def(função) e o programa principal, tem que ter duas linhas vazias.
#programa principal
mensagem('SISTEMA DE ALUNOS')
mensagem('EMERSON BUNITÃO')



