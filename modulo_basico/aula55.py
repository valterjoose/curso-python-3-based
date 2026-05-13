"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

# Numeros com o módulo do python
# Usados apenas para quando for calcular números float MUITO grandes
# Como funciona:
import decimal

num1 = decimal.Decimal(0.7)
num2 = decimal.Decimal(0.1)
num3 = num1 + num2
print(num3)
# Ele calcula perfeitamente o número, mas não é recomendado o uso sem motivo

# Números com 'f' str
# O uso do comando só é recomendado para calculos finalizandos, apenas para
# exibir ao usuario, já que pode acontecer algum erro caso continue calculando
numero1 = 0.7
numero2 = 0.1
numero3 = numero1 + numero2
print(f'{numero3:.2f}')

# Round, o melhor para calcular e exibir, faz o calculo exato do número
# e nao exibi numeros com 0 ou q não tem 100% de precisão
numero_1 = 0.7
numero_2 = 0.1
numero_3 = numero_1 + numero_2
print(numero_3)
print(round(numero_3, 2))