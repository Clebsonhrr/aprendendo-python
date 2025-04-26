a = 'AS'
b = 'BAO'
c = 20.2
string = 'a={} b={} c={:.3f}'

formato = string.format(a,b,c)

print(formato)


# Criamos três variáveis:
# 'a' recebe o texto (string) 'AS'
# 'b' recebe o texto (string) 'BAO'
# 'c' recebe o número decimal (float) 20.2

# Em seguida, criamos uma variável chamada 'string' que contém um texto com espaços reservados (chaves {}) 
# para inserir os valores das variáveis a, b e c. 
# O trecho {:.3f} significa que o valor de 'c' será formatado com 3 casas decimais (ex: 20.200).

# Depois usamos o método .format(a, b, c) para substituir as chaves {} dentro da string pelos valores das variáveis.
# O primeiro {} será substituído por 'a', o segundo por 'b' e o terceiro por 'c' formatado.

# O resultado é guardado na variável 'formato'.

# Por fim, usamos print(formato) para mostrar o resultado no terminal.
# A saída será: a=AS b=BAO c=20.200