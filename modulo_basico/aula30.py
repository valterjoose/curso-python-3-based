"""
~~~~~~ORGANIZAÇÂO DE CODIGO~~~~~~~~

CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

vel_passar_radar_1 = velocidade > RADAR_1 # Condição para

carro_passou_o_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) # carro passou pelo radar 1

carro_multado_radar_1 = carro_passou_o_radar_1 and vel_passar_radar_1


if carro_passou_o_radar_1:
    print('RADAR 1: PASSOU DO RADAR')

if vel_passar_radar_1:
    print('RADAR 1: PASSOU DA VELOCIDADE')

if carro_multado_radar_1:
    print('RADAR 1: MULTADO')

