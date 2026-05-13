# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

a, b, *_, d, e = lista
print(a, d)

for nome in lista:
    print(nome, end=' ')
#                  └─> ao inves de quebrar linha no fim de cada nome, 
#                      ele vai apenas adicionar um espaço. 

print(*lista)  # * -> a cada item da lista   ┐
print(*string) # * -> a cada caracter da str ├─> ele add um espaço
print(*tupla)  # * -> a cada item da tupla   ┘

salas = [
#     0         1         2
    ['Válter', 'João',   'Jatobá'], # 0

    ['Júlia',  'Maria',  'Ana'],    # 1

    ['Samuel', 'Edinez', 'Otávio']  # 2
]

print(*salas, sep='\n')
#        │     │    │
#        │     │    └─> e quebrar a linha de cada lista
#        │     └─> separar cada lista 
#        └─> a cada item da lista ele add um espaço