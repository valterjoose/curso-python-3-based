### ~~~~~~ QUANDO SE USAR O WHILE ~~~~~~ ###

senha_salva = '123456'
senha_digitada = ''
i =  0 

while senha_salva != senha_digitada:
    senha_digitada = input(f'Digite a senha({i}x): ')

    i += 1

print('Acesso válido')
print(f'Tentativas ({i}x)')


### ~~~~~~ COMEÇANDO A USAR FOR ~~~~~~ ###

texto = 'Python'
letra_mudada = ''

for letra in texto: 
    letra_mudada += f' * {letra}'
letra_mudada += ' *'
print(letra)
print(letra_mudada)   