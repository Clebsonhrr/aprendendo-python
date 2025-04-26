# Solicita o nome do usuário e armazena como texto (string)
nome = input('Qual o seu nome? ')

# Exibe uma saudação com o nome usando f-string
print(f'Olá  {nome}!')

# Solicita a idade do usuário e armazena como string
idade = input('Quantos anos você tem? ')
# (Neste código, a idade é capturada, mas não está sendo usada depois)

# Pede ao usuário que digite dois números entre 1 e 10
numero_1 = input('Digite um número de 1 a 10: ')
numero_2 = input('Digite outro número de 1 a 10: ')

# Converte os dois números de string para inteiros, para que possam ser somados
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

# Soma os dois números e exibe o resultado
# A f-string insere o resultado da soma direto na frase
print(f'A soma dos números é: {int_numero_1 + int_numero_2}')
