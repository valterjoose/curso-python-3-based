# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

porta = input('[E]ntrar [S]air ')
senha_digitada = input('Digite a senha: ')
senha_usuario = '123'

if porta == 'E' and senha_digitada == senha_usuario:
    print('Entrando...')

else:
    print('Saindo...')