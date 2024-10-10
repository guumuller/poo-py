from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, preco_diaria, numero_portas):
        super().__init__(marca, modelo, ano, preco_diaria)
        self.numero_portas = numero_portas
         
    def calcular_aluguel(self, dias):
        total = dias * self.preco_diaria
        
        if dias > 7:
            desconto = total * 0.10  # 10% de desconto
            total -= desconto
            print(f"Desconto aplicado: R${desconto:.2f}")
        
        self.listar_veiculo()
        print(f"Total a pagar por {dias} dias: R${total:.2f}")
        return total