# Cria uma string chamada "concatenacao" que junta (concatena) vários valores:
# 'Clebson', um espaço em branco ' ', o número 55.36 (convertido para texto com str()), outro espaço e 'Henrique'.
# Resultado final: "Clebson 55.36 Henrique"
concatenacao = 'Clebson' + ' ' + str(55.36) + ' ' + 'Henrique'
print(concatenacao)  # Exibe: Clebson 55.36 Henrique

# Cria uma string repetindo a letra 'A' 10 vezes: 'AAAAAAAAAA'
a_dez_vezes = 'A' * 10

# Cria uma string repetindo o nome 'Clebson' 3 vezes: 'ClebsonClebsonClebson'
tres_vezes_clebson = 3 * 'Clebson'

# Imprime a string com 10 letras 'A'
print(a_dez_vezes)  # Exibe: AAAAAAAAAA

# Imprime o nome 'Clebson' repetido 3 vezes
print(tres_vezes_clebson)  # Exibe: ClebsonClebsonClebson

# Imprime tudo junto: as letras 'A' repetidas, um espaço, o nome repetido 3 vezes, outro espaço, e a string com nome e número
print(a_dez_vezes, ' ', tres_vezes_clebson, ' ', concatenacao)
# Exibe: AAAAAAAAAA   ClebsonClebsonClebson   Clebson 55.36 Henrique
