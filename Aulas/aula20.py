# Pede ao usuário para digitar o primeiro valor (pode ser número ou letra)
primeiro_valor = input('Digite um valor: ')

# Pede ao usuário para digitar o segundo valor
segundo_valor = input('Digite o segundo valor: ')

# A função input() sempre retorna uma STRING, então as comparações serão feitas como texto, a menos que se converta para número

# Verifica se o primeiro valor é maior que o segundo (comparação feita pela ordem de caracteres, como em ordem alfabética)
if primeiro_valor > segundo_valor:
    # Se for verdade, exibe que o primeiro valor é maior que o segundo
    # O formato "{variavel=}" mostra tanto o nome da variável quanto seu valor (ex: primeiro_valor='B')
    print(f'{primeiro_valor=} é maior que {segundo_valor=}')
    
# Se o primeiro valor for menor que o segundo
elif primeiro_valor < segundo_valor:
    # Exibe que o segundo valor é maior que o primeiro
    print(f'{segundo_valor=} é maior que {primeiro_valor=}')
    
# Se os dois valores forem exatamente iguais
else:
    # Informa que os dois valores são iguais
    print(f'{primeiro_valor=} e {segundo_valor=} são iguais')
