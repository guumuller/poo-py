from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL ="mysql+mysqlconnector://root:@localhost/aluguel_veiculos"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

if __name__ == "__main__":
    Base.metadata.create_all(engine)

class Vehicle(Base):
    __tablename__ = 'veiculos'

    ID_veiculo = Column(Integer, primary_key=True, autoincrement=True)
    marca = Column(String(50), nullable=False)
    modelo = Column(String(50), nullable=False)
    placa=Column(String(20), nullable=False)
    ano = Column(Integer, nullable=False)
    valor_diaria = Column(Numeric(10,2), nullable=False)

def addVehicle(marca, modelo, ano, placa, valor_diaria):
    newVehicle=Vehicle(marca=marca, modelo=modelo, placa=placa, ano=ano, valor_diaria=valor_diaria)

    existing_vehicle = session.query(Vehicle).filter_by(placa=placa).first()
    if existing_vehicle:
        print(f'Vehicle with license plate {placa} already exists. Vehicle not added.')
        return

    newVehicle = Vehicle(marca=marca, modelo=modelo, placa=placa, ano=ano, valor_diaria=valor_diaria)

    session.add(newVehicle)
    session.commit()
    print(f'Vehicle has been added successfully.')

def updateVehicleForId(ID_veiculo):
    vehicle=session.query(Vehicle).filter_by(ID_veiculo=ID_veiculo).first()
    if vehicle:
        newValue=float(input('What is the new daily value of the vehicle? R$'))
        newPlate=str(input('What is the new license plate on the car?')).upper()
        vehicle.valor_diaria=newValue
        vehicle.placa=newPlate
        session.commit()
        print(f'Updated vehicle information!\nNew daily rate: R${newValue:.2f}.\nNew board: {newPlate}.')

def deleteVehicleForId(ID_veiculo):
    vehicle=session.query(Vehicle).filter_by(ID_veiculo=ID_veiculo).first()
    if vehicle:
        session.delete(vehicle)
        session.commit()
        print(f'Vehicle {vehicle.mark} model {vehicle.model}, year {vehicle.year}, plate: {vehicle.plate} has been successfully deleted from the bank.')
    else:
        print(f'Entered vehicle not found.')

def listVehicles():
    todos_veiculos=session.query(Vehicle).all()
    if todos_veiculos:
        for veiculo in todos_veiculos:
            print(f'ID: {veiculo.ID_veiculo} mark: {veiculo.marca} model: {veiculo.modelo} year: {veiculo.ano} plate: {veiculo.placa} daily rate: R${veiculo.valor_diaria}.')
    else:
        print('Vehicle was not found.')

def simulationDaily(ID_veiculo):
    veiculo=session.query(Vehicle).filter_by(ID_veiculo=ID_veiculo).first()
    if veiculo:
        dias=int(input('How many days will the vehicle be rented?'))
        sim = dias * veiculo.valor_diaria
        print(f'The value will be R${sim:2f}.')


class Admin(Base):
    __tablename__ = 'admin_sist'
    idAdmin = Column(Integer, primary_key=True, autoincrement=True)
    Administradores = Column(String(150), nullable=False)
    Senhas = Column(String(100), nullable=False)

def registerUser():
    print('User Registration: ')
    Administradores= input('New user name: ')
    Senhas = input('New user password: ')

    usuario_existente = session.query(Admin).filter_by(Administradores = Administradores).first()
    if usuario_existente:
        print('This username is already in use. Try another one.')
        return
    else:
        usuario_cadastrado = Admin(Administradores=Administradores, Senhas = Senhas)
        session.add(usuario_cadastrado)
        session.commit()
        print(f'User {Administradores} successfully registered.')

log_menu='''
========================
    Choose an option:
1 - Access system.
2 - Adduser. 
3 - Exit.
========================
'''

def login():
    while True:
        print(log_menu)
        choice=input('Choose an option:')
        if choice == '1':
            Administradores=input('Admin: ')
            Senhas = input('Password: ')
            usuario = session.query(Admin).filter_by(Administradores = Administradores, Senhas = Senhas).first()
            if usuario:
                    print(f'Welcome {Administradores}.')
                    return True
            else:
                print('Username or password is incorrect.')
                return False
        elif choice == '2':
            registerUser()
        elif choice == '3':
            print('Logging off.')
            break
        else:
            print('Option not recognized.')

opcoes='''
==================================================
        Options menu:
    1- Add vehicle.
    2- Update vehicle information with ID.
    3- Delete vehicle with ID.
    4- List characteristics of the vehicle.
    5- Daily simulation.
    6- Leave
=================================================== '''

def menu():
    while True:
        print(opcoes)
        choice=input('Choose an option: ')
        if choice =='1':
            marca=str(input('Vehicle make: ')).title()
            modelo=str(input('Vehicle model:')).title()
            ano=int(input('Year of manufacture of the vehicle: '))
            placa=str(input('License plate: ')).upper()
            valor_diaria=float(input('What is the daily cost of this vehicle? R$'))
            addVehicle(marca, modelo, ano, placa, valor_diaria)

        elif choice == '2':
            listVehicles()
            id=int(input('Enter the vehicle ID that will have its information updated: '))
            updateVehicleForId(id)
        elif choice == "3":
            listVehicles()
            id= int(input('Vehicle ID to be deleted: '))
            deleteVehicleForId(id)
        elif choice == '4':
            listVehicles()
        elif choice == '5':
            print('Vehicle daily simulation: ')
            listVehicles()
            id=int(input('What is the vehicle ID for the calculation? '))
            simulationDaily(id)
        elif choice == '6':
            print('Closing the vehicle rental system.')
            break
        else:
            print('Invalid option.')

if login():
    menu()
