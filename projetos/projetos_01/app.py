# Ler dados da planilhar
# Inserir cada célula de cada linha em um campo
# do sistema

import openpyxl


# Ler um arquivo do excel
workbook = openpyxl.load_workbook('Base_dados_produtos_reais.xlsx')
vendas_sheet = workbook['vendas'] # selecionando a pagina para trabalhar

for linha in vendas_sheet.iter_rows(min_row=2):
    print(linha[0].value)
    print(linha[1].value)
    print(linha[2].value)
    print(linha[3].value)
