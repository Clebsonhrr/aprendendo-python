
# Operadores in e not in
 # Strings são iteráveis
 #  0 1 2 3 4 5
 #  O t á v i o
 # -6-5-4-3-2-1
nome = 'otavio'
print(nome[2])
print(nome[-4])
print('vio' in nome)
print('zero' in nome)
print(10 * '-')
print('vio' not in nome)
print('zero' not in nome)


nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontar no seu nome: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}' )

else:
    print(f'{encontrar} não estar em {nome}')

