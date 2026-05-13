frase = ' Ola meu nome é valter' # Frase que o codigo vai verificar

i = 0               # → contador do while
contagem_final = 0  # → contador da letra que mais aparece
letra_final = ''    # → letra que mais aparece

while i < len(frase): # → quantos caracteres tem na frase
    letra_atual = frase[i] # → armazena o dado da letra q vai vereificar
    contagem_atual = frase.count(letra_atual) # verificar quantas vezes a letra atual aparece
                                              
    if contagem_final < contagem_atual and letra_atual != ' ': # se a contagem final
        letra_final = letra_atual        # for maior que a atual a atual vira a final
        contagem_final = contagem_atual
        
    i += 1

print(f'Frase: {frase}')
print()
print(f'A letra *{letra_final}* apareceu mais vezes')
print(f'Letra *{letra_final}* apareceu {contagem_final}x')

