"""
Introdução ao empacotamento e desempacotamento
"""

# Caso precise transformar os itens de uma lista em uma diversas variaveis
# você possivelmente vai se deparar com esse problema:

nome_1, nome_2 = [ 'Valter', 'José']
print(nome_1)
# ValueError: too many values to unpack (expected 2, got 3)
# Você não declarou todos os itens em uma variavel

# para resolver, basta utilizar o comando " * + (variavel) " recomendado: _
# na programação o (_) significa (não irei usar essa variavle)
# Ex:
nome1, nome2, *_ = [ 'Valter', 'José', 'Julia']
print(nome2) # assim o comando executa normalmente
# Tudo que nao foi declarado vira uma variavel do tipo list

# Caso deseja declarar uma variavel do meio e deixar uma da frente em branco
# Faça isso:
_, _, nome3, *_ = [ 'Valter', 'José', 'Julia']
print(nome3) # assim o comando executa normalmente