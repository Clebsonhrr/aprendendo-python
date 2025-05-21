"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
# Velocidade atual do carro
velocidade = 61

# Localização atual do carro na estrada (em metros, por exemplo)
local_carro = 99

# Velocidade máxima permitida no radar 1
RADAR_1 = 60

# Local onde o radar 1 está instalado na estrada
LOCAL_1 = 100

# Alcance do radar — ou seja, quantos metros antes e depois do radar ele detecta o carro
RADAR_RANGE = 1
if velocidade > RADAR_1:
    print('Carro passou pelo radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and \
    velocidade > RADAR_1:
    print('Carro multado em radar 1')