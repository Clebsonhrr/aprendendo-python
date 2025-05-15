"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

# Pede ao usuário para digitar um número
numero_str = input('Vou dobrar o número que vc digitar: ')

# Tenta converter a string digitada em um número float
try:
    numero_float = float(numero_str)  # Tenta transformar o texto em número com ponto (ex: 5.2)

    # Se conseguir converter, mostra o número convertido
    print('FLOAT:', numero_float)

    # Calcula o dobro do número e mostra o resultado com 2 casas decimais
    print(f'O dobro de {numero_str} é {numero_float * 2:.1f}')

# Se der erro na conversão (ex: se o usuário digitar "abc"), entra aqui
except:
    print('Isso não é um número')  # Informa que o valor digitado não é válido


# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')