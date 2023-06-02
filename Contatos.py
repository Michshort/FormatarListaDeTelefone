# Nome do arquivo: contatos.py
 #* Autor: Michelli
 #* Data de criação: 08/04/2023
 #* Copyright (c) 2023 Michelli Susana da Silva
 #* Todos os direitos reservados.
 #*
 #* Este programa é de autoria de Michelli Susana da Silva e está protegido por direitos autorais.
 #* Você pode modificá-lo e/ou distribuí-lo livremente, desde que respeite os termos da licença MIT.
 
import re
import pandas as pd

# Carrega a planilha de contatos
df = pd.read_excel('contatos1.xlsx')

# Define o padrão de telefone que será utilizado
padrao = r'\d{2}\s*\d{2}\s*(\d{4,5})\s*(\d{4})'

# Função para formatar o número de telefone
def formatar_telefone(telefone):
     # Extrai apenas os dígitos do número de telefone
    digitos = re.sub(r'\D', '', telefone)
    
    # Remove os parênteses, caso existam
    digitos = digitos.replace('(', '').replace(')', '')
    
    # Verifica se o número já começa com '+55'
    if digitos.startswith('55'):
        # Remove o hífen, caso exista
        digitos = digitos.replace('-', '')
    else:
        # Adiciona o código '+55' no começo
        digitos = '55' + digitos
    
    # Formata o número de telefone no padrão desejado
    return f'+{digitos[:2]} {digitos[2:]}'

# Percorre a lista de números de telefone e formata cada um
for i, row in df.iterrows():
    telefone = str(row['Telefone'])
    if pd.isnull(telefone):
        continue
    telefone_formatado = formatar_telefone(re.sub('\s+|:::', '', telefone))
    df.at[i, 'Telefone'] = telefone_formatado


# Salva a nova tabela em um arquivo Excel
df.to_excel('contatos1_v3.xlsx', index=False)
