import customtkinter as ctk
from tkinter import messagebox
from service.sheet_handler import SheetHandler

def cadastrar_venda():
    # Obtém os valores dos campos
    produto = combobox_produtos.get()
    cliente = entry_cliente.get()
    valor = entry_valor.get()
    pagamento = combobox_formas_pagamento.get()
    vendedor = combobox_vendedor.get()

    # produto = Produto(produto)
    # venda = Venda()

    # Validação básica
    if not produto or not cliente or not valor or not pagamento or not vendedor:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    # Exibe os dados cadastrados (pode ser substituído por um banco de dados)
    mensagem = (
        f"Produto: {produto}\n"
        f"Cliente: {cliente}\n"
        f"Valor: R${valor}\n"
        f"Pagamento: {pagamento}\n"
        f"Vendedor: {vendedor}"
    )
    messagebox.showinfo("Venda Cadastrada", mensagem)

    # Limpa os campos após o cadastro
    combobox_produtos.set("Selecione o produto")
    entry_cliente.delete(0, "end")
    entry_valor.delete(0, "end")
    combobox_formas_pagamento.set("Selecione a forma de pagamento")
    combobox_vendedor.set("Selecione o vendedor")

# Configuração da janela principal
ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Cadastro de Vendas")
root.geometry("500x400")

# Frame principal
frame = ctk.CTkFrame(root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Título
label_titulo = ctk.CTkLabel(frame, text="Cadastro de Venda", font=("Arial", 18, "bold"))
label_titulo.pack(pady=10)

# Campos do formulário
produtos_list = SheetHandler().load_products()
produtos_names = [produto["nome"] for produto in produtos_list] 

combobox_produtos = ctk.CTkComboBox(frame, values=produtos_names, state="readonly")
combobox_produtos.set("Selecione o produto")
combobox_produtos.pack(pady=5, padx=10, fill="x")

entry_cliente = ctk.CTkEntry(frame, placeholder_text="Nome do Cliente")
entry_cliente.pack(pady=5, padx=10, fill="x")

entry_valor = ctk.CTkEntry(frame, placeholder_text="Valor da Venda (R$)")
entry_valor.pack(pady=5, padx=10, fill="x")

formas_pagamento = ["Pix", "Cartão de Débito", "Cartão de Crédito", "Espécie"]
combobox_formas_pagamento = ctk.CTkComboBox(frame, values=formas_pagamento, state="readonly")
combobox_formas_pagamento.set("Selecione a forma de pagamento")
combobox_formas_pagamento.pack(pady=5, padx=10, fill="x")

vendedores = ["Carlos", "Josenildo"]
combobox_vendedor = ctk.CTkComboBox(frame, values=vendedores, state="readonly")
combobox_vendedor.set("Selecione o vendedor")
combobox_vendedor.pack(pady=5, padx=10, fill="x")

# Botão de cadastro
botao_cadastrar = ctk.CTkButton(frame, text="Cadastrar Venda", command=cadastrar_venda)
botao_cadastrar.pack(pady=20)

root.mainloop()