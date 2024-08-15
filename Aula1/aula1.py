"""from datetime import date

def idade():
    nome = input('Digite seu nome: ')
    ano = int(input('Digite o ano do seu nascimento: '))
    idade = date.today().year - ano
    informacoes = print('Olá {}! Você tem {} anos.'.format(nome, idade))
    if idade >= 16:
        print(f'{nome} pode votar')
    else:
        print(f'{nome} não pode votar')
    return informacoes

idade()"""
#########################################################################################################################
"""def infos():
    nome = input('Digite seu nome: ')
    ano_atual = int(input('Digite o ano atual:'))
    ano_nascimento = int(input('Digite o ano do seu nascimento:'))
    idade = (ano_atual - ano_nascimento)
    print(f'Olá, {nome}! Você tem {idade} anos.')
    
infos() """
#########################################################################################################################

from datetime import date

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi,{name}')
def calcula_idade(nome, ano):
    ano_atual= date.today().year
    idade = ano_atual - ano
    print(f'Idade de {nome} é {idade}'  )

    return(idade)

def data_atual():
    dt_atu= f'{date.today().day}/{date.today().month}/{date.today().year}'
   # print(f'{date.today().day}/{date.today().month}/{date.today().year}')
    return  dt_atu
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nome=input('Digite seu nome:')
    ano=int(input('Digite Ano de Nascimento:'))
    print_hi(nome)
    data_sistema=data_atual()
    print(data_sistema)
    idade_criatura = calcula_idade(nome,ano)
    if idade_criatura >=16:
        print(f'{nome} pode votar')
    else:
         print(f'{nome} NÃO pode votar')
