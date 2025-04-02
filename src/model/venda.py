from model.produto import Produto
from model.vendedor import Vendedor
from model.cliente import Cliente
from model.forma_pagamento import FormaPagamento
from datetime import datetime

class Venda:
    def __init__(self, produto: Produto, cliente: Cliente, forma_pagamento: FormaPagamento,  vendedor: Vendedor):
        self.produto = produto
        self.cliente = cliente
        self.forma_pagamento = forma_pagamento
        # self.data_hora_venda = data_hora_venda
        self.vendedor = vendedor
        