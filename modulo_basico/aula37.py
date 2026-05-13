"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:    # \ Continue
        print('Não vou mostrar o', contador) # | 
        continue                             # / e continue

    print(contador)

    if contador == 40: # \ Contdição pra usar o Break
        break          # / Break -> quebra o laço de repetição


print('Acabou')