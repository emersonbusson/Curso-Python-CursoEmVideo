''' Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional).

Adicione também os docstrings da função. '''

def notas(*n, sit=False):
    '''
    --> Função para analisar notas e situações de varios alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionario com várias informações sobre a situação da turma.
    '''

    boletim = dict ()
    boletim["Total"] = len(n)
    boletim["maior"] = max(n)
    boletim["menor"] = min(n)
    boletim["media"] = sum(n) / boletim["Total"]
    if sit == True:
        if boletim["media"] >= 7:
            boletim["situação"] = 'BOA'
        elif 6 <= boletim["media"] < 7:
            boletim["situação"] = 'RAZOAVEL'
        elif boletim["media"] < 6:
            boletim["situação"] = 'RUIM'
    return print(boletim)

notas(8,7,4,9,7, sit=True)
