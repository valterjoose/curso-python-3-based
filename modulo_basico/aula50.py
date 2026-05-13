"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Válter', 'Julia', 'Vitor']

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))

# Aqui basicamente é um contador, a variavel indices recebe um range com
# uma len do inicio da lista ate o fim, a cada item adicionado na lista,
# 1 numero é add junto.
# 