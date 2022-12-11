import random

class Conta():
    def __init__(self, numConta):
        self.numero = numConta
        self.saldo = 0

    def deposite(self, valor):
        self.saldo = self.saldo + valor
    
    def withdraw(self, valor):
        if self.saldo - valor >= 0:
            self.saldo -= valor
            return self.saldo
        else:
            return -1


class Banco():
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def getNome(self):
        return self.nome

    def criarConta(self):
        num = random.randint(0, 1000)
        c = Conta(num)
        self.contas.append(c)
        return num

    def consultaSaldo(self, numConta):
        for conta in self.contas:
            if conta.numero == numConta:
                return conta.saldo
        return -1

    def depositar(self, numConta, valor):
        for conta in self.contas:
            if conta.numero == numConta:
                conta.deposite(valor)

    def saque(self, numConta, valor):
        for conta in self.contas:
            if conta.numero == numConta:
                conta.withdraw(valor)


print("Bem-vindo")
bancoUfrpe = Banco("UABJ")
print("Menu")
print("0 - Sair")
print("1 - Criar uma Nova Conta")
print("2 - Consultar Saldo Conta")
print("3 - Depositar na Conta")
print("4 - Realizar saque")
escolha = int(input("digite a opção desejada:"))
while escolha > 0:
    if escolha == 1:
        # criar uma conta
        print("Criando Conta...")
        numConta = bancoUfrpe.criarConta()
        print("Conta criada:", numConta)
    elif escolha == 2:
        print("Consultando Saldo...")
        numConta = int(input("digite o numero da conta: "))
        saldo = bancoUfrpe.consultaSaldo(numConta)
        print("o saldo da conta", numConta, "é", saldo, "R$")
    elif escolha == 3:
        print("Depositando Conta...")
        numConta = int(input("digite o numero da conta: "))
        valor = int(input("digite o valor que deseja depositar: "))
        saldo = bancoUfrpe.depositar(numConta, valor)
        print("Valor Depositado")
    elif escolha == 4:
        print("Realizando saque...")
        numConta = int(input("Digite o numero da conta: "))
        valor = int(input("Digite o valor que deseja sacar: "))
        saldo = bancoUfrpe.saque(numConta, valor)
        if saldo == -1:
            print("Saldo Insuficiente!")
        else:
            print("Você realizou um saque de {} reais".format(saldo))
    escolha = int(input("digite a opção desejada:"))
