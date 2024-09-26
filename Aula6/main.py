from datetime import date

class Caminhao:
    def __init__(self, modelo, placa, capacidade_carga):
        self.modelo = modelo
        self.placa = placa
        self.capacidade_carga = capacidade_carga
        self.peso = None
        
    def carregar(self, peso):
        self.peso = peso
        
        if peso > capacidade_carga:
            print("O caminhão não suportará este peso!")
        else:
            print("O caminhão está disposto a carregar esta carga.")
        
    def descarregar(self, peso):
        peso = 0
        self.peso = peso
        
class Motorista:
    def __init__(self, nome, idade, CNH, dataValidade):
        self.nome = nome
        self.idade = idade
        self.CNH = CNH
        self.dataValidade = dataValidade

    def dirigir(self, caminhao):
        self.caminhao = caminhao
        print("O motorista estã diriginto o caminhão.")

    def verificarValidade(self, motorista):
        self.motorista = dataValidade
        
        
capacidade_carga = int(input("Digite a capacidade de carga do caminhão: "))
peso = int(input("Digite o peso da carga: "))
modelo = input("Digite o modelo do caminhão: ")
placa = input("Digite a placa do caminhão: ")
caminhao = Caminhao(modelo, placa, capacidade_carga)

caminhao.carregar(peso)
# caminhao.descarregar(peso)
print(caminhao.peso)


nome = input("Digite o nome do motorista: ")
idade = int(input("Digite a idade do mortorista: "))
CNH = int(input("Digite a CNH do motorista: "))
dataValidade = int(input("Digite a validade da CNH do motorista: "))
motorista = Motorista(nome, idade, CNH, dataValidade)

motorista.dirigir(caminhao)
