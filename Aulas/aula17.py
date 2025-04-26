#if = se
#elif = se não se
#else = se não

# Pede ao usuário que digite uma opção: "entrar" ou "sair"
# A resposta é armazenada como texto (string) na variável "entrada"
entrada = input('Você quer "entrar" ou "sair"? ') 

# Verifica se o usuário digitou exatamente a palavra "entrar"
if entrada == 'entrar':
    print('Você entrou no sistema')  # Mostra essa mensagem se a condição for verdadeira

# Se o usuário não digitou "entrar", mas digitou "sair", executa este bloco
elif entrada == 'sair':
    print('Você saiu do sistema')  # Mostra essa mensagem se a condição for verdadeira

# Se o usuário digitou algo diferente de "entrar" ou "sair", cai no "else"
else:
    print('Você não digitou nem entrar e nem sair')  # Mensagem de erro ou opção inválida


#A estrutura if, elif, else é usada para tomar decisões no código.

#O Python lê de cima para baixo:
    #Se o if for verdadeiro, ele executa aquele bloco e ignora o resto.
    #Se não for, ele tenta o elif.
    #Se nenhuma condição for atendida, ele executa o else.

#O input() sempre retorna texto, então as comparações (== 'entrar') precisam ser feitas com strings. 

#Se quiser que o código aceite palavras com letras maiúsculas ou minúsculas 
# (ex: "Entrar", "SAIR", "sAiR"), você pode usar .lower() assim:

#entrada = input('Você quer "entrar" ou "sair"? ').lower()
