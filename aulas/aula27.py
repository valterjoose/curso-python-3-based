"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(f'{variavel[2]}')
print('-' * 10)
print(f'{variavel[0:3]}')
print('-' * 10)
print(len(f'{variavel}'))
print('-' * 10)
print(f'{variavel[0::1]}')
print(f'{variavel[-1::-1]}')
