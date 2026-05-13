qtd_linhas = 5
qtd_colunas = 5
coluna = 1

coluna = 1
while coluna <= qtd_colunas: # --> Para coluna de 1 ate 5 Faca 
    linha = 1
    while linha <= qtd_linhas: # --> Para linha de 1 ate 5 Faca 
        print(f'Coluna: {coluna} Linha: {linha}')

        linha += 1 # Já que aqui não se tem o para adicionamos um contador
    print()
    coluna += 1 # Quando a coluna 1 enche, o cantador adiciona 1 e voltamos ao
                # Inicio do (while coluna <= qtd_colunas)

print('fim') # Fim do while
