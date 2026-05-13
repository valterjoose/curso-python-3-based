"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

condicao = 10 == 10
variavel ='Valor' if condicao else 'Outro Valor'
print(variavel)

###

digito = 1
novo_digito = digito if digito <= 9 else 0
print(novo_digito)

###

print('Valor' if  True else 'Outro Valor' if True else 'Fim')

