# Válidar CPF

import re
import sys

# cpf_enviado_pelo_usuario = '746.824.890-70' \
#     .replace('.', '') \
#     .replace('-', '') \
#     .replace(' ', '')

entrada = input('Digite o seu CPF: ')

cpf_enviado_pelo_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_e_repetida = entrada == entrada[0] * len(entrada)

if entrada_e_repetida:
    print('Voçê enviou dados sequênciais')
    sys.exit()

nove_digitos = cpf_enviado_pelo_usuario[:9]
contador_regressivo = 10
digito_1 = 0

for digito in nove_digitos:
    digito_1 += int(digito) * int(contador_regressivo)
    contador_regressivo -= 1

digito_1 = (digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

###

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo = 11
digito_2 = 0

for digito in dez_digitos:
    digito_2 += int(digito) * contador_regressivo
    contador_regressivo -= 1

digito_2 = (digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

### 

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_pelo_usuario == cpf_gerado_pelo_calculo:
    print('CPF válido')
else:
    print('CPF inválido')