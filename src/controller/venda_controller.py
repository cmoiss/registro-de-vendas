from model.produto import Produto
from model.cliente import Cliente
from model.venda import Venda

class VendaController:
    def __init__(self, view, sheet_handler):
        self.view = view
        self.sheet_handler = sheet_handler
        self.produtos_list = []
        
        # Carrega os produtos
        self._carregar_produtos()
        
        # Configura os eventos da view
        self._setup_events()
    
    def _carregar_produtos(self):
        """Carrega a lista de produtos do SheetHandler"""
        self.produtos_list = self.sheet_handler.load_products()
        self.view.set_produtos(self.produtos_list)
    
    def _setup_events(self):
        """Configura os eventos da view"""
        self.view.bind_produto_selected(self.on_produto_selected)
    
    def on_produto_selected(self, event=None):
        """Callback para quando um produto é selecionado"""
        nome_selecionado = self.view.combobox_produtos.get()
        
        # Procura o produto correspondente na lista
        produto_selecionado = next(
            (produto for produto in self.produtos_list if produto.nome == nome_selecionado),
            None
        )
        
        # Se encontrou, atualiza o Entry com o preço
        if produto_selecionado:
            self.view.set_valor(produto_selecionado.preco)
    
    def cadastrar_venda(self):
        """Processa o cadastro de uma nova venda"""
        # Obtém os dados do formulário
        form_data = self.view.get_form_data()
        
        # Validação básica
        if not all(form_data.values()):
            self.view.show_error_message("Preencha todos os campos!")
            return
        
        # Cria a mensagem de sucesso
        mensagem = (
            f"Produto: {form_data['produto']}\n"
            f"Cliente: {form_data['cliente']}\n"
            f"Valor: R${form_data['valor']}\n"
            f"Pagamento: {form_data['pagamento']}\n"
            f"Vendedor: {form_data['vendedor']}"
        )
        
        # Aqui você pode adicionar a lógica para salvar no banco de dados
        # Por exemplo:
        # venda = Venda(...)
        # self.sheet_handler.save_venda(venda)
        
        # Mostra mensagem de sucesso e limpa o formulário
        self.view.show_success_message(mensagem)
        self.view.clear_form()