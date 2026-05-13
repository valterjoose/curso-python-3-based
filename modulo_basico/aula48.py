"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

# var      0       1     2   3
lista = [ 'Maria', 1.60, 60, True, []]
#          └──────┬──────┘   │     │
#                 │          │     └─> Dá pra criar listas dentro de listas
#                 │          │
#                 │          └─> Dá pra criar boolens dentro de listas
#                 │
#                 └─> Dá armazenar varios tipos de variaveis

# Como chamar um item de uma lista?
print(lista[0])
#     │     │
#     │     └─> Coordenada da lista. 0, 1, 2,...
#     │
#     └─> nome da lista (variavel)
#
# OBS: Caso voçê tentr acessar uma coordenada q ainda nao foi adicionada:
# vai dar esse erro: IndexError: list index out of range

# Como alterar o valor de um item da lista?
lista[0] = 'Válter'
#     │       │
#     │       └─> Nome que vai mudar, também pode transformar qualquer tipo
#     │
#     └─> Coordenada da lista. 0, 1, 2,...

# Adicionar um item na lista:
lista.append('Ana')
#       │      │
#       │      └─> Oque deseja adicionar
#       │
#       └─> método " .append "
#
# OBS: Adiciona o item ao (Final) da lista

# Adicionar um item no índice escolhido:
lista.insert(0, 10)
#        │   │   │   
#        │   │   └─> item que você quer adicionar  
#        │   │      
#        │   └─> Coordenada do indice que você quer q o item fique     
#        │         
#        └─>  método de str ( .insert() ) 

# Apagar um item da lista:
lista.pop()
#      │
#      └─> Remove o ultimo item da lista

# Como apagar um item de uma lista?
del lista[0]
#     │   │
#     │   └─> Coordenada da lista. 0, 1, 2,... ou -1 -2 -3,... para os ultimos números
#     │
#     └─> nome da lista (variavel)
#
# OBS: Tome cuidado no uso desse comando, pois pode bugar o terminal já que
#      ele gasta muita memoria quando está em alta performace

# Limpar a lista:
lista.clear()
# │      │
# │      └─> método de str ( .clear() )
# │
# └─> variavel

# Juntar duas listas:
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
#   
lista_c = lista_a + lista_b
#  │        └─────┬─────┘               
#  │              │          
#  │              │          
#  │              └─> soma das duas listas  
#  │      
#  └─> (variavel)  junção dos dois valores  
 
# Extender uma lista:
lista_a.extend(lista_b)  
#   │      │      │        
#   │      │      │        
#   │      │      └─> (Variavel) que vai entregar o seu valor pra principal      
#   │      │             
#   │      └─> metódo de str ( .extend() )         
#   │                 
#   └─>  (variavel que vai receber o valor da outra) 

#

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# variaveis tem valores imutaveis:
#
# A variaveis tem valores imutaveis, ou seja indepente do que acontece lá
# na frente do código, ela nao muda oque tá atras.
# Ex:
nome_a = 'Válter' # ──> Valor inicial de uma variavel
nome_b = nome_a   # ──> var_b = var_a 
nome_a = 'Luiz'   # ──> mudança no valor da variavel a
#
print(nome_a)     #       ┌──> 'Luiz'
#                   print ┤ 
print(nome_b)     #       └──> 'Válter'

# listas tem valores mutaveis:
#
# No caso da lista, quando voce adiciona um valor la na frente,
# toda linha de raciocinio do seu codio vai seguir junto com a mudança
# Ex:
lista_a = ['Válter', 'Luiz'] # ──> Valor inicial de uma lista
lista_b = lista_a            # ──> list_b = list_a 
#                              
lista_a[0] = 'Ana'           # ──> mudança no valor da lista a
print(lista_b)               # print ──> ['Ana', Luiz]
#                                │
#                                └──> mostra o valor da lista a, depois da
#                                     mudança.
#   
# Agora, utilizando um método de str:
# Ele cria uma nova linha de raciocinio, apenas copia o valor antigo e passa
# pra nova lista, como se fosse armazenar um versão antiga dela:
# Ex:                           
lista_a = ['Válter', 'Luiz'] # ──> Valor inicial de uma lista 
lista_b = lista_a.copy()     # list_b = (copia da lista_a)
#                              
lista_a[0] = 'Ana'           # ──> mudança no valor da lista_a 
print(lista_b)               # ──> tela -> [valor antigo da lista_a]
#                                    │
#                                    └──> mesmo depois da mudança de valor,
#                                         Não muda nada na lista_b
# Fim.:)