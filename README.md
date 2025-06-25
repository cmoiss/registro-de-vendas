# 🚀 Sistema de Registro de Vendas para Camisas Esportivas ⚽🏀
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-UI%20Library-green)
![Openpyxl](https://img.shields.io/badge/Openpyxl-Excel%20Handling-red)
![License](https://img.shields.io/badge/License-MIT-orange)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)

## 📝 Descrição
Este é um sistema simples de registro de vendas desenvolvido em Python para um empreendedor no ramo de camisas esportivas. O sistema permite cadastrar vendas de forma intuitiva, armazenando os dados em uma planilha Excel com duas abas: "Vendas" e "Produtos".

## ✨ Funcionalidades
- Cadastro de vendas com os seguintes campos:
  - Nome do Produto (combobox alimentado pela lista de produtos)
  - Nome do Cliente
  - Valor da Venda (preenchido automaticamente, mas editável)
  - Forma de Pagamento (combobox com opções fixas)
  - Data da Venda
  - Vendedor (combobox com nomes fixos)
- Geração automática de planilha Excel se não existir
- Adição de novos registros à planilha existente
- Confirmação visual após cadastro bem-sucedido

## 🗂️ Estrutura da Planilha
O sistema trabalha com um arquivo Excel contendo duas abas:

### 📌 Aba "Vendas"
Contém os seguintes campos:
- Nome do Produto
- Valor
- Nome do Cliente
- Forma de Pagamento
- Data de Venda
- Vendedor

### 📌 Aba "Produtos"
Contém os seguintes campos:
- Nome do Produto
- Valor

## 🛠️ Tecnologias Utilizadas
- **Python**: Linguagem de programação principal
- **CustomTkinter**: Biblioteca para construção da interface gráfica
- **Openpyxl**: Biblioteca para manipulação de planilhas Excel
- **CX_Freeze**: Ferramenta para empacotamento do projeto

## ❓ Por que não usar...?
- **PyInstaller**: Optou-se por CX_Freeze para evitar falsos positivos no Windows Defender
- **Banco de dados relacional**: Considerado desnecessário para o escopo do projeto (MVP simples)

## 📋 Pré-requisitos
- Python 3.x instalado
- Dependências listadas no arquivo `requirements.txt`

## ⚙️ Instalação
1. Clone este repositório
2. Crie um ambiente virtual (opcional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Linux/Mac
   venv\Scripts\activate  # No Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Execução
Para executar o projeto em modo de desenvolvimento:
```bash
python app.py
```

## 📦 Empacotamento
Para criar um executável do projeto:
```bash
python setup.py build
```
(O arquivo `setup.py` deve estar configurado para usar CX_Freeze)

## 💻 Interface
A interface consiste em uma única tela com:
- Combobox para seleção de produto (com valores carregados da planilha)
- Campo para nome do cliente
- Campo para valor da venda (preenchido automaticamente, mas editável)
- Combobox para forma de pagamento (Pix, Cartão de débito, Cartão de crédito, Espécie, Boleto)
- Campo para data da venda
- Combobox para seleção de vendedor (Josenildo ou Carlos)
- Botão para confirmar o registro

Após o cadastro, uma caixa de diálogo confirma o sucesso da operação.

## 📝 Observações
- O valor na aba de Vendas pode diferir do valor na aba de Produtos (para acomodar descontos ou acréscimos)
- O sistema foi projetado para pequenos volumes de dados, sem necessidade de banco de dados complexo
- A planilha gerada pode ser facilmente compartilhada ou importada para outros sistemas
