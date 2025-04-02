class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco
        
    def to_list(self):
        return [
            self.nome,
            self.preco            
        ]
        
    def __str__(self):
        return f"Produto(nome={self.nome}, preço={self.preco})"

    def __repr__(self):
        return f"Produto(nome='{self.nome}', preço={self.preco})"