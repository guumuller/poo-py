from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, preco_diaria, cilindrada):
        super().__init__(marca, modelo, ano, preco_diaria)
        self.cilindrada = cilindrada
        
    def calcular_aluguel(self, dias):
        valor = super().calcular_aluguel(dias)
        valor *= 1.05 
        self.listar_veiculo()
        print(f'Valor aluguel da moto por {dias} dias = R${valor}')