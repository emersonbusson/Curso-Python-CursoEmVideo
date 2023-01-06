# Desafio 040 - Crie um programa que leia duas notas de um aluno e calcule sua média. Se a média for abaixo de 5.0, a mensagem exibida deve ser "REPROVADO". Se a média estiver entre 5.0 e 6.9, a mensagem exibida deve ser "RECUPERAÇÃO". Caso contrário, se a média for 7.0 ou superior, a mensagem exibida deve ser "APROVADO".

primeira_nota = int(input('Digite a primeira nota do aluno:'))

segunda_nota = int(input('Digite a segunda nota do aluno:'))

media_aluno = (primeira_nota + segunda_nota) / 2

if media_aluno >= 7.0:
    print('O aluno tirou as notas: {} e {}, sendo a media {}, Aluno Aprovado.'.format(primeira_nota, segunda_nota, media_aluno))

elif media_aluno >= 5.0 or media_aluno >= 6.9:
    print('O aluno tirou as notas: {} e {}, sendo a média {}, Aluno em recuperação'.format(primeira_nota, segunda_nota, media_aluno))

elif media_aluno < 5.0:
    print('O Aluno tirou as notas: {} e {}, sendo a média {}, Aluno Reprovado'.format(primeira_nota, segunda_nota, media_aluno))

# OUTRAS FORMA:   if 7 > media_aluno >= 5:
