"""
Tipo tupla - Uma lista imutável
"""
nomes = 'Valter', 'Vitor', 'Julia'
print(nomes)
# Tuplas são listas q não vai mudar ao decorrer do código
# Caso você queira guardar uma lista imutavel, use tuplas

# Também tem como converter uma tupla pra lista e virse versa
nomes = list(nomes)    
nomes = tuple(nomes)

# Os comandos da lista também são validos na tupla
