primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor ')
# print('Valor 1 =', primeiro_valor)
# print('Valor 2 =', segundo_valor)



# if primeiro_valor > segundo_valor:
#    print('Primeiro valor é:', primeiro_valor, 'e ele é maior que o segundo valor:', segundo_valor)
#
# elif segundo_valor > primeiro_valor:
#    print('Primeiro valor é:', primeiro_valor, 'e ele é menor que o segundo valor:', segundo_valor)
#
# else:
#    print('Primeiro valor é:', primeiro_valor, 'e ele tem o mesmo valor que o segundo valor:', segundo_valor)



if primeiro_valor > segundo_valor:
    print(primeiro_valor, '>', segundo_valor)

elif segundo_valor > primeiro_valor:
    print(primeiro_valor, '<', segundo_valor)

else:
    print(primeiro_valor, '=', segundo_valor)