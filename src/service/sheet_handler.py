from openpyxl import load_workbook
from service.workbook_factory import WorkBookFactory
from model.venda import Venda

class SheetHandler:
    def __init__(self):
        self.nome_planilha = WorkBookFactory().workboook_name
    
    def registrar_venda(venda: Venda):
        factoy = WorkBookFactory()
        book = factoy.load_book()

        sheet_produtos = book["Produtos"]
        sheet_produtos.append([
            venda.produto.to_list(), 
            venda.cliente.name, 
            venda.data_hora_venda,
            venda.vendedor
        ])
        
        book.save()
    
    def load_products(self):
        # 1. Carregar a planilha
        planilha = load_workbook(self.nome_planilha)
        sheet_produtos = planilha["Produtos"]

        # 2. Extrair dados (assumindo que nome está na coluna A e valor na B)
        produtos_list = []
        for linha in sheet_produtos.iter_rows(min_row=2, values_only=True):  # Pula cabeçalho
            nome = linha[0]
            valor = linha[1]
            produtos_list.append({'nome': nome, 'valor': valor})

        return produtos_list