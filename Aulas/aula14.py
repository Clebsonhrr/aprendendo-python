nome = 'Clebson'
altura = 1.79
peso = 98
imc = peso / altura ** 2


#"f-strings" = F é igual a formatação 

linha_1 = f'{nome} tem {altura:.2f} de altura, pesa {peso} quilos e o seu imc é {imc:.2f}'

print(linha_1)

print(nome, 'tem', altura, 'de altura,', 'pesa', peso, 'quilos e o seu IMC é', imc,)
        