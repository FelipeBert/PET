import random

class Conta():
    def __init__(self, numConta, tipo):
        self.numero = numConta
        self.saldo = 0
        self.tipo = tipo

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

    def criarConta(self, tipo):
        num = random.randint(0, 1000)
        c = Conta(num, tipo)
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

    def remover(self, n_conta):
        indice = 0
        for i in self.contas:
            if i.numero == n_conta:
                del self.contas[indice]
                return 1
            else:
                indice += 1
        return -1
    
    def render(self, num):
        for i in self.contas:
            if i.numero == num and self.contas.tipo == 2:
                i.saldo = i.saldo + (0.01 * i.saldo)
                return i.saldo
        return -1