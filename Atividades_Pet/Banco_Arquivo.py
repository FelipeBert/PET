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

class Poupanca(Conta):

    def render(self, rende):
        self.saldo = self.saldo + self.saldo*rende

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
    
    def criarPoupanca(self):
        num = random.randint(0, 1000)
        p = Poupanca(num)
        self.contas.append(p)
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

    def remover(self, n_conta):
        indice = 0
        for i in self.contas:
            if i.numero == n_conta:
                del self.contas[indice]
                return 1
            else:
                indice += 1
        return -1
    
    def renderPoupanca(self, numConta, rend):
        for i in self.contas:
            if i.numero == numConta and isinstance(i, Poupanca):
                i.render(rend)
                return True
        return -1