from carro import Carro
from moto import Moto

carro = Carro(marca="Fiat", modelo="Uno", ano=2012, preco_diaria=150.0, numero_portas=4)
carro.calcular_aluguel(dias=10)

print("################################################")

moto = Moto(marca="Ducati", modelo="Ducati DesertX", ano=2021, preco_diaria=100.0, cilindrada=500)
moto.calcular_aluguel(dias=5)
