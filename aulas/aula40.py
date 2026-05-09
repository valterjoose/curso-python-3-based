# Calculadora --> | + | - | * | / |

resultado = 0

while True: # Abrindo Repetição e deixando verdadeira sem questionamento
    print('--- CALCULADORA V1.0 ---')
    num1 = input('Digite o primeiro número: ') # Armazenando o primeiro valor
    num2 = input('Digite o segundo número: ')  # Armazenando o segundo valor

    print('VOCÊ DESEJA:')
    print('Somar       = + ')
    print('Subtrair    = - ')
    print('Multiplicar = * ')
    print('Dividir     = / ')
    operador = input(': ') # Armazenando qual operador voçê deseja utilizar
   
    numeros_validos = None # Variavel 
    num1_float = 0         # Variavel numero 1 transformada pro tipo float
    num2_float = 0         # Variavel numero 2 transformada pro tipo float
    
    try: # Caso o usuario escreveu tudo certo vem pra cá
        num1_float = float(num1)      # transformando num1 em float
        num2_float = float(num2)      # transformando num2 em float
        resultado = float(resultado)  # transformando o resultado em float
        numeros_validos = True        # A variavel numeros_validos vira True

    except:                    # Caso o usuario escrevel algo errado
        numeros_validos = None # A variavel (numeros_validos) se mantém None 

    if numeros_validos is None: # se numeros validos for None o except vem pra cá
       print('Um ou ambos números digitados são inválidos')   
       continue # continue ignora oq digitou e volta para o while
    
    operadores_permitidos = '+-/*' # variavel pra declarar os operadores permitidos

    if operador not in operadores_permitidos: # se o usuario nao digitar algum desses
       print('Operador inválido')             # operadores, ele caí nesse erro
       continue # continue ignora oq digitou e volta para o while

    if len(operador) > 1: # se o usuario digitar mais de 1 caracter
       print('Digite apenas 1 operador') # ele caí nesse erro  
       continue # continue ignora oq digitou e volta para o while

    ### Caso tudo der certo ele faz o calculo
    print('Realizando sua conta... confire o resultado abaixo:')
    if operador == '+':
        print(f'{num1_float}+{num2_float} = ',num1_float + num2_float)

    elif operador == '-':
        print(f'{num1_float}-{num2_float} = ',num1_float - num2_float)

    elif operador == '*':
        print(f'{num1_float}x{num2_float} = ',num1_float * num2_float)

    elif operador == '/':
        print(f'{num1_float}/{num2_float} = ',num1_float / num2_float)

    else: 
        print('Não deveria chegar aqui...')     

    #~~OPÇÂO SAIR~~#
    sair = input('Deseja Sair? [s]im: ').lower().startswith('s')
    print('Saindo...')                 # |     # |
                                       # |     # ↪ ignora todas as outras letras
                                       # |     e so verifica a primeira letra digitada
                                       # |     
                                       # ↪ transforma letras maiusculas em minusculas                                  
    if sair is True: 
        break # Fim do while
    