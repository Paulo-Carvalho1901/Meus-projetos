# Ler dados da planilhar
# Inserir cada célula de cada linha em um campo
# do sistema

import openpyxl


# Ler um arquivo do excel
workbook = openpyxl.load_workbook('Base_dados_produtos_reais.xlxs')
workbook['vendas'] # selecionando a pagina para trabalhar