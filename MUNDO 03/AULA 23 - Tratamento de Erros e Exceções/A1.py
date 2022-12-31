try: #Try ou tente: (Operação): Oque gerealmente pode dá problema, qual é o comando ou comandos que normalmente daria problemas.
    a = int(input('Numerador:'))
    b = int(input('Denominador:'))
    r = a / b
except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__}')
# except: #except ou exceção (Falhou, Aréa de Falha): Se falhar no de cima, oque vai acontecer?
#     print('Infelizmente tivemos um problema :(')
else: #else ou senão (deu certo): resultado,executa ou mostra algo. (Opcional)
    print(f'P resultado é {r:.1f}')
finally: #finally ou finalmente(certo ou falha), resultado, executa ou mostra algo, indendente de ter dado certo ou falhado. (Opcional).
    print('Volte sempre! Muito Obrigado.')