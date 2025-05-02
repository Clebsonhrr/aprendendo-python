nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ') 

if nome:
    print(f'Seu nome é,', nome, 'você tem', idade, 'anos')
    
if ' ' in nome:
    print('Seu nome contem espaço') 

elif  nome:
    print('Seu nome não contem espaço') 

if nome:
    print(f'Seu nome invertido é:', (nome[::-1]))
    print(f'Seu nome contem', len(nome), 'letras')
    print(f'A primeira letra do seu nome é:',(nome[0:1]))
    print(f'A ultima letra do seu nome é:', (nome[0:]))

else:
    print('Desculpe nada foi digitado')




 #', (' ' in nome))