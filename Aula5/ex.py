class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.proprietario = None
    
    def definirProprietario(self, pessoa):
        self.proprietario = pessoa
    
    def mostrarInformacoes(self):
        info = (f'''
              Marca: {self.marca}
              Modelo: {self.modelo}
              Ano: {self.ano}
              ''')
        
        if self.proprietario:
           info += f',\nProprietario: {self.proprietario.nome}'
           info += f',\nIdade: {self.proprietario.idade}'
        else:
            info += '\n SEM PROPRIETARIO'
        print(info)
        
class Proprietario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

nomeProprietario = input("Digite o nome do proprietario: ")
idadeProprietario = input("Digite a idade do proprietario: ")
pessoa = Proprietario(nomeProprietario, idadeProprietario)

marca = input("Digite a marca do carro: ")
modelo = input("Digite o modelo do carro: ")
ano = input("Digite o ano do carro: ")

carro = Carro(marca, modelo, ano)

carro.definirProprietario(pessoa)
carro.mostrarInformacoes()

        