# Cria uma variável chamada 'nome' e armazena o texto 'Clebson'
nome = 'Clebson'

# Cria uma variável chamada 'altura' e armazena o valor 1.80 (em metros)
altura = 1.80

# Cria uma variável chamada 'peso' e armazena o valor 95 (em quilos)
peso = 95

# Calcula o IMC (Índice de Massa Corporal) usando a fórmula:
# peso dividido pela altura ao quadrado: IMC = peso / (altura * altura)
# O resultado é armazenado na variável 'imc'
imc = peso / altura ** 2

# Mostra apenas o valor do IMC calculado
print(imc)

# Mostra uma frase completa com as informações da pessoa e o IMC calculado
# Usa vírgulas para juntar diferentes partes na mesma linha do print
# O Python insere automaticamente espaços entre as vírgulas
print(nome, 'tem', altura, 'de altura,', 'pesa', peso, 'quilos e o seu IMC é', imc)
