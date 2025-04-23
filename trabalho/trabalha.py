import pandas

planilha = pandas.read_excel (io = './trabalho/planilha.xlsx')

colunas = ['Operadora', 'Convênio', 'Saldo Devedor', 'Status do Contrato', 'Data Exclusão', 'Marca Óptica', 'Nome Beneficiário', 'CPF Beneficiário', 'Tipo de Beneficiário', 'Status Atual Beneficiário', 
'ID Fatura', 'Valor da Fatura', 'Data de Emissão']

abas = 

print(planilha[colunas].head(5))