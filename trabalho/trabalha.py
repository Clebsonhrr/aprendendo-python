import pandas

# Lê uma planilha do Excel localizada no caminho './trabalho/planilha.xlsx' 
# e armazena seu conteúdo em um DataFrame chamado "planilha".
# A função read_excel é do pacote pandas e é usada para importar dados de arquivos .xlsx.
# O argumento "io" indica o caminho do arquivo a ser lido.
planilha = pandas.read_excel(io = './trabalho/planilha.xlsx')


colunas = ['Operadora', 'Convênio', 'Saldo Devedor', 'Status do Contrato', 'Data Exclusão', 
'Marca Óptica', 'Nome Beneficiário', 'CPF Beneficiário', 'Tipo de Beneficiário', 'Status Atual Beneficiário',]

planilha = planilha[colunas]

planilha['Marca Óptica Odonto'] = None
planilha['Emitir Boletos'] = None
planilha['Observação'] = None


print(planilha.head(5))

# Cria um objeto ExcelWriter, que permite escrever (salvar) dados em um arquivo Excel (.xlsx).
# O arquivo será criado ou sobrescrito no caminho './trabalho/resultado.xlsx'.
# Esse objeto é armazenado na variável "excel" e pode ser usado com métodos como .to_excel().
excel = pandas.ExcelWriter(path='./trabalho/resultado.xlsx',)


# Salva o DataFrame "planilha" em uma planilha Excel usando o objeto "excel" (ExcelWriter).
# Os dados serão escritos na aba (sheet) chamada 'BASE'.
# O argumento index=False indica que o índice do DataFrame não será incluído no arquivo Excel.
planilha.to_excel(excel_writer=excel, sheet_name='BASE', index=False)


# Filtra o DataFrame "planilha" para selecionar apenas as linhas onde a coluna "Saldo Devedor" é maior que zero.
# O resultado é um novo DataFrame contendo apenas os registros com saldo devedor positivo.
# Esse novo DataFrame é armazenado na variável "positivo".
positivo = planilha[planilha['Saldo Devedor'] > 0]


positivo.to_excel(excel_writer=excel, sheet_name='POSITIVO', index=False)


negativo = planilha[planilha['Saldo Devedor'] < 0]
negativo.to_excel(excel_writer=excel, sheet_name='NEGATIVO', index=False)

#nada = planilha.head(0)
#nada.to_excel(excel_writer=excel, sheet_name='MOV.DIGITAL', index=False)

excel.close() 