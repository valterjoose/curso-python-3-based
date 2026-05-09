# Condição While -> Repete algo ate uma condição acontecer
# Ex:
condicao = True

while condicao:
    print('~~ CADASTRO DO USUARIO ~~')
    print()
    sair = input('Deseja Sair? S/n')

    if sair == 'S' or sair == 's':
        break

print('Saiu!!')

#
i = 0

while i < 10: # | < | <= | = | >= | > |
    i = i + 1
    print(i)

print('Acabou')