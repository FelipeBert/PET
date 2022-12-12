import random

class Conta():
    def __init__(self, numConta):
        self.numero = numConta
        self.saldo = 0

    def deposite(self, valor):
        self.saldo = self.saldo + valor - valor*0.1

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            return True
        else:
            return False

class Poupanca(Conta):

    def render(self):
        self.saldo = self.saldo + self.saldo*0.01

class Bonificada(Conta):

    def __init__(self, numConta):
        self.numero = numConta
        self.saldo = 0
        self.bonus = 0

    def deposite(self, valor):
        self.saldo = self.saldo + (valor*0.9)
        self.bonus += (valor * 0.0001)

    def rendimentoBonus(self):
        self.saldo += self.bonus
        self.bonus = 0

    def consultaBonus(self):
        return self.bonus

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
    
    def criarBonificada(self):
        num = random.randint(0, 1000)
        b = Bonificada(num)
        self.contas.append(b)
        return num

    def consultaSaldo(self, numConta):
        for conta in self.contas:
            if conta.numero == numConta:
                return conta.saldo
        return -1

    def depositar(self, numConta, valor):
        for conta in self.contas:
            if conta.numero == numConta and isinstance(conta, Bonificada):
                conta.deposite(valor)
            else:
                conta.deposite(valor)

    def deletar(self, numConta):
        for conta in self.contas:
            if conta.numero == numConta:
                self.contas.remove(conta)
                return True
        return False

    def sacar(self, numConta, valor):
        for conta in self.contas:
            if conta.numero == numConta:
                return conta.sacar(valor)

    def renderPoupanca(self, numConta):
        for i in self.contas:
            if i.numero == numConta and isinstance(i, Poupanca):
                i.render()
                return True
        return False

    def renderBonus(self, numConta):
        for i in self.contas:
            if i.numero == numConta and isinstance(i, Bonificada):
                i.rendimentoBonus()
                return True
        return False
    
    def consultaBonus(self, numConta):
        for i in self.contas:
            if i.numero == numConta and isinstance(i, Bonificada):
                return i.consultaBonus()
        return False