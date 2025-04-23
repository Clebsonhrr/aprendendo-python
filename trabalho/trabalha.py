import pandas

planilha = pandas.read_excel(io = './trabalho/planilha.xlsx')

colunas = ['Operadora', 'Convênio', 'Saldo Devedor', 'Status do Contrato', 'Data Exclusão', 
'Marca Óptica', 'Nome Beneficiário', 'CPF Beneficiário', 'Tipo de Beneficiário', 'Status Atual Beneficiário',]


planilha = planilha[colunas]

planilha['Marca Óptica Odonto'] = None
planilha['Emitir Boletos'] = None
planilha['Observação'] = None


print(planilha.head(5))


excel = pandas.ExcelWriter(path='./trabalho/resultado.xlsx',)
planilha.to_excel(excel_writer=excel, sheet_name='BASE', index=False)

positivo = planilha[planilha['Saldo Devedor'] > 0]
positivo.to_excel(excel_writer=excel, sheet_name='POSITIVO', index=False)

negativo = planilha[planilha['Saldo Devedor'] < 0]
negativo.to_excel(excel_writer=excel, sheet_name='NEGATIVO', index=False)

#nada = planilha.head(0)
#nada.to_excel(excel_writer=excel, sheet_name='MOV.DIGITAL', index=False)

excel.close() 