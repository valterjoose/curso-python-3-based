"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

variavel = 'valter'

print(f'{variavel:_>25}')
print('')
print(f'{variavel:_<25}')
print('')
print(f'{variavel:_^25}')
print('')
print(f'{3.141592653589793238462:.2f}')
print('')
print(f'O hexadecimal de 1500 é: {1500:08X}')


