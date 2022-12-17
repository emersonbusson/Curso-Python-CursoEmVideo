# Desafio 109, forma 02
'''Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro
a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
desenvolvida no Desafio 108. '''


# forma guanabara.

def aumentar(preço=float(0), taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=float(0), taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=float(0), formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=float(0), formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=float(0), moeda='R$'):
    return f'{moeda} {preço:>.2f}'.replace('.', ',')

#minhaforma
# def resumo(preço=float(0), taxa1=0, taxa2=0):
#     print('--' * 20)
#     print(f'{"RESUMO DO VALOR":^40}')
#     print('--' * 20)
#     print(f'Preço Analisado:{moeda(preço): >{20}}')
#     print(f'Dobro do Preço:{moeda(dobro(preço)): >{21}}')
#     print(f'Metade do Preço:{moeda(metade(preço)): >{19}}')
#     print(f'{taxa1}% de Aumento:{moeda(aumentar(preço, taxa=taxa1)): >{21}}')
#     print(f'{taxa2}% de Redução:{moeda(diminuir(preço, taxa=taxa2)): >{20}}')
#     print('--' * 20)

#forma guanabara.
def resumo(preço=float(0), taxa1=0, taxa2=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço Analisado: \t{moeda(preço)}')
    print(f'Dobro do Preço: \t{dobro(preço,True)}')
    print(f'Metade do Preço: \t{metade(preço,True)}')
    print(f'{taxa1}% de Aumento: \t{aumentar(preço, taxa=taxa1,formato=True)}')
    print(f'{taxa2}% de Redução: \t{diminuir(preço, taxa=taxa2,formato=True)}')
    print('-' * 30)