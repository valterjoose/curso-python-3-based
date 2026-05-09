'''
Faça uma lista de compras com listas
o usuario deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista
'''

# i -> Nome do produto 
# voltar pro menu principal
# a -> indice do produto
# voltar pro menu principal
# l -> apenas mostra lista 

import os


lista_produto = []
int_apagar_produto = 0

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ').lower()

    if opcao == 'i':
        os.system('cls')
        add_produto = input('Valor: ')
        lista_produto.append(add_produto)
        continue
        
    if opcao == 'a':
        os.system('cls')
        for indice, nome in enumerate(lista_produto):
            print(indice, nome)
        apagar_produto = input('Digite o id do produto: ')
        try:                
            del lista_produto[int_apagar_produto]
            int_apagar_produto = int(apagar_produto)
            continue
        except ValueError:
            os.system('cls')
            print('Erro...Digite apenas letras')
            continue

    if opcao == 'l':
        os.system('cls')

        if len(lista_produto) == 0:
            print('Lista vazia, adicione produtos')
            continue

        print('lista de produtos')
        for indice, nome in enumerate(lista_produto):
            print(f'{indice} - {nome}')
            continue

    elif opcao.isdigit():
        os.system('cls')
        print('Erro... Não Digite numeros')
        continue
    elif opcao.isalpha():
        os.system('cls')
        print('Erro... Digite um apenas a letra inicial do nome')
        continue            
    elif opcao.isalnum():
        os.system('cls')
        print('Erro... Não Digite Caracteres')
        continue