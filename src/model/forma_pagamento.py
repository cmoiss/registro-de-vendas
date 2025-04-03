class FormaPagamento:
    def __init__(self, forma: str):
        self.forma = forma
        self.formas_pagamento = ["Pix", "Cartão de Débito", "Cartão de Crédito", "Espécie", "Boleto"]