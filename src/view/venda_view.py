import customtkinter as ctk
from tkinter import messagebox
from model.forma_pagamento_enum import FormaPagamentoEnum

class VendaView:
    def _filter_numeric_input(self, event):
        """Filtra caracteres não numéricos e valida formato decimal."""
        current_text = self.entry_valor.get()
        new_text = "".join([c for c in current_text if c.isdigit() or c == "."])  # Permite números e .
        
        # Garante apenas um ponto decimal
        if new_text.count(".") > 1:
            new_text = new_text.replace(".", "", new_text.count(".") - 1)
        
        # Atualiza o texto do Entry (se houve mudança)
        if new_text != current_text:
            self.entry_valor.delete(0, ctk.END)
            self.entry_valor.insert(0, new_text)
    
    def __init__(self, root):
        self.root = root
        self.controller = None
        self._setup_ui()
    
    def set_controller(self, controller):
        self.controller = controller
    
    def _setup_ui(self):
        # Frame principal
        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Título
        self.label_titulo = ctk.CTkLabel(self.frame, text="Cadastro de Venda", font=("Arial", 18, "bold"))
        self.label_titulo.pack(pady=10)

        # Combobox de produtos
        self.combobox_produtos = ctk.CTkComboBox(
            self.frame, 
            values=[], 
            state="readonly"
        )
        self.combobox_produtos.set("Selecione o produto")
        self.combobox_produtos.pack(pady=5, padx=10, fill="x")

        # Campo de cliente
        self.entry_cliente = ctk.CTkEntry(self.frame, placeholder_text="Nome do Cliente")
        self.entry_cliente.pack(pady=5, padx=10, fill="x")

        # Campo de valor (com validação via evento KeyRelease)
        self.entry_valor = ctk.CTkEntry(
            self.frame,
            placeholder_text="Valor da Venda (R$)"
        )
        self.entry_valor.pack(pady=5, padx=10, fill="x")
        self.entry_valor.bind("<KeyRelease>", self._filter_numeric_input)  # Valida ao digitar

        # Combobox de formas de pagamento
        self.formas_pagamento = [forma.value for forma in FormaPagamentoEnum]
        self.combobox_formas_pagamento = ctk.CTkComboBox(
            self.frame, 
            values=self.formas_pagamento, 
            state="readonly"
        )
        self.combobox_formas_pagamento.set("Selecione a forma de pagamento")
        self.combobox_formas_pagamento.pack(pady=5, padx=10, fill="x")

        # Combobox de vendedores
        self.vendedores = ["Carlos", "Josenildo"]
        self.combobox_vendedor = ctk.CTkComboBox(
            self.frame, 
            values=self.vendedores, 
            state="readonly"
        )
        self.combobox_vendedor.set("Selecione o vendedor")
        self.combobox_vendedor.pack(pady=5, padx=10, fill="x")

        # Botão de cadastro
        self.botao_cadastrar = ctk.CTkButton(
            self.frame, 
            text="Cadastrar Venda", 
            command=self._on_cadastrar_venda
        )
        self.botao_cadastrar.pack(pady=20)
    
    def set_produtos(self, produtos):
        """Define a lista de produtos disponíveis no combobox"""
        produtos_names = [produto.nome for produto in produtos]
        self.combobox_produtos.configure(values=produtos_names)
    
    def bind_produto_selected(self, callback):
        """Vincula o evento de seleção de produto a uma função callback"""
        self.combobox_produtos.configure(command=callback)
    
    def get_form_data(self):
        try:
            valor = float(self.entry_valor.get()) if self.entry_valor.get() else 0.0
        except ValueError:
            valor = 0.0  # Fallback se houver erro (improvável com a validação)
        
        return {
            "produto": self.combobox_produtos.get(),
            "cliente": self.entry_cliente.get(),
            "valor": valor,
            "pagamento": self.combobox_formas_pagamento.get(),
            "vendedor": self.combobox_vendedor.get()
        }
    
    def clear_form(self):
        """Limpa todos os campos do formulário"""
        self.combobox_produtos.set("Selecione o produto")
        self.entry_cliente.delete(0, "end")
        self.entry_valor.delete(0, "end")
        self.combobox_formas_pagamento.set("Selecione a forma de pagamento")
        self.combobox_vendedor.set("Selecione o vendedor")
    
    def show_success_message(self, message):
        """Exibe uma mensagem de sucesso"""
        messagebox.showinfo("Venda Cadastrada", message)
    
    def show_error_message(self, message):
        """Exibe uma mensagem de erro"""
        messagebox.showerror("Erro", message)
    
    def set_valor(self, valor):
        """Define o valor no campo correspondente"""
        self.entry_valor.delete(0, ctk.END)
        self.entry_valor.insert(0, str(valor))
    
    def _on_cadastrar_venda(self):
        """Handler para o botão de cadastrar venda"""
        if self.controller:
            self.controller.cadastrar_venda()