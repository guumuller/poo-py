class Produto:
    def __init__(self, codigo, nome, categoria, preco, quantidadeEstoque):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidadeEstoque = quantidadeEstoque

    def get_codigo(self):
        return self.codigo

    def get_nome(self):
        return self.nome

    def get_categoria(self):
        return self.categoria

    def get_preco(self):
        return self.preco

    def get_quantidade_estoque(self):
        return self.quantidadeEstoque

    def set_preco(self, novo_preco):
        self.preco = novo_preco

    def vender(self, quantidade_vendida):
        if quantidade_vendida > self.quantidadeEstoque:
            print("Estoque insuficiente para realizar a venda.")
            return
        self.quantidadeEstoque -= quantidade_vendida
        total_venda = quantidade_vendida * self.preco
        print(f"Venda realizada: {self.nome}, Categoria: {self.categoria}, "
              f"Quantidade Vendida: {quantidade_vendida}, Preço: {self.preco:.2f}, "
              f"Total da Venda: {total_venda:.2f}")

produto = Produto(1, "CAMISA", "Vestuário", 79.90, 75)
produto.vender(10)
