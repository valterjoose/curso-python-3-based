salas = [
#     0         1         2
    ['Válter', 'João',   'Jatobá'], # 0

    ['Júlia',  'Maria',  'Ana'],    # 1

    ['Samuel', 'Edinez', 'Otávio', (0, 10, 20, 30, 40)]  # 2
]

print(salas[0]) 
#           │
#           └─> lista

print(salas[1][1]) 
#           │  │
#           │  └─> item da lista
#           └─> lista

print(salas[2][3][2]) 
#           │  │  │
#           │  │  └─> item da lista
#           │  └─> lista dentro da lista
#           └─> lista

print()

for sala in salas:
    for aluno in sala:
        print(aluno)