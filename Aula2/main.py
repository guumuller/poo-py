class Conta:
    def __init__(self, numero, saldo, nome):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        
    # Função listar dados
    def listar(self):
        print('\n###############################################')
        print(f'Cliente: {self.nome}')
        print(f'Conta Corrente: {self.numero}')
        print(f'Saldo: {self.saldo}')

    #Função depositar valor
    def depositar(self, valor):
        self.saldo += valor
    
    #Função sacar valor
    def sacar(self, valor):
        self.saldo -= valor    

#Função entrada de dados
def entrada():
    nome = input('Digite o nome do cliente: ')
    numero = input('Digite a conta: ')
    saldo = float(input('Digite o saldo inicial: '))
    return(numero, saldo, nome)

if __name__ == '__main__':
    numero, saldo, nome = entrada()
    conta_gustavo = Conta(numero, saldo, nome)
    conta_gustavo.listar()
    
    nome, numero, saldo = entrada()
    conta_lisi = Conta(nome, numero, saldo)
    conta_lisi.listar()

"""
class Conta:
    numero=000000000
    saldo=0.0
    def listar(self):
         print("\n###############")
         print(f'Conta Corrente: {self.numero}')
         print(f'Saldo {self.saldo}')

    def depositar(self,valor):
        self.saldo += valor
    def sacar(self,valor):
        self.saldo -= valor

 
if __name__ == '__main__':
    contaHenrique = Conta()
    contaHenrique.listar()
    contaHenrique.numero="1234-5"
    contaHenrique.saldo=503.45

    contaHenrique.listar()
    conta_lisi=Conta()
    conta_lisi.numero="45312-5"
    conta_lisi.saldo=50.000
    conta_lisi.listar()
    contaHenrique.sacar(50)
    conta_lisi.depositar(50)
    conta_lisi.listar()
    contaHenrique.listar()
    
RESULTADO

###############
Conta Corrente: 0
Saldo 0.0

###############
Conta Corrente: 1234-5
Saldo 503.45

###############
Conta Corrente: 45312-5
Saldo 50.0

###############
Conta Corrente: 45312-5
Saldo 100.0

###############
Conta Corrente: 1234-5
Saldo 453.45
        
"""
