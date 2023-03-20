from utils import util
from random import randint
from datetime import date, datetime

class App():
    def __init__(self):
        pass

    def cadastrar_veiculo(self):
        marca = input('Digite a MARCA do veiculo: ')
        modelo = input('Digite o MODELO do veiculo: ')
        ano = input('Digite o ANO do veiculo: ')
        placa = input('Digite a PLACA do carro: ')
        quilometragem = int(input('Digite a QUILOMETRAGEM do veiculo: '))
        valorDaDiaria = int(input('Digite o VALOR DA DIARIA do Carro: '))
        car = self.Carro(marca, modelo, ano, placa, quilometragem, valorDaDiaria)
        print(f'{car} cadastrado!')
        return car

    def consultar_disponibilidade_de_veiculos(self, carList):
        carDisponiveis = []
        carIndisponiveis = []
        for veicle in carList:
            if veicle.estado == 'DISPONIVEL':
                carDisponiveis.append(veicle)
            else:
                carIndisponiveis.append(veicle)

        def menu():
            resp = int(input('1 - listar carros disponiveis\n2 - listar carros indisponiveis\ndigite sua escolha: '))
            return resp

        def mostrarVeiculos(resp):
            match(resp):
                case 1:
                    carDisLen = len(carDisponiveis)
                    print(f'Veiculos DISPONIVEIS({carDisLen}): \n')
                    print(carDisponiveis)
                case 2:
                    carIndisLen = len(carIndisponiveis)
                    print(f'Veiculos INDISPONIVEIS({carIndisLen}): \n')
                    print(carIndisponiveis)
                case _:
                    util.brokenProgram() 

        resp = menu()

        mostrarVeiculos(resp)

    def listar_veiculos_por_marca(self, carList): #Thiagoo
        self.carList = carList
        print(carList.carro[0])

    def listar_veiculos_por_modelo(self, carList): #thiagoo
        pass

    def ano_consulta(self, ano):
        return [car for car in self.carList if car.ano == ano] 
    
    def listar_veiculos_por_ano(self, carList):
    
        ano = int(input("Ano: "))
        carros_por_ano = self.carList(ano)
        if carros_por_ano:
            print(f'Veículos do ano {ano}:')
        for car in carros_por_ano:
            print(f'{i} - {car}')
            i = i + 1
        else:
            print(f'Não há veículos do modelo {ano}. ')

    def cadastrar_usuario(self):
        nome= input("Digite seu nome: ")
        id= input("Digite seu id: ")
        cliente= self.Cliente(self, self)
        cliente.cadastro_usuario(nome, id)
    

    def alugar_veiculo(self, carList, userList):
        for i, car in enumerate(carList):
            print(f'\ncarro {i}: {car}\n')
        resp = int(input('Digite o número do carro que deseja alugar: '))
        car = carList[resp]
        print(f'\ncarro: {car}')
        util.pauseAndClear()
        for i, user in enumerate(userList):
            print(f'\nusuario {i}: {user}\n')
        resp = int(input('Digite o número do seu usuario: '))
        user = userList[resp]
        print(f'\nuser: {user}\n')
        dataIni = input('digite a data que deseja pegar o veiculo (%dd/%mm/%yyyy): ')
        dataFim = input('digite a data que deseja entregar o veiculo (%dd/%mm/%yyyy): ')
        
        aluguel = self.Aluguel(user, car, dataIni, dataFim)
        print(aluguel)

    def devolver_veiculo(self):
        pass

    class Veiculo():
        def __init__(self, marca, modelo, ano):
            self.marca = marca
            self.modelo = modelo
            self.ano = ano
            self.estado = 'DISPONIVEL'
            self.nomeClasse = self.__class__.__name__

        def __str__(self):
            return f'{self.nomeClasse}: {self.marca}, {self.modelo}, {self.ano}'
    
        def __repr__(self):
            return f'\nMarca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Estado: {self.estado}\n'

        def set_estado(self):
            if self.estado == 'DISPONIVEL':
                self.estado = 'INDISPONIVEL'
            else:
                self.estado = 'DISPONIVEL'
            return self

    class Carro(Veiculo):
        def __init__(self, marca, modelo, ano, placa, quilometragem, valorDaDiaria):
            super().__init__(marca, modelo, ano)
            self.placa = placa
            self.quilometragem = quilometragem
            self.valorDaDiaria = valorDaDiaria
            self.nomeClasse = self.__class__.__name__

        def __str__(self):
            return f'{self.nomeClasse}: {self.marca}, {self.modelo}, {self.ano}'
    
        def __repr__(self):
            return f'\n{self.nomeClasse}: \n{self.marca}, {self.modelo},{self.ano}, placa: {self.placa}, {self.quilometragem}Km, {self.valorDaDiaria} R$ por dia\n'

    class Cliente():
        def __init__(self, nome, historicoDeCarrosAlugados=None):
            self.nome = nome
            self.id = randint(2, 5000) * randint(2, 5000)
            self.historicoDeCarrosAlugados = historicoDeCarrosAlugados
            self.nomeClasse = self.__class__.__name__

        def __str__(self):
            return f'{self.nomeClasse}: {self.nome}, id: {self.id}, historico de aluguel:\n{self.historicoDeCarrosAlugados}'
        
        def cadastro_usuario(self, nome, id):
            self.nome= nome 
            self.id= id
            self.historico= []
            self.historico.append(nome, id)
            

    class Aluguel:
        def __init__(self, user, car, dataIni, dataFim):
            self.user = user
            self.car = car
            self.dataIni = datetime.strptime(dataIni, '%d/%m/%Y').date()
            self.dataFim = datetime.strptime(dataFim, '%d/%m/%Y').date()
            hj = date.today().strftime('%d/%m/%Y')
            self.hj = datetime.strptime(hj, '%d/%m/%Y').date()
            self.diaria = self.car.valorDaDiaria
            self.qtDays = abs((self.dataFim - self.hj).days)
            self.taxa = self.qtDays * self.diaria * 0,20
            self.nomeClasse = self.__class__.__name__
        
        def __str__(self):
            if self.dataFim < self.hj:
                return f'{self.nomeClasse} de {self.user.nome}:\n{self.car.nomeClasse} {self.car}. com taxa de {self.taxa} R$ a ser paga'
            else:
                return f'{self.nomeClasse} de {self.user.nome}:\n{self.car.nomeClasse} {self.car} '
                
    def loadLists(self):
        c1 = self.Carro('Monza', 'Calhambeque', '2007', 'DEVIL', 0, 666)
        c2 = self.Carro('Shinerai', 'Fusca', '1986', '_ACDC_', 666, 69).set_estado()

        u1 = self.Cliente('Joaquim Tafarel de Fênix', '400')
        u2 = self.Cliente('Carlos Xavier de Pegáso', '47')

        userList = [u1, u2]
        
        carList = [c1,c2]

        return userList, carList