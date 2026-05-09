"""
Iterando strings com while
"""

nome = input('Digite o seu nome: ')
nome_final = ''

i = 0
while i < len(nome):
    letra = '*' + nome[i]    
    nome_final += letra

    i += 1

nome_final += '*'

print(nome_final) 