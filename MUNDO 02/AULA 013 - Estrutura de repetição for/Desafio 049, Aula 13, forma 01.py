# Desafio 049 - Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print(f"{' TABUADA DE MULTIPLICAÇÃO ':=^30}")
print()

num_escolhido_user = int(input('Digite um número para ver sua: '))
print()

for c in range(0, 11):
    print(f'{num_escolhido_user} X {c} = {num_escolhido_user * c}')