from enum import Enum, auto

class FormaPagamentoEnum(Enum):
    PIX = "Pix"
    CARTAO_DE_DEBITO = "Cartão de débito"
    CARTAO_DE_CREDITO = "Cartão de crédito"
    ESPECIE = "Espécie"
    BOLETO = "Boleto"