nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ') 

if nome and idade:
    print(f'Seu nome é, {nome} você tem {idade} anos')
    print(f'Seu nome invertido é:', (nome[::-1]))

    if ' ' in nome:
        print(f'Seu nome contem contem espaços')

    else:
        print('Seu nome NÃO contem espaços')


    print(f'Seu nome contem {len(nome)} letra')

    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A ultima letra do seu nome é: {nome[-1]}')

else:
    print('Desculpe você deixou os campos vazios.')







 #', (' ' in nome))