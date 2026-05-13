# Gerador de CPF

import random

for i in range(10):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

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

    print(cpf_gerado_pelo_calculo)