"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
# Velocidade atual do carro
velocidade = 61

# Localização atual do carro na estrada (em metros, por exemplo)
local_carro = 100

# Velocidade máxima permitida no radar 1
RADAR_1 = 60

# Local onde o radar 1 está instalado na estrada
LOCAL_1 = 100

# Alcance do radar — ou seja, quantos metros antes e depois do radar ele detecta o carro
RADAR_RANGE = 1

# Verifica se o carro está acima da velocidade permitida no radar 1
velo_carro_passar_radar_1 = velocidade > RADAR_1

# Verifica se o carro está dentro da área de alcance do radar 1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
                       local_carro <= (LOCAL_1 + RADAR_RANGE)
# Essa linha verifica se o carro está entre 99 e 101 (inclusive), que é a área do radar

# Verifica se o carro deve ser multado
# Isso só acontece se ele passou pelo radar E estava acima da velocidade
carro_multado_radar_1 = carro_passou_radar_1 and velo_carro_passar_radar_1

# Mensagem: o carro estava acima da velocidade do radar
if velo_carro_passar_radar_1:
    print('Velocidade carro passou do radar 1')

# Mensagem: o carro passou dentro do alcance do radar
if carro_passou_radar_1:
    print('Carro passou radar 1')

# Mensagem: o carro estava acima da velocidade e dentro do radar => deve ser multado
if carro_multado_radar_1:
    print('Carro multado em radar 1')