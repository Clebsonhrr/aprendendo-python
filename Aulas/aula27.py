"""
 Fatiamento de strings
  012345678
  Olá mundo
 -987654321
 Fatiamento [i:f:p] [::]
 Obs.: a função len retorna a qtd 
 de caracteres da str
 """

variavel = 'Ola mundo'
print(variavel[4])
print(variavel[4:])
print(variavel[4:8])
print(variavel[4:5])
print(variavel[0:5])
print(variavel[:5])


print(len(variavel))
print(len(variavel[3]))

print(variavel[0:9:2])

print(variavel[::-1])
