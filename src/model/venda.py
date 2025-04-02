from model.produto import Produto
from model.vendedor import Vendedor
from model.cliente import Cliente

class Venda:
    def __init__(self, produto: Produto, cliente: Cliente, data_hora_venda, vendedor: Vendedor):
        self.produto = produto
        self.cliente = cliente
        self.data_hora_venda = data_hora_venda
        self.vendedor = vendedor
        