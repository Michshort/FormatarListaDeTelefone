# Formatação de Números de Telefone para Lista de Contatos do WhatsApp
## Descrição do Projeto
Este projeto foi criado para solucionar a necessidade de formatar números de telefone em uma lista de contatos do WhatsApp. Muitas vezes, ao importar contatos para o WhatsApp, os números podem estar em diferentes formatos ou possuir caracteres indesejados, o que dificulta o uso correto e eficiente do aplicativo.

Através deste programa em Python, é possível automatizar o processo de formatação dos números de telefone, garantindo que todos estejam no formato adequado para importação no WhatsApp.

### Funcionalidades
Remove caracteres indesejados dos números de telefone, como espaços, hífens e parênteses.
Verifica se o número já possui o código de país '+55' no início.
Adiciona o código de país '+55' nos números que não possuem.
Formata os números no padrão '+55 19981356750' (sem hífen e sem espaços).
Atualiza a lista de contatos com os números formatados.
### Pré-requisitos
-- Python 3.x instalado
-- Bibliotecas pandas e openpyxl instaladas (instaláveis via pip)
#### Utilização
Clone o repositório para sua máquina local:
bash
Copy code
git clone https://github.com/seu-usuario/seu-projeto.git
Acesse o diretório do projeto:
bash
Copy code
cd seu-projeto
##### Instale as dependências:
Copy code
pip install pandas openpyxl
Coloque a lista de contatos no formato Excel (.xlsx) no diretório do projeto.

Abra o arquivo formatar_telefones.py em um editor de texto.

Na variável caminho_arquivo, substitua 'contatos.xlsx' pelo nome do seu arquivo de contatos.

Execute o programa:

Copy code
python formatar_telefones.py
O arquivo contatos_formatados.xlsx será gerado com os números de telefone formatados.

Importe o arquivo contatos_formatados.xlsx no WhatsApp para atualizar a lista de contatos com os números formatados.

#### Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar solicitações de pull com melhorias, correções de bugs ou novas funcionalidades.

##### Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.

##### Agradecimentos
Agradeço a todos os colaboradores e à comunidade de código aberto pelo suporte e pela contribuição para este projeto.

##### Status do Projeto
Este projeto está concluído e funcional, mas novas melhorias e funcionalidades podem ser adicionadas no futuro.

### Contato
Michelli Susana da Silva - https://www.linkedin.com/in/michelli-susana-silva-5b449559/                                                           
Email: michellisusanas@gmail.com 
