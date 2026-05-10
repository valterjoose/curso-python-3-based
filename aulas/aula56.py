frase = 'Olha só que, coisa interessante'
lista_de_palavras = frase.split()
print(lista_de_palavras)

frase = 'Olha só que, coisa interessante'
lista_de_frases = frase.split(', ')
print(lista_de_frases)

"""
split, strip e join com str e list

split  -> divide uma string
strip  -> remove espaços extras
join   -> junta elementos em uma única string
"""

# String original
frase = '   Olha só que   , coisa interessante          '

# --------------------------------------------------
# SPLIT
# --------------------------------------------------
# Aqui estamos dividindo a frase pela vírgula.
# O resultado será uma LISTA com 2 partes.

lista_frases_cruas = frase.split(',')

# Resultado:
# ['   Olha só que   ', ' coisa interessante          ']

print(lista_frases_cruas)


# --------------------------------------------------
# STRIP
# --------------------------------------------------
# Agora vamos remover os espaços desnecessários
# do começo e do final de cada frase.

lista_frases = []

# enumerate() serve para pegar:
# índice (i) e valor (frase)
for i, frase in enumerate(lista_frases_cruas):

    # .strip() remove espaços das extremidades
    frase_limpa = lista_frases_cruas[i].strip()

    # adiciona a frase limpa na nova lista
    lista_frases.append(frase_limpa)

# Resultado:
# ['Olha só que', 'coisa interessante']

print(lista_frases)


# --------------------------------------------------
# JOIN
# --------------------------------------------------
# join() junta os elementos da lista em uma string.
# O texto antes do .join() será o separador.

frases_unidas = ', '.join(lista_frases)

# Resultado:
# 'Olha só que, coisa interessante'

print(frases_unidas)


# --------------------------------------------------
# EXEMPLOS EXTRAS
# --------------------------------------------------

nome = '   Valter   '

# remove espaços dos dois lados
print(nome.strip())

# remove espaços da direita
print(nome.rstrip())

# remove espaços da esquerda
print(nome.lstrip())


# --------------------------------------------------
# MAIS UM EXEMPLO DE SPLIT
# --------------------------------------------------

texto = 'Python Java C++ JavaScript'

# sem passar nada no split(),
# ele separa pelos espaços
linguagens = texto.split()

print(linguagens)


# --------------------------------------------------
# MAIS UM EXEMPLO DE JOIN
# --------------------------------------------------

nomes = ['Ana', 'Carlos', 'Maria']

# junta usando " - " como separador
resultado = ' - '.join(nomes)

print(resultado)