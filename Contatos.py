{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f244a6ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Nome do arquivo: contatos.py\n",
    " #* Autor: Michelli\n",
    " #* Data de criação: 08/04/2023\n",
    " #* Copyright (c) 2023 Michelli Susana da Silva\n",
    " #* Todos os direitos reservados.\n",
    " #*\n",
    " #* Este programa é de autoria de Michelli Susana da Silva e está protegido por direitos autorais.\n",
    " #* Você pode modificá-lo e/ou distribuí-lo livremente, desde que respeite os termos da licença MIT.\n",
    " \n",
    "import re\n",
    "import pandas as pd\n",
    "\n",
    "# Carrega a planilha de contatos\n",
    "df = pd.read_excel('contatos1.xlsx')\n",
    "\n",
    "# Define o padrão de telefone que será utilizado\n",
    "padrao = r'\\d{2}\\s*\\d{2}\\s*(\\d{4,5})\\s*(\\d{4})'\n",
    "\n",
    "# Função para formatar o número de telefone\n",
    "def formatar_telefone(telefone):\n",
    "     # Extrai apenas os dígitos do número de telefone\n",
    "    digitos = re.sub(r'\\D', '', telefone)\n",
    "    \n",
    "    # Remove os parênteses, caso existam\n",
    "    digitos = digitos.replace('(', '').replace(')', '')\n",
    "    \n",
    "    # Verifica se o número já começa com '+55'\n",
    "    if digitos.startswith('55'):\n",
    "        # Remove o hífen, caso exista\n",
    "        digitos = digitos.replace('-', '')\n",
    "    else:\n",
    "        # Adiciona o código '+55' no começo\n",
    "        digitos = '55' + digitos\n",
    "    \n",
    "    # Formata o número de telefone no padrão desejado\n",
    "    return f'+{digitos[:2]} {digitos[2:]}'\n",
    "\n",
    "# Percorre a lista de números de telefone e formata cada um\n",
    "for i, row in df.iterrows():\n",
    "    telefone = str(row['Telefone'])\n",
    "    if pd.isnull(telefone):\n",
    "        continue\n",
    "    telefone_formatado = formatar_telefone(re.sub('\\s+|:::', '', telefone))\n",
    "    df.at[i, 'Telefone'] = telefone_formatado\n",
    "\n",
    "\n",
    "# Salva a nova tabela em um arquivo Excel\n",
    "df.to_excel('contatos1_v3.xlsx', index=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b9697e88",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f17e632f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
