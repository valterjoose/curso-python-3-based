#AT1
numero_usuario = input('Digite um numero inteiro: ')

try:
    numero_int = int(numero_usuario)
    
    if (numero_int % 2 == 0):
        print(f'O numero {numero_int} é par')
    else:
        print(f'O numero {numero_int} é impar')    
except:
    print('Isso não é um número inteiro')


#AT2 
Horario_usuario = int(input('Que horas são? '))

if (Horario_usuario >= 0) and (Horario_usuario <= 11):
    print('Bom Dia!!')
elif (Horario_usuario >= 12) and (Horario_usuario <= 17):
    print('Boa Tarde!!')
elif (Horario_usuario >= 18) and (Horario_usuario <= 23):
    print('Boa Noite!!')
else: 
    print('Algo deu errado...')  


#AT3
nome_do_usuario = str(input('Qual é o seu nome?'))

if (len(nome_do_usuario) >= 0) and (len(nome_do_usuario) <= 4):
    print('Seu nome é curto!!')
if (len(nome_do_usuario) >= 5) and (len(nome_do_usuario) <= 6):
    print('Seu nome é médio!!')
if (len(nome_do_usuario) > 7):
    print('Seu nome é grande!!')