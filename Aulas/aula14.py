nome = 'Clebson'  # Cria uma variável com o nome da pessoa

altura = 1.79     # Cria uma variável com a altura da pessoa (em metros)

peso = 98         # Cria uma variável com o peso da pessoa (em quilos)

# Calcula o IMC (Índice de Massa Corporal) usando a fórmula: peso dividido pela altura ao quadrado
# Aqui usamos o operador ** para elevar a altura ao quadrado
imc = peso / altura ** 2


# "f-strings" é uma forma moderna e prática de formatar textos em Python
# A letra "f" antes das aspas permite inserir variáveis dentro da string usando chaves { }

# Aqui estamos criando uma frase usando f-string:
# - {nome} insere o valor da variável nome
# - {altura:.2f} formata a altura com 2 casas decimais (ex: 1.79)
# - {peso} insere o peso normalmente
# - {imc:.2f} formata o valor do IMC com 2 casas decimais (ex: 30.58)

linha_1 = f'{nome} tem {altura:.2f} de altura, pesa {peso} quilos e o seu imc é {imc:.2f}'


# Exibe a frase formatada
print(linha_1)

# Aqui temos a mesma informação sendo exibida, mas sem o uso de f-string.
# Usamos vírgulas para juntar os valores dentro do print()
# O Python automaticamente coloca espaços entre as partes separadas por vírgula

print(nome, 'tem', altura, 'de altura,', 'pesa', peso, 'quilos e o seu IMC é', imc)
