"CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO UMA MENSAGEM NO FINAL, DE ACORDO COM A MEDIA ATINGIDA"

'''MÉDIA ABAIXO DE 5.0, REPROVADO''' '''MEDIA ENTRE 5.0 E 6.9, RECUPERAÇÃO.''' '''MÉDIA 7.0 OU SUPERIOR, APROVADO'''

primeira_nota = float(input('Digite a primeira nota do aluno:'.title()))

segunda_nota = float(input('Digite a segunda nota do aluno:'.title()))


media_aluno = (primeira_nota + segunda_nota) /2

if media_aluno >= 7.0:
    print('O aluno tirou as notas: {} e {}, sendo a media {}, Aluno Aprovado.'.title().format(primeira_nota, segunda_nota, media_aluno))

elif media_aluno >= 5.0 or media_aluno >= 6.9:
    print('O aluno tirou as notas: {} e {}, sendo a média {}, Aluno em recuperação'.title().format(primeira_nota, segunda_nota, media_aluno))

elif media_aluno < 5.0:
    print('O Aluno tirou as notas: {} e {}, sendo a média {}, Aluno Reprovado'.title().format(primeira_nota, segunda_nota, media_aluno))

#OUTRAS FORMA:   if 7 > media_aluno >= 5: