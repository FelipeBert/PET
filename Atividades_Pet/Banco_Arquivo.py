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

    def remover(self, n_conta):
        for i in range(len(self.contas)):
            if self.contas[i].numero == n_conta:
                del self.contas[i]
                return 1
        return -1